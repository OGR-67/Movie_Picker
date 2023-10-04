from dataclasses import dataclass


@dataclass
class Favorite:
    id: int
    user_id: int
    movie_id: int
