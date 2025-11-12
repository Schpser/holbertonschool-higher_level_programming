const redHeaderButton = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeaderButton.addEventListener('click', function() {
  header.style.color = '#FF0000';
});
