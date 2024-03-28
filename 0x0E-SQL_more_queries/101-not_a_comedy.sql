-- A SCriot that lists all Shows without the genre Comedy in the database
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT s.title AS title
FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS t
	ON s.id = t.show_id

	LEFT JOIN tv_genres AS g
	On t.genre_id = g.id
	WHERE s.title NOT IN
		(SELECT title
			FROM tv_shows AS t
			INNER JOIN tv_show_genres AS s
			ON s.show_id = t.id

			INNER JOIN tv_genres AS g
			ON g.id = s.genre_id
			WHERE g.name = "Comedy")
ORDER BY title ASC;
