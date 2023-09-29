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

- install python >= 3.11
- create a virtual environment
- install dependencies with `pip install -r requirements.txt`

## Set up database

- run `touch instance/movies_db.db`
- run `flask db upgrade`

## How to run

- run `python app.py` to run in develpment mode

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
- [ ] filter movies by tags
- [ ] filter movies by rating
- [ ] filter movies by duration

## Tests

- run `pytest` to run all tests
- run `pwt` to run all tests in watch mode

## Trouble Shooting

### 1. Error: Could not run pytest or pytest-watch

Try to run `set PYTHONPATH=.` when on root directory of the project. `pwt` or `pytest` should work after that.
