$(document).ready(function() {
    $.ajax({
      url: "https://swapi-api.alx-tools.com/api/films/?format=json",
      success: function(data) {
        var movies = data.results; // Get movie data
        for (var i = 0; i < movies.length; i++) {
          $("#list_movies").append("<li>" + movies[i].title + "</li>");
        }
      }
    });
  });
  