from flask import request


def get_movie_id() -> int:
    movie_id_str = request.args.get('movie_id')
    movie_id = int(
        movie_id_str
    ) if movie_id_str is not None and movie_id_str.isdigit() else -1
    return movie_id
