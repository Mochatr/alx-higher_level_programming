# Introduction to SQL

[!Image](https://cdn.prod.website-files.com/61ddd0b42c51f89b7de1e910/6697e5d70e6b50dbe5bbe3dd_6697e36f9a2e61c3f9a3c850_SQL.jpeg)

## Resources
### Read or watch:

[What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
[A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
[What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
[MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
[installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

## Learning Objectives
### General
What’s a database ?
What’s a relational database ? 
What does SQL stand for ?
What’s MySQL ? 
How to create a database in MySQL ?
What does DDL and DML stand for ?
How to CREATE or ALTER a table 
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries ?
How to use MySQL functions ?

### Tasks

0. List databases

0-list_databases.sql: Lists all databases of your MySQL server.

1. Create a database

1-create_database_if_missing.sql: Creates the database hbtn_0c_0 in your MySQL server.
If the database hbtn_0c_0 already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

2. Delete a database

2-remove_database.sql: Deletes the database hbtn_0c_0 in your MySQL server.
If the database hbtn_0c_0 already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

3. List tables

3-list_tables.sql: Lists all the tables of a database in your MySQL server.

4. First table

4-first_table.sql: Creates a table called first_table in the current database in your MySQL server.
first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command.
If the table first_table already exists, your script should not fail.
You are not allowed to use the SELECT or SHOW statements.

5. Full description

5-full_table.sql: Prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
You are not allowed to use the DESCRIBE or EXPLAIN statements.
