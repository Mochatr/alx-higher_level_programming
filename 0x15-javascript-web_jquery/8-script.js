$(document).ready(function() {
        $.ajax({
		url: 'http://swapi-api.alx-tools.com/api/people/5/?format=json',
		method: 'GET'
		success: function(data) {
			var movies = data.results;
			var movieList = $('#list_movies');
			movies.foreach(function(movie) {
				movieList.append('<li>' + movie.title + '</li>');
			});
		},
		error: function(error) {
			console.error('Error fetching movie data:', error);
		}
        });
});
