# Movie Picker Project

## Description

### Idea

The project aims to create a movie picker that helps you decide what movie to watch. In an era where algorithms often dictate our choices, this simple application allows you to make a decision based on movie tags, ratings, duration...

### Key Goals and Learning Objectives

This project provides me with the opportunity to explore several domains and learn more about:

- Python and its ecosystem
- Flask
- Hexagonal Architecture
- Tests Driven Development (TDD)
- "given when then" tests structure

## Installation

### Requirements

- install python >= 3.11
- create a virtual environment
- activate the virtual environment
- install dependencies with `pip install -r requirements.txt`

### Optional

#### MyPy

mypy is used for type checking

- run `export PROJECT_DIR=$(pwd)`
- run `dmypy run` to run mypy daemon

You can now run `dmypy status` to check for errors
Or `dmypy check` to check for errors and exit

## Set up database

- be sure to have the virtual environment activated
- run `touch instance/movies_db.db`
- run `flask db upgrade`

## How to run

- be sure to have the virtual environment activated
- run `python app.py` to run in develpment mode

## How to run tests

- be sure to have the virtual environment activated
- run `export PYTHONPATH=.` when on root directory of the project
- run `pytest` to run all tests
- run `pwt` to run all tests in watch mode

## Features

Users:

- [ ] create user
- [ ] login
- [ ] logout
- [ ] add movie to favorites
- [ ] remove movie from favorites
- [ ] add movie to watchlist
- [ ] remove movie from watchlist

Movies:

- [ ] add movie
- [ ] remove movie
- [ ] add tag to movie
- [ ] remove tag from movie
- [X] get all movies
- [ ] get movie by id
- [X] filter movies by tags
- [X] filter movies by rating

## Optimizations

- [ ] image lazy loading
- [X] pagination
- [ ] style

## Trouble Shooting

### 1. Error: Could not run pytest or pytest-watch

Try to run `export PYTHONPATH=.` when on root directory of the project. `pwt` or `pytest` should work after that.
