-- Cleaning up from previous run
-- -----------------------------------------------------
DROP DATABASE IF EXISTS hebo_week_9;

DROP USER IF EXISTS hebo_user@localhost;
-- -----------------------------------------------------



-- Creating and using database
-- -----------------------------------------------------
CREATE DATABASE hebo_week_9;
USE hebo_week_9;
-- -----------------------------------------------------



-- Creating tables
-- -----------------------------------------------------
CREATE TABLE Cereal(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    mfr varchar(1),
    type varchar(1),
    calories int,
    protein int,
    fat int,
    sodium int,
    fiber float,
    carbo float,
    sugars int,
    potass int,
    vitamins int,
    shelf int,
    weight float,
    cups float,
    rating float,
    PRIMARY KEY (ID)
);

CREATE TABLE user(
    name varchar(64) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (name)
);
-- -----------------------------------------------------



-- Creating procedures --
-- -----------------------------------------------------
DELIMITER //
CREATE PROCEDURE add_cereal (
	IN c_name varchar(255),
    In c_mfr varchar(1),
	IN c_type varchar(1),
    IN c_calories int,
    IN c_protein int,
    IN c_fat int,
    IN c_sodium int,
    IN c_fiber float,
    IN c_carbo float,
    IN c_sugars int,
    IN c_potass int,
    IN c_vitamins int,
    IN c_shelf int,
    IN c_weight float,
    IN c_cups float,
    IN c_rating float
)
BEGIN
	INSERT INTO Cereal
    (name, mfr, type, calories, protein, fat, sodium, fiber, carbo, sugars, potass, vitamins, shelf, weight, cups, rating)
    VALUES(c_name, c_mfr, c_type, c_calories, c_protein, c_fat, c_sodium, c_fiber, c_carbo, c_sugars, c_potass, c_vitamins, c_shelf, c_weight, c_cups, c_rating);
	SELECT LAST_INSERT_ID() as cereal_id;
END//
DELIMITER ;
-- -----------------------------------------------------



-- Create user
-- -----------------------------------------------------
CREATE USER 'hebo_user'@'localhost' IDENTIFIED BY 'test123';
GRANT SELECT, INSERT, UPDATE, DELETE ON hebo_week_9.Cereal TO 'hebo_user'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON hebo_week_9.user TO 'hebo_user'@'localhost';
GRANT EXECUTE ON PROCEDURE hebo_week_9.add_cereal TO 'hebo_user'@'localhost';
-- -----------------------------------------------------



-- Populating tables
-- -----------------------------------------------------
-- INSERT INTO Category (name, description) VALUES ('Miscellaneous', 'For everything not in other categories');
INSERT INTO user (name, password) VALUES('hebo_user', 'test123');
