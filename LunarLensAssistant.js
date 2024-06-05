<script src="https://telegram.org/js/telegram-web-app.js"></script>

// Initialize the Telegram Web App
Telegram.WebApp.init({
  // Your Telegram Web App ID
  id: 'LLA',
  // Your Telegram Web App bot token
  bot_token: '7480253592:AAFFwrQ_IPLj1jbBoVssE2jnE9POUenrSNA',
  // The URL of your Python backend
  backend_url: 'https://github.com/summerbird77/ARESIV-Bot/blob/main/lunarlensAssistant.py',
});

// Handle the OAuth verification link click
document.addEventListener('DOMContentLoaded', function () {
  const verifyLink = document.getElementById('verify-link');
  verifyLink.addEventListener('click', function (event) {
    event.preventDefault();
    // Send a request to your Python backend to initiate the OAuth flow
    fetch(`${Telegram.WebApp.backend_url}/oauth/init`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        // Pass the Telegram user ID and chat ID to your Python backend
        user_id: Telegram.WebApp.getUser().id,
        chat_id: Telegram.WebApp.getChat().id,
      }),
    })
   .then(response => response.json())
   .then(data => {
      // Open the OAuth verification link in a new tab
      window.open(data.verification_url, '_blank');
    })
   .catch(error => console.error(error));
  });
});