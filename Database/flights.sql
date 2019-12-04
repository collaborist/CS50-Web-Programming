/* 
Команда в psql для смены кодировки:
    psql \! chcp 1251
Просмотр всех сущностей в таблице
    psql \d

*/

CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);


INSERT INTO flights
(origin, destination, duration)
VALUES ('New York', 'London', 415);


UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    AND destination = 'London';

DELETE FROM flights
    WHERE destination = 'Tokyo';

SELECT * FROM flights limit = 2;