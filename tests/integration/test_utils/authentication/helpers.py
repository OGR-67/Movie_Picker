from tests.custom_test_case import CustomTestCase


def when_login(
    test_case: CustomTestCase,
    username: str,
    password: str
) -> None:
    test_case.authentication_service.login(username, password)


def when_check_is_logged_in(
    test_case: CustomTestCase
) -> bool:
    return test_case.authentication_service.is_logged_in()
