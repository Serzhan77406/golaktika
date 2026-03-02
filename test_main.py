from main import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(0, 0) == 0    