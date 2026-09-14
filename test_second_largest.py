from main import second_largest


def test_regular_list():
    assert second_largest([3, 7, 2, 9, 5]) == 7


def test_negative_numbers():
    assert second_largest([-10, -3, -7]) == -7


def test_with_duplicates():
    assert second_largest([4, 4, 4, 2]) == 2