from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).parent
DIST=ROOT/'dist'
manifest=json.loads((ROOT/'page_manifest.json').read_text())
errors=[]
warnings=[]
titles=set()
descriptions=set()
files=list(DIST.rglob('*.html'))

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[];self.images=[];self.h1=0;self.title='';self.metas={};self.canonical=[];self.ids=[];self.labels=[];self.inputs=[];self.schema=[];self.capture=None;self.buf=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag=='img':self.images.append(a)
        if tag=='meta' and a.get('name'):self.metas[a['name']]=a.get('content','')
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
        if tag=='label' and a.get('for'):self.labels.append(a['for'])
        if tag in ['input','select','textarea'] and a.get('id'):self.inputs.append(a['id'])
        if tag=='title' or (tag=='script' and a.get('type')=='application/ld+json'):
            self.capture=tag;self.buf=[]
    def handle_endtag(self,tag):
        if self.capture==tag:
            value=''.join(self.buf)
            if tag=='title':self.title=value
            else:self.schema.append(value)
            self.capture=None
    def handle_data(self,data):
        if self.capture:self.buf.append(data)

parsed={}
for file in files:
    page=Page();page.feed(file.read_text())
    parsed[file]=page
    if page.h1!=1:errors.append(f'{file.relative_to(DIST)}: expected one H1, found {page.h1}')
    if len(page.canonical)!=1:errors.append(f'{file.relative_to(DIST)}: missing or repeated canonical')
    if not page.metas.get('description'):errors.append(f'{file.relative_to(DIST)}: missing description')
    if 'noindex' not in page.metas.get('robots',''):errors.append(f'{file.relative_to(DIST)}: preview must use noindex')
    if len(page.ids)!=len(set(page.ids)):errors.append(f'{file.relative_to(DIST)}: duplicate HTML ids')
    for script in page.schema:
        try:
            data=json.loads(script)
            if not data.get('@graph'):errors.append(f'{file}: missing schema graph')
        except Exception as exc:errors.append(f'{file}: invalid JSON-LD: {exc}')
    for img in page.images:
        src=img.get('src','')
        if not img.get('alt'):errors.append(f'{file.relative_to(DIST)}: missing image alt text')
        if not img.get('width') or not img.get('height'):errors.append(f'{file.relative_to(DIST)}: missing image dimensions')
        if src.startswith('/') and not (DIST/src.lstrip('/')).is_file():errors.append(f'{file.relative_to(DIST)}: missing image {src}')
    for field in page.inputs:
        if field not in page.labels and field!='message-preview':errors.append(f'{file.relative_to(DIST)}: unlabelled field {field}')

for row in manifest:
    if row['title'] in titles:errors.append('Duplicate title: '+row['title'])
    if row['description'] in descriptions:errors.append('Duplicate description: '+row['description'])
    titles.add(row['title']);descriptions.add(row['description'])
    if len(row['title'])>65:warnings.append('Review title length: '+row['path'])
    if len(row['description'])>175:warnings.append('Review description length: '+row['path'])

for file,page in parsed.items():
    for href in page.links:
        url=urlsplit(href)
        if url.scheme or href.startswith('//'):continue
        path=unquote(url.path)
        target=file if not path else DIST/path.lstrip('/') if path.startswith('/') else file.parent/path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{file.relative_to(DIST)}: broken local link {href}')
        elif url.fragment and target.suffix=='.html':
            target_page=parsed.get(target)
            if target_page and url.fragment not in target_page.ids:errors.append(f'{file.relative_to(DIST)}: broken anchor {href}')

tree=ET.parse(DIST/'sitemap.xml')
locs=[node.text for node in tree.getroot().iter() if node.tag.endswith('loc')]
expected={x['canonical'] for x in manifest if x['path']!='/404/'}
if set(locs)!=expected:errors.append('Sitemap URLs do not match page canonicals')
total_assets=sum(p.stat().st_size for p in (DIST/'assets').rglob('*') if p.is_file())
report={'pages':len(manifest),'html_files':len(files),'sitemap_urls':len(locs),'product_pages':len([x for x in manifest if x['path'].startswith('/products/')])-1,'total_asset_bytes':total_assets,'errors':errors,'warnings':warnings}
print(json.dumps(report,indent=2))
sys.exit(1 if errors else 0)
