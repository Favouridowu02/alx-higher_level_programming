-- A Script that uses the database to list all genres of the show Dexter
SELECT t.name FROM tv_genres AS t
INNER JOIN tv_show_genres AS s
ON t.id = s.genre_id
INNER JOIN tv_shows AS k
ON k.id = s.show_id
WHERE k.title = "Dexter"
ORDER BY t.name ASC;
