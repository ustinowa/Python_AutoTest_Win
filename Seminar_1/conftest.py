import pytest

@pytest.fixture
def incorrect_word():
    return "карава"

@pytest.fixture
def correct_word():
    return "корова"