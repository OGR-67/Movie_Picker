# Movie Picker Project

## Description

### Idea

The project aims to create a movie picker that helps you decide what movie to watch. In an era where algorithms often dictate our choices, this simple application allows you to make a decision based on movie tags and ratings.

### Key Goals and Learning Objectives

This project provides me with the opportunity to explore several domains and learn more about:

- Python and its ecosystem
- Flask
- Hexagonal Architecture
- Tests Driven Development (TDD)
- "given when then" tests structure

### Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy (migrations)
- pytest
- pytest-watch
- mypy
- flake8
- templating: Jinja2

### Choices explanation

#### Raw SQL for migrations

While using an ORM's schema concept for migration generation can speed up development and maintain consistency between the expected model in code and the database table, some decisions made by ORMs are obscured from us. This can occasionally lead to issues when modifying schemas later on. For instance, when a field is defined with a uniqueness constraint, certain ORMs append a timestamp to identify this constraint, complicating the removal of this constraint in a production setting (since the timestamp will differ from the development environment). This is a primary reason, but also because switching to another database management system, especially if it's not supported by the chosen ORM, becomes simpler, that I've decided to write queries in separate SQL files for migrations.

#### Raw SQL for queries in repositories implémentations

In addition to the reasons mentioned earlier, I've chosen to use raw SQL for queries within repository implementations to deepen my understanding of SQL and to craft more efficient queries.

#### Hexagonal Architecture

Hexagonal Architecture is a software architecture pattern that allows us to decouple the core logic of our application from the external dependencies. This is achieved by defining ports and adapters. Ports are interfaces that define the core logic of our application. Adapters are implementations of these interfaces that depend on external dependencies. This allows us to easily swap out implementations of these interfaces without having to modify the core logic of our application. This is especially useful when writing tests, as we can easily mock the dependencies of our application.
This project is my first application using this architecture. I've chosen to use it to deepen my understanding of this pattern and to learn how to implement tests using this architecture.

#### Tests Driven Development (TDD)

TDD is a software development process that relies on the repetition of a very short development cycle: first the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards. This project is my first application using this process. I've chosen to use it to deepen my understanding of this process and to learn how to implement tests using this process.

#### "given when then" tests structure

This project is my first application using this structure. I've chosen to use it to deepen my understanding of this structure and to learn how to implement tests using this structure.

#### mypy

To implement the hexagonal architecture in Python in a strongly-typed manner, I've found `mypy` to be the most effective solution. I chose to use it both to enhance my understanding of the tool and to gain experience integrating it into a project.

## Installation

### Requirements

- install python >= 3.11
- create a virtual environment
- activate the virtual environment
- install dependencies with `pip install -r requirements.txt`

### Optional

#### MyPy

mypy is used for type checking

mypy deamon can be used in association with vscode to check for errors while coding using [this](https://marketplace.visualstudio.com/items?itemName=matangover.mypy) extension

- run `export PROJECT_DIR=$(pwd)`
- run `dmypy run` to run mypy daemon

## Set up database

- be sure to have the virtual environment activated
- run `touch instance/movies_db.db`
- run `flask db upgrade`

### Create migration

- be sure to have the virtual environment activated
- run `flask db revision -m "message"` to create a migration

To apply migrations run `flask db upgrade`
To revert last migration run `flask db downgrade`

### Feed database

- be sure to have the virtual environment activated
- run `python feed_db.py` to feed the database with movies

## How to run

- be sure to have the virtual environment activated
- run `python app.py` to run in develpment mode

## How to run tests

- be sure to have the virtual environment activated
- run `export PYTHONPATH=.` when on root directory of the project
- run `pytest` to run all tests
- run `ptw` to run all tests in watch mode

## Features

Users:

- [X] create user / register
- [X] login
- [X] logout
- [X] delete user - depends on: profile page
- [X] profile page with user's favorites and watchlist and account deletion - depends on: Users/delete, Movies, Favorites, Watchlist

favorites:

- [X] add movie - depends on: Users, Movies
- [X] remove movie - depends on: Users, Movies
- [X] get user's favorites - depends on: Users, Movies
- [X] get user's favorite movies - depends on: Users, Movies

Watchlist:

- [X] add movie - depends on: Users, Movies
- [X] remove movie - depends on: Users, Movies
- [X] get user's watchlist - depends on: Users, Movies
- [X] get user's watchlist movies - depends on: Users, Movies

Movies:

- [X] get all movies
- [X] get movie by id
- [X] filter movies by tags
- [X] filter movies by rating

## Optimizations

- [X] image lazy loading
- [X] pagination
- [X] style
- [X] 404 page
- [X] 500 page
- [X] try except for all routes
- [X] responsive design

## Trouble Shooting

### 1. Error: Could not run pytest or pytest-watch

Try to run `export PYTHONPATH=.` when on root directory of the project. `ptw` or `pytest` should work after that.
