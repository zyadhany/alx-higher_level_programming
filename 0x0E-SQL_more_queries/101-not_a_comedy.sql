-- Get all DB of server.

SELECT title FROM tv_shows WHERE title NOT IN (
SELECT title FROM tv_shows
LEFT JOIN a ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN b ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy')
GROUP BY title
ORDER BY title ASC;
