INSERT INTO EyesColor VALUES ((SELECT id FROM Person WHERE first_name = 'Jon' AND last_name = 'Snow'), 'Brown');
/*Add eye color to Jon Snow and Arya Stark*/
INSERT INTO EyesColor VALUES ((SELECT id FROM Person WHERE first_name = 'Arya' AND last_name = 'Stark'), 'Green');

/*Create new tables*/
CREATE TABLE TVShow (
       id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
       NAME char(128) NOT NULL);
CREATE TABLE TVShowPerson (
       tvshow_id INTEGER NOT NULL,
       person_id INTEGER NOT NULL,
       FOREIGN KEY(tvshow_id) REFERENCES TVShow(id), 
       FOREIGN KEY (person_id) REFERENCES Person(id)
);

/*Add in TVShow*/
INSERT INTO TVShow (Name) VALUES
       ('Homeland'),
       ('The big bang theory'),
       ('Game of Thrones'),
       ('Breaking bad');

/*Add all TVShow link to Person in TVShowPerson*/
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES
       ( (SELECT id FROM TVShow WHERE NAME = 'Breaking bad'), (SELECT id FROM Person WHERE first_name = 'Walter Junior' AND last_name = 'White') ),
       ( (SELECT id FROM TVShow WHERE NAME = 'Game of Thrones'), (SELECT id FROM Person WHERE first_name = 'Jaime' AND last_name = 'Lannister') ),
       ( (SELECT id FROM TVShow WHERE NAME = 'The big bang theory'), (SELECT id FROM Person WHERE first_name = 'Sheldon' AND last_name = 'Cooper') ),
       ( (SELECT id FROM TVShow WHERE NAME = 'Game of Thrones'), (SELECT id FROM Person WHERE first_name = 'Tyrion' AND last_name = 'Lannister') ),
       ( (SELECT id FROM TVShow WHERE NAME = 'Game of Thrones'), (SELECT id FROM Person WHERE first_name = 'Jon' AND last_name = 'Snow') ),
       ( (SELECT id FROM TVShow WHERE NAME = 'Game of Thrones'), (SELECT id FROM Person WHERE first_name = 'Arya' AND last_name = 'Stark') );

/*Display all records with all attributes of all tables */
SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;