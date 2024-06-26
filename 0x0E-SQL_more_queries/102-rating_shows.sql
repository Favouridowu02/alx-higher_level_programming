-- A Script that lists all shows from the database
-- Display tv_shows.title and rating sum

SELECT title, SUM(rate) AS "rating"
FROM tv_shows AS t
INNER JOIN tv_show_ratings AS r
ON t.id = r.show_id
GROUP BY title
ORDER BY rating DESC;
