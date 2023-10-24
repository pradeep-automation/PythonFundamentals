import pytest


@pytest.fixture
def set_up():
    print("I do run before the tests")
    yield
    print("I do run after the tests")
