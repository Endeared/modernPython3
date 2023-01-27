-- CREATE TABLE dogs (
--     name TEXT,
--     breed TEXT,
--     age INTEGER
-- );

INSERT INTO dogs (name, age, breed) VALUES ("Toby", 11, "Shepherd-Beagle");
INSERT INTO dogs (name, age, breed) VALUES ("Zipper", 14, "Golden Retriever");
INSERT INTO dogs (name, age, breed) VALUES ("Shadow", 16, "Labrador");
INSERT INTO dogs (name, age, breed) VALUES ("Elvis", 11, "Yorkie");


CREATE TABLE temp_table as SELECT DISTINCT * FROM dogs;
DELETE FROM dogs;
INSERT INTO dogs SELECT * FROM temp_table