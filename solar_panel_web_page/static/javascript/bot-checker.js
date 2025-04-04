let captchaAttempts = 0;
let currentCaptcha = '';

function isBot(event) {
    event.preventDefault();
    const form = document.querySelector('form');

    // Проверяваме дали формата е валидна
    if (!form.checkValidity()) {
        form.reportValidity(); // Показва кои полета липсват
        return false;
    }
    generateCaptcha();
    showModal();
    return false;
}

function generateCaptcha() {
    currentCaptcha = '';
    for (let i = 0; i < 4; i++) {
        currentCaptcha += Math.floor(Math.random() * 10).toString();
    }
    document.getElementById('captchaPrompt').innerText = `Моля, въведете следния код: ${currentCaptcha}`;
    document.getElementById('captchaInput').value = '';
}

function showModal() {
    const modal = document.getElementById('captchaModal');
    const content = modal.querySelector('.modal-content');

    modal.style.display = 'flex';
    modal.style.height = '500px';
    content.style.background = '#363535';
    modal.style.color = 'whitesmoke';
    content.style.borderRadius = '12px';
    content.style.boxShadow = '0 8px 24px rgba(0,0,0,0.15)';
    content.style.transition = 'all 0.3s ease';
    content.style.border = '1px solid #eee';

    content.style.transform = 'translateY(30px)';
    content.style.opacity = '0';
    setTimeout(() => {
        content.style.transform = 'translateY(0)';
        content.style.opacity = '1';
    }, 10);

    const input = content.querySelector('#captchaInput');
    input.style.borderRadius = '8px';
    input.style.border = '1px solid #ccc';
    input.style.padding = '0.6rem';
    input.style.fontSize = '1rem';
    input.style.width = '100%';

    // Бутон стил
    const btn = content.querySelector('button');
    btn.style.backgroundColor = '#444';
    btn.style.color = '#fff';
    btn.style.border = 'none';
    btn.style.borderRadius = '8px';
    btn.style.padding = '0.6rem 1rem';
    btn.style.cursor = 'pointer';
    btn.style.marginTop = '10px';
    btn.onmouseenter = () => btn.style.backgroundColor = '#222';
    btn.onmouseleave = () => btn.style.backgroundColor = '#444';
}

function hideModal() {
    document.getElementById('captchaModal').style.display = 'none';
}

function submitCaptcha() {
    const userInput = document.getElementById('captchaInput').value.trim();
    if (userInput === currentCaptcha) {
        hideModal();
        document.querySelector('form').submit();
    } else {
        captchaAttempts++;
        if (captchaAttempts < 3) {
            generateCaptcha(); // нов опит
        } else {
            window.location.href = '/'; // пренасочване към началната
        }
    }
}
