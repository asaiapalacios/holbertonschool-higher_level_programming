/*Insert records in a table to add and update values*/
INSERT INTO Person (first_name, last_name, age) VALUES ('Jon', 'Snow', '26');
INSERT INTO Person (first_name, last_name, age) VALUES ('Arya', 'Stark', '12');
/*Display all last_name attributes of Person table in this order (A->Z)*/
SELECT * FROM Person ORDER BY last_name; /*Note: Ascending order by default*/
