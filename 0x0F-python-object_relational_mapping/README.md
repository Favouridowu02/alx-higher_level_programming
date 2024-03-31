# Object Relational mapping

# Project Setup Guide

This guide will walk you through setting up a Python virtual environment and installing necessary dependencies for your project.

## Installing mysql client and server
    ```
    $ sudo apt-get install mysql-server mysql-client
    ```

## Installing and Activating Virtual Environment

To create a Python Virtual Environment, allowing you to install specific dependencies for this Python project, follow these steps:

1. Install `venv`:
    ```
    $ sudo apt-get install python3.8-venv
    ```

2. Create the virtual environment:
    ```
    $ python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```
    $ source venv/bin/activate
    ```

## Installing MySQLdb Module (Version 2.0.x)

Before installing MySQLdb, ensure MySQL is installed. You can follow [these instructions](#how-to-install-mysql-80-in-ubuntu-2004) to install MySQL 8.0 on Ubuntu 20.04.

1. Install necessary dependencies:
    ```
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    ```

2. Install MySQLdb:
    ```
    $ sudo pip3 install mysqlclient
    ```

3. Verify the installation:
    ```
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info
    (2, 0, 3, 'final', 0)
    ```

## Installing SQLAlchemy Module (Version 1.4.x)

1. Install SQLAlchemy:
    ```
    $ sudo pip3 install SQLAlchemy
    ```

2. Verify the installation:
    ```
    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__
    '1.4.22'
    ```

## How to Install MySQL 8.0 in Ubuntu 20.04

[This section should provide detailed instructions on how to install MySQL 8.0 on Ubuntu 20.04. It should include any necessary steps such as adding repositories, installing the MySQL server, and setting up a root password.]
