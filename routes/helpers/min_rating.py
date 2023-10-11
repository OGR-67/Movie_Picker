from flask import request


def get_min_rating() -> int:
    min_rating_str = request.args.get("min_rating")
    if min_rating_str is None or not min_rating_str.isdigit():
        return 0
    else:
        return int(min_rating_str)
