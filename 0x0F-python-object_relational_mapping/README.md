0x0F. Python - Object-relational mapping

Background
This project focuses on linking MySQL databases and Python code using the MySQLdb and SQLAlchemy libraries.

The first part involves executing SQL queries directly using MySQLdb. The second part involves using SQLAlchemy's ORM to map Python classes to MySQL tables.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
You will need to following installed:

 - Python 3.8
 - MySQLdb 2.0.x
 - SQLAlchemy 1.4.x
 - MySQL Server

Installing
  1. Install and set up MySQL Server
  2. Create and activate a virtual environment:
$ python3 -m venv venv 
$ source venv/bin/activate
 
  3. Install dependencies:
$ pip install mysqlclient
$ pip install SQLAlchemy

  4. Test connections and library versions:
import MySQLdb
import sqlalchemy

Usage
  - Review tutorials and documentation for SQLAlchemy and MySQLdb
  - Connect to MySQL database and run queries using MySQLdb directly
  - Map Python classes to MySQL tables using SQLAlchemy ORM
  - Follow code documentation and style guidelines

Acknowledgments
  - SQLAlchemy documentation
  - MySQLdb documentation
