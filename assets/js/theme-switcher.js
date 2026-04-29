const themeStorageKey = 'vgp-theme';

function getThemeMap() {
	const mapNode = document.getElementById('theme-style-map');
	if (!mapNode) return null;

	try {
		return JSON.parse(mapNode.textContent || '{}');
	} catch (error) {
		console.error('Failed to parse theme map JSON.', error);
		return null;
	}
}

function getDefaultTheme() {
	const mapNode = document.getElementById('theme-style-map');
	if (!mapNode) return null;

	const defaultTheme = mapNode.getAttribute('data-default-theme');
	return defaultTheme || null;
}

function applyTheme(theme, themeMap) {
	if (!themeMap) return;

	const stylesheet = document.getElementById('theme-stylesheet');
	if (!stylesheet) return;

	const fallbackTheme = getDefaultTheme() || Object.keys(themeMap)[0];
	const nextTheme = themeMap[theme] ? theme : fallbackTheme;
	if (!nextTheme) return;

	stylesheet.setAttribute('href', themeMap[nextTheme]);
	stylesheet.setAttribute('data-theme', nextTheme);

	const select = document.getElementById('theme-select');
	if (select) select.value = nextTheme;
}

function loadSwitcherStyles() {
	const scriptTag = document.currentScript;
	if (!scriptTag) return;

	const switcherHref = scriptTag.getAttribute('data-switcher-css');
	if (!switcherHref) return;

	if (document.querySelector('link[data-switcher-css]')) return;

	const link = document.createElement('link');
	link.rel = 'stylesheet';
	link.href = switcherHref;
	link.setAttribute('data-switcher-css', 'true');
	document.head.appendChild(link);
}

function initThemeSwitcher() {
	const themeMap = getThemeMap();
	if (!themeMap) return;

	const select = document.getElementById('theme-select');
	const storedTheme = localStorage.getItem(themeStorageKey);
	const initialTheme = storedTheme || getDefaultTheme();

	if (initialTheme) applyTheme(initialTheme, themeMap);

	if (!select) return;

	select.addEventListener('change', (event) => {
		const nextTheme = event.target.value;
		applyTheme(nextTheme, themeMap);
		localStorage.setItem(themeStorageKey, nextTheme);
	});
}

function initThemeSwitcherAfterRender() {
	requestAnimationFrame(() => {
		loadSwitcherStyles();
		initThemeSwitcher();
	});
}

if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', initThemeSwitcherAfterRender);
} else {
	initThemeSwitcherAfterRender();
}
