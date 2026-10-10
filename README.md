# CleanAir website

Source files and the ready-to-serve static build of the CleanAir Website Demo.

Live demo: https://cleanair-sales-demo.rockyhero4.chatgpt.site/

## Included

- Twenty pages, including nine product pages and a custom 404 page.
- Authentic CleanAir logo and device images.
- Responsive navigation, product filters and a product finder.
- Enquiry drafts with WhatsApp, email and copy actions.
- Technology, company, contact, privacy and air quality guide pages.
- Page metadata, structured data, sitemap and asset provenance.

## Run locally

Python 3 is sufficient to serve the existing website. From the repository root:

```sh
python3 -m http.server 8080 --directory dist
```

Open http://localhost:8080/ in a browser. Serve the `dist` directory as the website root so links such as `/products/` and `/assets/` work correctly.

## Rebuild the demo

The Python build script uses the standard library. Images, CSS and JavaScript are already included in `dist/assets/`.

```sh
python3 build_site.py --base-url https://cleanair-sales-demo.rockyhero4.chatgpt.site --mode demo
```

Demo pages retain `noindex` directives. Set `--base-url` to the actual deployment origin when rebuilding for another host.

## Verify

Python 3 and Node.js are needed for the included checks; no package installation is required.

```sh
python3 verify_site.py
node --check dist/assets/site.js
node verify_interactions.cjs
```

The checks cover internal links, image references, page metadata, sitemap consistency, product filtering, product recommendations and enquiry draft handling.

## Files

| Path | Purpose |
| --- | --- |
| `dist/` | Static website files to serve or deploy |
| `dist/assets/` | Brand images, product images, styles and interactions |
| `build_site.py` | Generates pages and SEO metadata |
| `page_manifest.json` | Page paths, titles, descriptions and canonical URLs |
| `verify_site.py` | Static website checks |
| `verify_interactions.cjs` | JavaScript interaction checks |
| `asset_sources.json` | Image and product source references |
| `content_sources.json` | Brochure and content source references |

## Hosting

Deploy the contents of `dist/` with a static host that serves the website at the domain root. Uploading this repository does not configure hosting or change the company's existing website at https://cleanairme.com/.

For an approved production release, rebuild with the real production domain and `--mode production`, then review the product information, privacy notice and redirects before using the company's hosting workflow. The current static verifier expects demo `noindex` directives.

## Enquiry handling

The contact form prepares a message; it does not store or automatically deliver an enquiry. Visitors send the draft themselves through WhatsApp or email. No analytics account or server-side enquiry service is connected.

The original source references are retained. Raw user-supplied brochures, hosting credentials and internal Sites configuration are not included in this repository.
