const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, textStatus) {
  for (let i = 0; i < data.results.length; i++) {
    const title = data.results[i].title;
    $('UL#list_movies').append(`<li>${title}</li>`);
  }
});
