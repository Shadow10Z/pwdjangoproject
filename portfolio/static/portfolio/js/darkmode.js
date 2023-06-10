const toggleBtn = document.getElementById('label-togg');
const content = document.querySelector('.test5');
const content2 = document.querySelector('.backgroundMenu');
const content3 = document.querySelector('.navegation');
const content4 = document.querySelector('.test8');
const content5 = document.querySelector('.test7');

toggleBtn.addEventListener('click', () => {
  content.classList.toggle('dark-mode');
  content2.classList.toggle('dark-mode');
  content3.classList.toggle('dark-mode');
  content4.classList.toggle('dark-mode');
  content5.classList.toggle('dark-mode');

  // Salva o modo atual no localStorage
  localStorage.setItem('dark-mode', content.classList.contains('dark-mode'));
  localStorage.setItem('dark-mode', content2.classList.contains('dark-mode'));
  localStorage.setItem('dark-mode', content3.classList.contains('dark-mode'));
  localStorage.setItem('dark-mode', content4.classList.contains('dark-mode'));
  localStorage.setItem('dark-mode', content5.classList.contains('dark-mode'));
});

// Configura o modo inicial
const isDarkMode = localStorage.getItem('dark-mode') === 'true';
if (isDarkMode) {
  content.classList.add('dark-mode');
  content2.classList.add('dark-mode');
  content3.classList.add('dark-mode');
  content4.classList.add('dark-mode');
  content5.classList.add('dark-mode');
}