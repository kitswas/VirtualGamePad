// TOC Scroll Tracking
let tocObserver;
function initTocTracking() {
    if (tocObserver) tocObserver.disconnect();

    const tocLinks = document.querySelectorAll('.toc nav a');
    const headings = Array.from(document.querySelectorAll('.content h2, .content h3'))
        .filter(h => h.id);

    if (!tocLinks.length || !headings.length) return;

    tocObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocLinks.forEach(link => {
                    const href = link.getAttribute('href');
                    if (href === `#${entry.target.id}`) {
                        link.classList.add('active');
                    } else {
                        link.classList.remove('active');
                    }
                });
            }
        });
    }, {
        rootMargin: '-10% 0px -80% 0px',
        threshold: 0
    });

    headings.forEach(h => tocObserver.observe(h));
}

// Initialize on first load
document.addEventListener('DOMContentLoaded', () => {
    initTocTracking();
});

// View Transitions API helper
function transitionTo(url) {
    console.log('Transitioning to:', url);
    if (!document.startViewTransition) {
        console.log('View Transitions API not supported, falling back to standard navigation');
        window.location.href = url;
        return;
    }

    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            return response.text();
        })
        .then(html => {
            const parser = new DOMParser();
            const newDoc = parser.parseFromString(html, 'text/html');

            const newContent = newDoc.querySelector('.content')?.innerHTML;
            const newTitle = newDoc.title;
            const newToc = newDoc.querySelector('.toc-sidebar');
            const newSidebarMenu = newDoc.querySelector('.menu')?.innerHTML;

            if (!newContent || !newSidebarMenu) {
                console.warn('Could not find required elements in new page, falling back');
                window.location.href = url;
                return;
            }

            document.startViewTransition(() => {
                // Update Title
                document.title = newTitle;

                // Update Meta Tags
                const metaTags = [
                    { name: 'description', isProperty: false },
                    { name: 'og:title', isProperty: true },
                    { name: 'og:description', isProperty: true },
                    { name: 'og:image', isProperty: true },
                    { name: 'og:url', isProperty: true },
                    { name: 'twitter:title', isProperty: false },
                    { name: 'twitter:description', isProperty: false },
                    { name: 'twitter:image', isProperty: false }
                ];

                metaTags.forEach(tag => {
                    const selector = tag.isProperty ? `meta[property="${tag.name}"]` : `meta[name="${tag.name}"]`;
                    const newMeta = newDoc.querySelector(selector);
                    const oldMeta = document.querySelector(selector);
                    if (newMeta && oldMeta) {
                        oldMeta.setAttribute('content', newMeta.getAttribute('content'));
                    }
                });

                // Update Content
                document.querySelector('.content').innerHTML = newContent;

                // Update Sidebar Active State
                document.querySelector('.menu').innerHTML = newSidebarMenu;

                // Update TOC
                const currentToc = document.querySelector('.toc-sidebar');
                const container = document.querySelector('.container');

                if (newToc) {
                    if (currentToc) {
                        currentToc.innerHTML = newToc.innerHTML;
                    } else {
                        const tocAside = document.createElement('aside');
                        tocAside.className = 'toc toc-sidebar';
                        tocAside.id = 'toc-container';
                        tocAside.innerHTML = newToc.innerHTML;
                        container.appendChild(tocAside);
                    }
                } else if (currentToc) {
                    currentToc.remove();
                }

                window.history.pushState({}, '', url);
                window.scrollTo(0, 0);

                // Re-render LaTeX
                if (window.renderMathInElement) {
                    window.renderMathInElement(document.body);
                }

                // Re-initialize TOC tracking
                initTocTracking();

                console.log('Transition complete');
            });
        })
        .catch(err => {
            console.error('Fetch error:', err);
            window.location.href = url;
        });
}

document.addEventListener('click', e => {
    // Mobile menu toggle
    const toggle = e.target.closest('.menu-toggle');
    if (toggle) {
        const sidebar = document.getElementById('sidebar');
        sidebar.classList.toggle('active');
        return;
    }

    const link = e.target.closest('a');

    // Close sidebar on link click (mobile)
    const sidebar = document.getElementById('sidebar');
    if (sidebar && sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
    }

    if (link &&
        link.origin === window.location.origin &&
        !link.hash &&
        link.getAttribute('target') !== '_blank' &&
        !link.getAttribute('download') &&
        !link.href.includes('mailto:') &&
        !link.href.includes('tel:')) {

        e.preventDefault();
        transitionTo(link.href);
    }
});

window.addEventListener('popstate', () => {
    console.log('Popstate event, reloading');
    location.reload();
});
