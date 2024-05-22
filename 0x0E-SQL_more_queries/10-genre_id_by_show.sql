-- list all shows contained in tvshows that at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show.id = tv_show_genres.tv_show_id
ORDER BY tv_show.titele ASC, tv_show_genres.genre_id ASC;
