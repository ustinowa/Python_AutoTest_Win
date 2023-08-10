from create_post import create_post


def test_step1():
    assert create_post() == "my_description", "Test"
