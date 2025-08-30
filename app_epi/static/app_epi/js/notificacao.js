function notificacao(type, message) {
    const container = document.getElementById('notificacao_system');

    const notification = document.createElement('div');
    notification.className = `notification ${type}`;

    // Criação do botão de fechar
    const closeBtn = document.createElement('button');
    closeBtn.className = 'close-btn';
    closeBtn.innerHTML = '&times;';
    closeBtn.onclick = () => {
        notification.classList.add('slide-out');
        setTimeout(() => {
            notification.remove();
        }, 300); // Tempo da animação (match com CSS)
    };

    notification.innerHTML = message;
    notification.appendChild(closeBtn);

    container.appendChild(notification);

    // Remoção automática após 5 segundos
    setTimeout(() => {
        if (notification.parentElement) {
            notification.classList.add('slide-out');
            setTimeout(() => {
                notification.remove();
            }, 300);
        }
    }, 5000);

    if (message === "Usuario não logado") {
        window.location.href = '/sistema/public/'; // Redireciona para página de login
    }
}