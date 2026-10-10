const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync('dist/assets/site.js', 'utf8');

class Element {
  constructor(value = '') {
    this.value = value; this.hidden = false; this.dataset = {};
    this.listeners = {}; this.attributes = {}; this.children = [];
    this.options = []; this.validationMessage = '';
  }
  addEventListener(name, handler) { (this.listeners[name] ||= []).push(handler); }
  async fire(name, event = {}) { for (const handler of this.listeners[name] || []) await handler(event); }
  setAttribute(name, value) { this.attributes[name] = value; }
  setCustomValidity(value) { this.validationMessage = value; }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children = [...nodes]; }
  focus() { this.focused = true; }
  select() { this.selected = true; }
  scrollIntoView() { this.scrolled = true; }
  get selectedIndex() { return this.options.findIndex(option => option.value === this.value); }
}

function boot(ids, selectors = {}, search = '', scrollY = 0) {
  const events = [];
  const listeners = {};
  const document = {
    getElementById: id => ids[id] || null,
    querySelector: selector => selectors[selector] || null,
    querySelectorAll: selector => selectors[selector] || [],
    createElement: () => new Element(),
    addEventListener() {}
  };
  const window = {
    scrollY,
    addEventListener: (name, handler) => (listeners[name] ||= []).push(handler),
    dispatchEvent: event => events.push(event),
    matchMedia: () => ({ matches: true })
  };
  const location = { search, pathname: '/contact/', href: 'https://example.com/contact/' + search };
  vm.runInNewContext(source, {
    document, window, location, URL, URLSearchParams,
    history: { replaceState() {} }, navigator: {},
    CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options.detail; } }
  });
  return { window, events, emit: name => (listeners[name] || []).forEach(handler => handler()) };
}

async function main() {
  // Exercise the actual script using small DOM stand-ins; no browser or messages are opened.
  const header = new Element();
  const classes = new Set();
  header.classList = { toggle(name, active) { if (active) classes.add(name); else classes.delete(name); } };
  const headerContext = boot({}, { '.site-header': header });
  assert.equal(classes.has('is-scrolled'), false);
  headerContext.window.scrollY = 80; headerContext.emit('scroll');
  assert.equal(classes.has('is-scrolled'), true);
  headerContext.window.scrollY = 0; headerContext.emit('scroll');
  assert.equal(classes.has('is-scrolled'), false);
  headerContext.window.scrollY = 160; headerContext.emit('pageshow');
  assert.equal(classes.has('is-scrolled'), true);
  classes.clear(); boot({}, { '.site-header': header }, '', 160);
  assert.equal(classes.has('is-scrolled'), true);

  const result = new Element();
  const ducts = new Element('unknown');
  const choice = new Element('home');
  const label = new Element();
  boot({ 'finder-result': result, ducts }, {
    'input[name="use-case"]:checked': choice,
    'input[name="use-case"]': [choice],
    'label[for="ducts"]': label
  });
  const recommendation = () => result.children[1].children[2].href;
  assert.equal(recommendation(), '/products/ductfit-mobile/');
  ducts.value = 'yes'; await ducts.fire('change');
  assert.equal(recommendation(), '/products/ductfit-vent/');
  choice.value = 'car'; await choice.fire('change');
  assert.equal(recommendation(), '/products/ductfit-s/');
  assert.equal(ducts.hidden, true);
  choice.value = 'monitor'; await choice.fire('change');
  assert.equal(recommendation(), '/products/ductfit-kleansense-iaq-sensor/');
  assert.match(result.children[1].children[1].textContent, /separate from air purification/);

  const filters = ['all', 'cars', 'rooms', 'buildings', 'monitoring'].map(value => {
    const el = new Element(); el.dataset.filter = value; return el;
  });
  const cards = ['cars', 'rooms', 'rooms', 'buildings', 'monitoring'].map(value => {
    const el = new Element(); el.dataset.category = value; return el;
  });
  const count = new Element();
  boot({ 'product-count': count }, {
    '[data-filter]': filters, '.catalog-grid .product-card': cards
  }, '?filter=invalid');
  assert.equal(count.textContent, '5 products');
  await filters[2].fire('click');
  assert.equal(count.textContent, '2 products');
  assert.deepEqual(cards.map(card => card.hidden), [true, false, false, true, true]);
  assert.equal(filters[2].attributes['aria-pressed'], 'true');
  await filters[4].fire('click');
  assert.equal(count.textContent, '1 product');

  const ids = Object.fromEntries([
    'enquiry-form', 'name', 'contact', 'space', 'location', 'size', 'message', 'product',
    'message-preview', 'whatsapp-draft', 'email-draft', 'enquiry-result', 'copy-status',
    'prepare-enquiry', 'copy-enquiry'
  ].map(id => [id, new Element()]));
  ids.product.options = [
    { value: '', textContent: 'Help me choose' },
    { value: 'ductfit-mobile', textContent: 'ductFIT Mobile' }
  ];
  ids['enquiry-result'].hidden = true;
  ids['enquiry-form'].reportValidity = () => !ids.name.validationMessage && !ids.contact.validationMessage;
  const context = boot(ids, {}, '?product=ductfit-mobile&space=office');
  assert.equal(ids.product.value, 'ductfit-mobile');
  assert.equal(ids.space.value, 'Office or retail');
  assert.equal(ids['prepare-enquiry'].disabled, false);
  assert.equal(ids['prepare-enquiry'].type, 'submit');
  let prevented = 0;
  await ids['enquiry-form'].fire('submit', { preventDefault() { prevented++; } });
  assert.equal(ids['enquiry-result'].hidden, true);
  assert.equal(context.window.dataLayer, undefined);
  assert.match(ids.name.validationMessage, /enter your name/);
  ids.name.value = 'Test & Review'; ids.contact.value = 'test@example.com';
  await ids.name.fire('input', { target: ids.name });
  await ids.contact.fire('input', { target: ids.contact });
  ids.message.value = '<script>example</script> & a question?';
  await ids['enquiry-form'].fire('submit', { preventDefault() { prevented++; } });
  const draft = ids['message-preview'].value;
  const whatsapp = new URL(ids['whatsapp-draft'].href);
  assert.equal(whatsapp.hostname, 'wa.me');
  assert.equal(whatsapp.pathname, '/971501169833');
  assert.equal(whatsapp.searchParams.get('text'), draft);
  const email = new URL(ids['email-draft'].href);
  assert.equal(email.pathname, 'info@cleanairme.com');
  assert.equal(email.searchParams.get('body'), draft);
  assert.match(draft, /Name: Test & Review\nContact: test@example.com/);
  assert.match(draft, /Product: ductFIT Mobile/);
  assert.equal(ids['enquiry-result'].hidden, false);
  assert.equal(ids['enquiry-result'].focused, true);
  assert.equal(prevented, 2);
  const tracked = JSON.stringify(context.window.dataLayer);
  assert.match(tracked, /enquiry_draft_created/);
  assert.doesNotMatch(tracked, /Test & Review|test@example.com|<script>/);
  await ids['copy-enquiry'].fire('click');
  assert.equal(ids['message-preview'].selected, true);
  assert.match(ids['copy-status'].textContent, /copy command/);

  const contactHtml = fs.readFileSync('dist/contact/index.html', 'utf8');
  assert.match(contactHtml, /id="prepare-enquiry" type="button" disabled/);
  console.log('Passed: scroll header, restored scroll position, finder choices, filter results, enquiry validation, draft links, privacy-safe events and clipboard fallback.');
}
main().catch(error => { console.error(error); process.exitCode = 1; });
