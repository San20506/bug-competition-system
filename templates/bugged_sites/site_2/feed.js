
// Social media feed functionality
let posts = [];
let likes = {};

function loadFeed() {
    // Simulate loading posts from server
    posts = [
        { id: 1, user: "John Doe", content: "Great day!", likes: 5 },
        { id: 2, user: "Jane Smith", content: "Cool website!", likes: 12 }
    ];
    
    renderFeed();
}

function renderFeed() {
    const feedContainer = document.querySelector('.feed');
    if (!feedContainer) return;
    
    posts.forEach(post => {
        // This function would render each post
        console.log("Rendering post:", post.id);
    });
}

function toggleLike(postId) {
    if (!likes[postId]) {
        likes[postId] = 0;
    }
    likes[postId]++;
    
    // Update UI
    updateLikeDisplay(postId);
}

function updateLikeDisplay(postId) {
    const likeElement = document.getElementById(`like-count-${postId}`);
    if (likeElement) {
        likeElement.textContent = likes[postId];
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', loadFeed);
