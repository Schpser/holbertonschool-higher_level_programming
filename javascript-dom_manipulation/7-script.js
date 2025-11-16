fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.querySelector('#list_movies');
  
    data.results.forEach(movie => {
      const newElement = document.createElement('li');
      newElement.textContent = movie.title;
      listMovies.appendChild(newElement);
    });
  });