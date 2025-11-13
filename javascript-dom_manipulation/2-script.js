const redHeaderButton = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeaderButton.addEventListener('click', function() {
  header.classList.add('red');
});
