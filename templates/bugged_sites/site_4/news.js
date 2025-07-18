
// News website functionality
let articles = [];
let currentCategory = 'all';

function loadNews() {
    // Simulate loading news articles
    articles = [
        {
            id: 1,
            title: "Technology Breakthrough",
            category: "tech",
            date: "2024-01-15",
            summary: "Scientists make major discovery...",
            image: "tech-news.jpg"
        },
        {
            id: 2,
            title: "Economic Updates",
            category: "economy",
            date: "2024-01-14",
            summary: "Stock market shows positive trends...",
            image: "economy.jpg"
        },
        {
            id: 3,
            title: "Sports Championship",
            category: "sports",
            date: "2024-01-13",
            summary: "Local team wins championship...",
            image: "sports.jpg"
        }
    ];
    
    renderNews();
}

function renderNews() {
    const newsContainer = document.querySelector('.news-grid');
    if (!newsContainer) return;
    
    const filteredArticles = currentCategory === 'all' 
        ? articles 
        : articles.filter(article => article.category === currentCategory);
    
    newsContainer.innerHTML = '';
    
    filteredArticles.forEach(article => {
        const articleElement = createArticleElement(article);
        newsContainer.appendChild(articleElement);
    });
}

function createArticleElement(article) {
    const div = document.createElement('div');
    div.className = 'news-item';
    div.innerHTML = `
        <h3>${article.title}</h3>
        <img src="${article.image}" alt="${article.title}" class="thumbnail">
        <p>${article.summary}</p>
        <p class="date">${formatDate(article.date)}</p>
        <a href="/article/${article.id}">Read more</a>
    `;
    
    return div;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function filterNews(category) {
    currentCategory = category;
    renderNews();
    
    // Update active category in navigation
    document.querySelectorAll('nav a').forEach(link => {
        link.classList.remove('active');
    });
    
    const activeLink = document.querySelector(`nav a[data-category="${category}"]`);
    if (activeLink) {
        activeLink.classList.add('active');
    }
}

function searchNews(query) {
    if (!query.trim()) {
        renderNews();
        return;
    }
    
    const searchResults = articles.filter(article => 
        article.title.toLowerCase().includes(query.toLowerCase()) ||
        article.summary.toLowerCase().includes(query.toLowerCase())
    );
    
    displaySearchResults(searchResults, query);
}

function displaySearchResults(results, query) {
    const newsContainer = document.querySelector('.news-grid');
    if (!newsContainer) return;
    
    newsContainer.innerHTML = `<h4>Search results for "${query}" (${results.length} found)</h4>`;
    
    results.forEach(article => {
        const articleElement = createArticleElement(article);
        newsContainer.appendChild(articleElement);
    });
}

function trackClick(element, category) {
    // Analytics tracking
    console.log(`Clicked: ${element} in category: ${category}`);
    
    // Send to analytics service
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            'event_category': category,
            'event_label': element
        });
    }
}

function subscribeNewsletter(email) {
    if (!email || !validateEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }
    
    // Simulate newsletter subscription
    setTimeout(() => {
        showMessage('Successfully subscribed to newsletter!', 'success');
    }, 1000);
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showMessage(message, type) {
    // Create and show notification
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    loadNews();
    
    // Set up search form
    const searchForm = document.querySelector('.search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = this.querySelector('input').value;
            searchNews(query);
        });
    }
    
    // Set up newsletter form
    const newsletterForm = document.querySelector('.newsletter');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            subscribeNewsletter(email);
        });
    }
});
