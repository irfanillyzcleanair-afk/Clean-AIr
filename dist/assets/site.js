'use strict';
(function () {
  var header = document.querySelector('.site-header');
  if (header) {
    function updateHeaderColour() {
      header.classList.toggle('is-scrolled', window.scrollY > 24);
    }
    updateHeaderColour();
    window.addEventListener('scroll', updateHeaderColour, { passive: true });
    window.addEventListener('pageshow', updateHeaderColour);
  }

  var nav = document.getElementById('site-nav');
  var toggle = document.querySelector('.menu-toggle');
  if (nav && toggle) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') !== 'true';
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      nav.classList.toggle('is-open', open);
    });
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation');
      });
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation');
        toggle.focus();
      }
    });
  }

  function track(name, values) {
    var details = Object.assign({ event: name, page_path: location.pathname }, values || {});
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(details);
    window.dispatchEvent(new CustomEvent('cleanair:interaction', { detail: details }));
  }
  document.querySelectorAll('[data-track]').forEach(function (link) {
    link.addEventListener('click', function () { track(link.dataset.track); });
  });

  var filters = document.querySelectorAll('[data-filter]');
  if (filters.length) {
    var allowed = ['all', 'cars', 'rooms', 'buildings', 'monitoring'];
    var initial = new URLSearchParams(location.search).get('filter') || 'all';
    if (allowed.indexOf(initial) === -1) initial = 'all';
    function applyFilter(value) {
      var count = 0;
      document.querySelectorAll('.catalog-grid .product-card').forEach(function (card) {
        var visible = value === 'all' || card.dataset.category === value;
        card.hidden = !visible;
        if (visible) count += 1;
      });
      filters.forEach(function (filter) {
        filter.setAttribute('aria-pressed', String(filter.dataset.filter === value));
      });
      document.getElementById('product-count').textContent = count + (count === 1 ? ' product' : ' products');
    }
    applyFilter(initial);
    filters.forEach(function (filter) {
      filter.addEventListener('click', function () {
        applyFilter(filter.dataset.filter);
        var url = new URL(location.href);
        if (filter.dataset.filter === 'all') url.searchParams.delete('filter');
        else url.searchParams.set('filter', filter.dataset.filter);
        history.replaceState(null, '', url);
        track('product_filter_selected', { category: filter.dataset.filter });
      });
    });
  }

  var finder = document.getElementById('finder-result');
  if (finder) {
    var ducts = document.getElementById('ducts');
    var options = {
      s: { slug: 'ductfit-s', name: 'ductFIT S', image: 'ductfit-s.png', description: 'A portable option to discuss for a car or small personal space.' },
      mobile: { slug: 'ductfit-mobile', name: 'ductFIT Mobile', image: 'ductfit-mobile.png', description: 'Start with a standalone option. Our team can compare other room configurations.' },
      vent: { slug: 'ductfit-vent', name: 'ductFIT Vent', image: 'ductfit-vent.png', description: 'An HVAC-integrated starting point. Duct layout and airflow need a closer look.' },
      monitor: { slug: 'ductfit-kleansense-iaq-sensor', name: 'KleanSense IAQ Sensor', image: 'ductfit-kleansense-iaq-sensor.png', description: 'A monitor for environmental readings. It is separate from air purification.' }
    };
    function updateFinder() {
      var use = document.querySelector('input[name="use-case"]:checked').value;
      var ductRelevant = use === 'home' || use === 'office';
      ducts.hidden = !ductRelevant;
      document.querySelector('label[for="ducts"]').hidden = !ductRelevant;
      var result = use === 'car' ? options.s : use === 'monitor' ? options.monitor : ducts.value === 'yes' ? options.vent : options.mobile;
      finder.replaceChildren();
      var photo = document.createElement('img');
      photo.src = '/assets/' + result.image;
      photo.alt = result.name + ' device';
      photo.width = 95;
      photo.height = 95;
      var copy = document.createElement('div');
      var heading = document.createElement('h3');
      heading.textContent = result.name;
      var text = document.createElement('p');
      text.textContent = result.description;
      var link = document.createElement('a');
      link.className = 'text-link';
      link.href = '/products/' + result.slug + '/';
      link.textContent = 'Explore this starting point →';
      copy.append(heading, text, link);
      finder.append(photo, copy);
    }
    document.querySelectorAll('input[name="use-case"]').forEach(function (input) { input.addEventListener('change', updateFinder); });
    ducts.addEventListener('change', updateFinder);
    updateFinder();
  }

  var form = document.getElementById('enquiry-form');
  if (form) {
    var query = new URLSearchParams(location.search);
    var product = document.getElementById('product');
    var requestedProduct = query.get('product');
    if (requestedProduct && Array.from(product.options).some(function (option) { return option.value === requestedProduct; })) product.value = requestedProduct;
    var space = document.getElementById('space');
    var requestedSpace = (query.get('space') || '').toLowerCase();
    var spaces = { 'homes and villas': 'Home or villa', 'offices and retail': 'Office or retail', 'hotels and hospitality': 'Hotel or hospitality', 'schools and education': 'School or education', 'healthcare settings': 'Healthcare setting', 'transport and mobility': 'Transport', 'car': 'Car', 'home': 'Home or villa', 'office': 'Office or retail' };
    if (spaces[requestedSpace]) space.value = spaces[requestedSpace];
    ['name', 'contact'].forEach(function (id) {
      document.getElementById(id).addEventListener('input', function (event) { event.target.setCustomValidity(''); });
    });
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var name = document.getElementById('name');
      var contact = document.getElementById('contact');
      if (!name.value.trim()) name.setCustomValidity('Please enter your name.');
      if (!contact.value.trim()) contact.setCustomValidity('Please enter a phone number or email address.');
      if (!form.reportValidity()) return;
      var lines = ['Hello CleanAir, I would like help choosing an air solution.', '', 'Name: ' + name.value.trim(), 'Contact: ' + contact.value.trim()];
      if (space.value) lines.push('Space: ' + space.value);
      var locationField = document.getElementById('location').value.trim();
      if (locationField) lines.push('Location: ' + locationField);
      var size = document.getElementById('size').value.trim();
      if (size) lines.push('Approximate room area: ' + size);
      lines.push('Product: ' + (product.value ? product.options[product.selectedIndex].textContent : 'Please help me choose'));
      var message = document.getElementById('message').value.trim();
      if (message) lines.push('', 'I would like help with: ' + message);
      var draft = lines.join('\n');
      document.getElementById('message-preview').value = draft;
      document.getElementById('whatsapp-draft').href = 'https://wa.me/971501169833?text=' + encodeURIComponent(draft);
      document.getElementById('email-draft').href = 'mailto:info@cleanairme.com?subject=' + encodeURIComponent('Air solution enquiry' + (product.value ? ' — ' + product.options[product.selectedIndex].textContent : '')) + '&body=' + encodeURIComponent(draft);
      var result = document.getElementById('enquiry-result');
      result.hidden = false;
      document.getElementById('copy-status').textContent = '';
      result.focus();
      result.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
      track('enquiry_draft_created', { product: product.value || 'help_me_choose', space_type: space.value || 'unspecified' });
    });
    var prepareButton = document.getElementById('prepare-enquiry');
    prepareButton.type = 'submit';
    prepareButton.disabled = false;
    document.getElementById('copy-enquiry').addEventListener('click', async function () {
      var preview = document.getElementById('message-preview');
      var status = document.getElementById('copy-status');
      try {
        if (!navigator.clipboard) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(preview.value);
        status.textContent = 'Message copied. You can paste it into your preferred conversation.';
      } catch (error) {
        preview.focus();
        preview.select();
        status.textContent = 'Select and copy the message above using your device’s copy command.';
      }
    });
  }
})();
