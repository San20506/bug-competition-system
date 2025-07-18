
// Banking security and functionality
let currentSession = {
    userId: null,
    accountNumber: null,
    sessionToken: null,
    loginTime: null
};

function initializeBanking() {
    // Check if user is logged in
    if (sessionStorage.getItem('bankingSession')) {
        currentSession = JSON.parse(sessionStorage.getItem('bankingSession'));
        displayAccountInfo();
    }
}

function login(username, password) {
    // Simulate login process
    if (username && password) {
        currentSession = {
            userId: 'user_' + Math.random().toString(36).substr(2, 9),
            accountNumber: '123456789',
            sessionToken: 'token_' + Math.random().toString(36).substr(2, 16),
            loginTime: new Date()
        };
        
        // Store session
        sessionStorage.setItem('bankingSession', JSON.stringify(currentSession));
        
        // Redirect to dashboard
        window.location.href = '/dashboard';
    }
}

function displayAccountInfo() {
    const balanceElement = document.getElementById('balance');
    if (balanceElement && currentSession.accountNumber) {
        // Simulate fetching balance
        fetchAccountBalance(currentSession.accountNumber);
    }
}

function fetchAccountBalance(accountNumber) {
    // Simulate API call
    setTimeout(() => {
        const balance = '$2,500.00';
        document.getElementById('balance').textContent = balance;
    }, 1000);
}

function transferMoney(recipient, amount) {
    if (!currentSession.sessionToken) {
        alert('Please log in first');
        return;
    }
    
    // Validate transfer
    if (validateTransfer(recipient, amount)) {
        // Process transfer
        processTransfer(recipient, amount);
    }
}

function validateTransfer(recipient, amount) {
    if (!recipient || !amount) {
        showError('Please fill in all fields');
        return false;
    }
    
    if (amount <= 0) {
        showError('Amount must be greater than 0');
        return false;
    }
    
    return true;
}

function processTransfer(recipient, amount) {
    // Simulate transfer processing
    console.log(`Transferring $${amount} to ${recipient}`);
    alert('Transfer completed successfully!');
}

function showError(message) {
    const errorDiv = document.getElementById('error-messages');
    if (errorDiv) {
        errorDiv.innerHTML = `<p style="color: red;">${message}</p>`;
    }
}

function logout() {
    // Clear session
    sessionStorage.removeItem('bankingSession');
    currentSession = {};
    
    // Redirect to login
    window.location.href = '/login';
}

// Auto-logout after 30 minutes of inactivity
let inactivityTimer;

function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(logout, 30 * 60 * 1000); // 30 minutes
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeBanking();
    
    // Set up inactivity monitoring
    document.addEventListener('mousedown', resetInactivityTimer);
    document.addEventListener('mousemove', resetInactivityTimer);
    document.addEventListener('keypress', resetInactivityTimer);
    document.addEventListener('scroll', resetInactivityTimer);
    document.addEventListener('touchstart', resetInactivityTimer);
    
    resetInactivityTimer();
});
