-- DISPLAY GENRES AND NUMBER OF TV SHOWS RELATED TO THEM;
SELECT 
    tv_genres.name AS genre,
    COUNT(*) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
