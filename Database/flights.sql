/* 
Команда в psql для смены кодировки:
    psql \! chcp 1251
Просмотр всех сущностей в таблице
    psql \d

set DATABASE_URL = URI of my db
set FLASK_DEBUG = 1  // run debug mode
set FLASK_APP=application.py


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




CREATE TABLE users (
    id SERIAL not null,
    name VARCHAR PRIMARY KEY,
    password VARCHAR NOT NULL
);

INSERT INTO users
(id, name, password)
VALUES (1, 'Rustam', 'rerifet12');

INSERT INTO users
(id, name, password)
VALUES (2, 'Rasul', '110119931');


SELECT * from users
where users.name = 'Rustam1';


INSERT INTO users (name, password) VALUES ('qwerty5', 'qwerty5');