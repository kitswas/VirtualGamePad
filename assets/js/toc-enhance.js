/* Enhanced TOC behavior: affix, active-section highlighting, and auto-scroll */
(function () {
	function safeId(href) { return href && href.charAt(0) === '#' ? href.slice(1) : null }
	document.addEventListener('DOMContentLoaded', function () {
		var toc = document.getElementById('markdown-toc');
		if (!toc) return;
		// sentinel to toggle affix class when TOC scrolls past top
		var sentinel = document.createElement('div');
		sentinel.className = 'toc-sentinel';
		toc.parentNode.insertBefore(sentinel, toc);
		var sentObs = new IntersectionObserver(function (entries) {
			entries.forEach(function (e) {
				if (!e.isIntersecting) toc.classList.add('affix'); else toc.classList.remove('affix');
			});
		}, { root: null, threshold: 0, rootMargin: '-1px 0px 0px 0px' });
		sentObs.observe(sentinel);

		var links = Array.from(toc.querySelectorAll('a[href^="#"]'));
		var targets = links.map(function (a) { return document.getElementById(safeId(a.getAttribute('href'))) }).filter(Boolean);
		if (targets.length === 0) return;

		var offsets = new Map();
		var visible = new Set();
		var first = true;
		var tocContainsOverscroll = getComputedStyle(toc).overscrollBehaviorY === 'contain';

		function setActive(activeEl) {
			links.forEach(function (a) { a.style.fontWeight = '' });
			if (!activeEl) return;
			var selector = 'a[href="#' + activeEl.id + '"]';
			var link = toc.querySelector(selector);
			if (link) {
				link.style.fontWeight = 'bold';
				if (tocContainsOverscroll) {
					clearTimeout(link.__tocScrollTimer);
					link.__tocScrollTimer = setTimeout(function () {
						if (toc.classList.contains('affix')) link.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
					}, 100);
				}
			}
		}

		var observer = new IntersectionObserver(function (entries) {
			if (first) {
				targets.forEach(function (t) { offsets.set(t, t.getBoundingClientRect().top + window.pageYOffset); });
				first = false;
			}
			entries.forEach(function (entry) {
				var el = entry.target;
				if (entry.isIntersecting) visible.add(el); else visible.delete(el);
			});
			if (visible.size === 0) { setActive(null); return; }
			var active = null;
			visible.forEach(function (el) { if (!active || offsets.get(el) < offsets.get(active)) active = el; });
			setActive(active);
		}, { root: null, threshold: [0, 0.1, 0.5, 1] });

		targets.forEach(function (t) { observer.observe(t) });
		window.addEventListener('unload', function () { observer.disconnect(); sentObs.disconnect(); });
	});
})();
