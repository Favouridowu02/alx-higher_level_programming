-- A Script that lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE `state`.`id` = `cities`.`state_id`
ORDER BY cities.id ASC;
