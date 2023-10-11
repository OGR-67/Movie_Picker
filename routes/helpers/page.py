from flask import request


def get_page_number() -> int:
    page_str = request.args.get("page")
    if page_str is None or not page_str.isdigit():
        return 1
    else:
        return int(page_str)
