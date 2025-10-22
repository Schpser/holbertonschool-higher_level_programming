-- LIST TV SHOWS FROM A DATABASE;
SELECT 
    tv_shows.title,
    tv_show_genres.genre_id

FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
