from tests.custom_test_case import CustomTestCase


def then_error_message_is(
    test_case: CustomTestCase,
    exception: Exception,
    message: str
) -> None:
    test_case.assertEqual(str(exception), message)
