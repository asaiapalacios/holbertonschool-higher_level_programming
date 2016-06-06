/*Update age*/
UPDATE Person SET age='27' WHERE first_name='Jon' AND last_name='Snow';
UPDATE Person SET age='18' WHERE first_name='Walter Junior' AND last_name='White';
/*Delete 'Walter White' from Person and EyesColor tables*/
/*Step 1: Delete the foreign key in EyesColor table. Step 2: Delete the record from Person table*/
DELETE FROM EyesColor WHERE person_id = (SELECT id FROM Person WHERE first_name='Walter' AND last_name='White');
DELETE FROM Person WHERE first_name='Walter' AND last_name='White';
/*Display all Person with first_name attributes in ascending order*/
SELECT * FROM Person ORDER BY first_name;
