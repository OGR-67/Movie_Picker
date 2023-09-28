-- for sqLite3
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    original_language VARCHAR(50),
    summary VARCHAR(500),
    release_date VARCHAR(10),
    poster_url VARCHAR(255),
    genre VARCHAR(100),
    vote_average FLOAT
);