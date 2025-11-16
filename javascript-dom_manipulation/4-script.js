const addButton = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addButton.addEventListener('click', function() {
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  myList.appendChild(newElement);
});