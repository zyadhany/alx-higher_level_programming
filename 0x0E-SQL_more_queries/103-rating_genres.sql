-- Get all DB of server.

SELECT name, SUM(tv_show_ratings.rate) 'rating' FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY name
ORDER BY rating DESC;
