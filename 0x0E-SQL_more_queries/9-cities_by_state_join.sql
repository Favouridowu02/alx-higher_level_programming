-- A Script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON `state`.`id` = `cities`.`state_id`
ORDER BY cities.id ASC;
