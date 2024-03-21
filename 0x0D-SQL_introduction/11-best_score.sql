-- A Script that lists all records with a score >= 10 in the table second_table
SELECT scores, name FROM `second_table`
ORDER BY scores DESC
where score >= 10;
