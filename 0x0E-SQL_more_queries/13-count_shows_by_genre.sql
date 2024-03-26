-- A Script that lists all genres from the database
SELECT t.name AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM tv_genres AS t
	INNER JOIN `tv_show_genres` AS n
	ON t.id = n.`genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows` DESC;
