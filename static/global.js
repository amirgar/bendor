// Функция для плавной прокрутки до элемента
function smoothScrollTo(targetId) {
  const targetElement = document.getElementById(targetId);
  if (targetElement) {
    targetElement.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  }
}

// Обработчик события для кнопки PRICELIST
document.addEventListener('DOMContentLoaded', function() {
  const pricelistButton = document.querySelector('.pricelist-button');
  if (pricelistButton) {
    pricelistButton.addEventListener('click', function(e) {
      // Предотвращаем стандартное поведение ссылки
      e.preventDefault();
      
      // Получаем ID целевого элемента из href ссылки
      const targetId = this.getAttribute('href').substring(1);
      
      // Выполняем плавную прокрутку
      smoothScrollTo(targetId);
    });
  }
});