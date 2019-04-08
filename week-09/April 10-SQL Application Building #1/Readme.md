### Introduction to MySQL I ###

The following **concepts** has been coverd in this class:
* April-06-2019

* [x] Required Software
  * [-] MySql Database server
  * [-] MySqlWorkBench

* [x] Software operations
    * [-] Instalation steps
        ```
        1 install mysql software
        2 go to system preference and check mysql logo
        3 Click start MySQL server
        ```
    * [-] MySql Workbench
        ```
        1 Open MySql Workbench software 
        2 Connect to local database
        ```
* [x] Database operations
    * [-] How to create database
        ```
        # create database database_name;
        create database animals_db;
        ```
    * [-] How to check all database names
        ```
        # show databases command shows all datbase names
        show databases;
        ```
    * [-] How to select a database to work
        ```
        # use database_name to select the database to work
        use animals_db;
        ```
    * [-] How to create a table in a database
        ```
        # use database_name to select the database to work
        use animals_db;
        
        # use create table query to create a table
        CREATE TABLE people (
            id INT AUTO_INCREMENT NOT NULL,
            name VARCHAR(30) NOT NULL,
            has_pet BOOLEAN DEFAULT false,
            pet_name VARCHAR(30),
            pet_age INT,
            PRIMARY KEY (id)
        );
        ```
    * [-] How to insert data into a table
        ```
        # use insert table query to insert data
        INSERT INTO people (name, has_pet, pet_name, pet_age)
        VALUES ("Jacob", true, "Misty", 10);
        ```
    * [-] How to update data into a table
        ```        
        # use insert table query to insert data
        UPDATE people
        SET has_pet = true
        WHERE name = "Peter";
        ```
    * [-] How to see the data from a table
        ```
        # select query help you to read the data from table
        SELECT * FROM people;
        ```
    * [-] How to add primary key
        ```
        # user primary key in create table
        CREATE TABLE programming_languages (
            id INT AUTO_INCREMENT NOT NULL,
            languages VARCHAR(30) NOT NULL,
            rating INT,
            PRIMARY KEY (id)
        );
        ```
    * [-] Inner Join examples
        ```
        DROP DATABASE IF EXISTS books_db;
        CREATE DATABASE books_db;
        USE books_db;

        CREATE TABLE books(
        id INT AUTO_INCREMENT NOT NULL,
        authorId INT,
        title VARCHAR(100),
        PRIMARY KEY (id)
        );

        CREATE TABLE authors(
        id INT AUTO_INCREMENT NOT NULL,
        firstName VARCHAR(100),
        lastName VARCHAR(100),
        PRIMARY KEY (id)
        );

        INSERT INTO authors (firstName, lastName) values ('Jane', 'Austen');
        INSERT INTO authors (firstName, lastName) values ('Mark', 'Twain');
        INSERT INTO authors (firstName, lastName) values ('Lewis', 'Carroll');
        INSERT INTO authors (firstName, lastName) values ('Andre', 'Asselin');

        INSERT INTO books (title, authorId) values ('Pride and Prejudice', 1);
        INSERT INTO books (title, authorId) values ('Emma', 1);
        INSERT INTO books (title, authorId) values ('The Adventures of Tom Sawyer', 2);
        INSERT INTO books (title, authorId) values ('Adventures of Huckleberry Finn', 2);
        INSERT INTO books (title, authorId) values ('Alice''s Adventures in Wonderland', 3);
        INSERT INTO books (title, authorId) values ('Dracula', null);

        SELECT * FROM authors;
        SELECT * FROM books;

        SELECT title, firstName, lastName
        FROM books
        INNER JOIN authors ON books.authorId = authors.id;

        SELECT title, firstName, lastName
        FROM books
        LEFT JOIN authors ON books.authorId = authors.id;

        SELECT title, firstName, lastName
        FROM books
        RIGHT JOIN authors ON books.authorId = authors.id;
        ```
* [x] Excercise
  * [-] Create database
  * [-] Create table
  * [-] insert data into table
  * [-] update a row to table
  * [-] read the data from the table
  * [-] alter data in table
  * [-] drop the table
  * [-] inner join the table
