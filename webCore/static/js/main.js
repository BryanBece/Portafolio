document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('.typing-effect');
    elements.forEach((element) => {
        const text = element.innerText;
        element.innerHTML = '';
        let index = 0;

        function type() {
            if (index < text.length) {
                element.innerHTML += text.charAt(index);
                index++;
                setTimeout(type, 100); // Ajusta la velocidad de escritura aquí
            }
        }
        type();
    });
});