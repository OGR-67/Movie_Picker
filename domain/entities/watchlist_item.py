from dataclasses import dataclass


@dataclass
class WatchlistItem:
    id: int
    user_id: int
    movie_id: int
