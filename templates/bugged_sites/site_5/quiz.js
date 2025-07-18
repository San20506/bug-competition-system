
// Learning platform quiz and course functionality
let courses = [];
let userProgress = {};
let currentQuiz = null;

function initializeLearningPlatform() {
    loadCourses();
    loadUserProgress();
    setupEventListeners();
}

function loadCourses() {
    // Simulate loading courses from server
    courses = [
        {
            id: 1,
            title: "JavaScript Fundamentals",
            instructor: "John Smith",
            price: 99,
            rating: 4.5,
            category: "programming",
            description: "Learn the basics of JavaScript programming...",
            image: "js-course.jpg"
        },
        {
            id: 2,
            title: "Web Design Masterclass",
            instructor: "Jane Doe",
            price: 149,
            rating: 4.2,
            category: "design",
            description: "Master modern web design principles...",
            image: "design-course.jpg"
        },
        {
            id: 3,
            title: "Business Strategy",
            instructor: "Mike Johnson",
            price: 79,
            rating: 3.8,
            category: "business",
            description: "Build your business skills...",
            image: "business-course.jpg"
        }
    ];
}

function loadUserProgress() {
    // Load user progress from localStorage or server
    const savedProgress = localStorage.getItem('learningProgress');
    if (savedProgress) {
        userProgress = JSON.parse(savedProgress);
    } else {
        userProgress = {
            enrolledCourses: [],
            completedQuizzes: [],
            totalProgress: 0,
            achievements: []
        };
    }
    
    updateProgressDisplay();
}

function saveUserProgress() {
    localStorage.setItem('learningProgress', JSON.stringify(userProgress));
}

function enrollInCourse(courseId) {
    const course = courses.find(c => c.id === courseId);
    if (!course) {
        showMessage('Course not found', 'error');
        return;
    }
    
    if (userProgress.enrolledCourses.includes(courseId)) {
        showMessage('Already enrolled in this course', 'warning');
        return;
    }
    
    // Simulate enrollment process
    userProgress.enrolledCourses.push(courseId);
    saveUserProgress();
    
    showMessage(`Successfully enrolled in ${course.title}!`, 'success');
    updateProgressDisplay();
}

function searchCourses(query, category) {
    let filteredCourses = courses;
    
    if (query.trim()) {
        filteredCourses = filteredCourses.filter(course =>
            course.title.toLowerCase().includes(query.toLowerCase()) ||
            course.description.toLowerCase().includes(query.toLowerCase()) ||
            course.instructor.toLowerCase().includes(query.toLowerCase())
        );
    }
    
    if (category && category !== '') {
        filteredCourses = filteredCourses.filter(course =>
            course.category === category
        );
    }
    
    displaySearchResults(filteredCourses);
}

function displaySearchResults(courses) {
    const container = document.querySelector('.featured-courses');
    if (!container) return;
    
    // Clear existing courses (keep the heading)
    const heading = container.querySelector('h2');
    container.innerHTML = '';
    if (heading) {
        container.appendChild(heading);
    }
    
    courses.forEach(course => {
        const courseElement = createCourseElement(course);
        container.appendChild(courseElement);
    });
}

function createCourseElement(course) {
    const div = document.createElement('div');
    div.className = 'course-card';
    div.innerHTML = `
        <h3>${course.title}</h3>
        <img src="${course.image}" alt="${course.title}" class="course-image">
        <p class="instructor">Instructor: ${course.instructor}</p>
        <p class="description">${course.description}</p>
        <div class="rating" aria-label="${course.rating} out of 5 stars">
            ${generateStars(course.rating)}
        </div>
        <button type="button" onclick="enrollInCourse(${course.id})">
            Enroll Now - $${course.price}
        </button>
    `;
    
    return div;
}

function generateStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    let stars = '';
    
    for (let i = 0; i < fullStars; i++) {
        stars += '★';
    }
    
    if (hasHalfStar) {
        stars += '☆';
    }
    
    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {
        stars += '☆';
    }
    
    return stars;
}

function startQuiz(quizId) {
    // Quiz questions for demonstration
    const quizQuestions = {
        html: {
            question: "What is HTML?",
            answers: ["Markup Language", "Programming Language", "Database Language"],
            correct: 0
        },
        js: {
            question: "Which is a JavaScript framework?",
            answers: ["React", "HTML", "CSS"],
            correct: 0
        }
    };
    
    currentQuiz = quizQuestions;
    displayQuiz();
}

function displayQuiz() {
    // This would render the quiz questions dynamically
    console.log("Displaying quiz:", currentQuiz);
}

function submitQuiz(formData) {
    if (!currentQuiz) {
        showMessage('No active quiz found', 'error');
        return;
    }
    
    const answers = new FormData(formData);
    let score = 0;
    let total = 0;
    
    // Check answers
    for (let [question, answer] of answers) {
        total++;
        if (currentQuiz[question] && currentQuiz[question].correct === parseInt(answer)) {
            score++;
        }
    }
    
    // Update progress
    const percentage = (score / total) * 100;
    userProgress.completedQuizzes.push({
        timestamp: new Date(),
        score: score,
        total: total,
        percentage: percentage
    });
    
    // Check for achievements
    checkAchievements();
    
    saveUserProgress();
    updateProgressDisplay();
    
    showMessage(`Quiz completed! Score: ${score}/${total} (${percentage}%)`, 'success');
}

function checkAchievements() {
    const achievements = userProgress.achievements || [];
    
    // First quiz completed
    if (userProgress.completedQuizzes.length === 1 && !achievements.includes('first_quiz')) {
        achievements.push('first_quiz');
        showMessage('Achievement unlocked: First Quiz Completed! 🏆', 'achievement');
    }
    
    // 5 courses enrolled
    if (userProgress.enrolledCourses.length >= 5 && !achievements.includes('course_collector')) {
        achievements.push('course_collector');
        showMessage('Achievement unlocked: Course Collector! 📚', 'achievement');
    }
    
    // 10 quizzes passed
    if (userProgress.completedQuizzes.length >= 10 && !achievements.includes('quiz_master')) {
        achievements.push('quiz_master');
        showMessage('Achievement unlocked: Quiz Master! ⭐', 'achievement');
    }
    
    userProgress.achievements = achievements;
}

function updateProgressDisplay() {
    // Update progress bar
    const progressBar = document.querySelector('.progress');
    if (progressBar) {
        const totalCourses = courses.length;
        const enrolledCourses = userProgress.enrolledCourses.length;
        const progressPercentage = (enrolledCourses / totalCourses) * 100;
        
        progressBar.style.width = `${progressPercentage}%`;
        
        const progressText = document.querySelector('.sidebar p');
        if (progressText) {
            progressText.textContent = `Overall Progress: ${Math.round(progressPercentage)}%`;
        }
    }
}

function setupEventListeners() {
    // Search form
    const searchForm = document.querySelector('.search-courses');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = this.querySelector('input[name="query"]').value;
            const category = this.querySelector('select[name="category"]').value;
            searchCourses(query, category);
        });
    }
    
    // Quiz form
    const quizForm = document.querySelector('.quiz-form');
    if (quizForm) {
        quizForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitQuiz(this);
        });
    }
    
    // Newsletter form
    const newsletterForm = document.querySelector('.newsletter');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = this.querySelector('input[type="email"]').value;
            subscribeToNewsletter(email);
        });
    }
}

function subscribeToNewsletter(email) {
    if (!email || !validateEmail(email)) {
        showMessage('Please enter a valid email address', 'error');
        return;
    }
    
    // Simulate newsletter subscription
    setTimeout(() => {
        showMessage('Successfully subscribed to learning tips newsletter!', 'success');
    }, 1000);
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showMessage(message, type) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Style the notification
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '1rem 2rem',
        borderRadius: '10px',
        color: 'white',
        fontWeight: 'bold',
        zIndex: '10000',
        transition: 'all 0.3s ease'
    });
    
    // Set background color based on type
    switch (type) {
        case 'success':
            notification.style.background = '#28a745';
            break;
        case 'error':
            notification.style.background = '#dc3545';
            break;
        case 'warning':
            notification.style.background = '#ffc107';
            notification.style.color = '#333';
            break;
        case 'achievement':
            notification.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
            break;
        default:
            notification.style.background = '#6c757d';
    }
    
    document.body.appendChild(notification);
    
    // Remove notification after 4 seconds
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 4000);
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', initializeLearningPlatform);

// Global functions for inline event handlers (these are the bugs)
function enrollCourse(courseId) {
    enrollInCourse(courseId);
}
