from src.math_lib import max_fun, is_perfect


def test_none():
    # Arrange
    argument = None

    # Act
    result = max_fun(argument)

    # Assert
    assert result is None, "max(None) should return None"


def test_empty():
    # Arrange
    argument = []

    # Act
    result = max_fun(argument)

    # Assert
    assert result is None, "max([]) should return None"


def test_one_element():
    # Arrange
    argument = [2]

    # Act
    result = max_fun(argument)

    # Assert
    assert result == 2, "max(2) should return 2"


def test_array():
    # Arrange
    argument = [2, 6, 3, 12, 3]

    # Act
    result = max_fun(argument)

    # Assert
    assert result == 12, "max([2, 6, 3, 12, 3]) should return 12"


###################################

def test_perfect_none():
    # Arrange
    argument = None

    # Act
    result = is_perfect(argument)

    # Assert
    assert result is False, "is_perfect(None) should return False"


def test_perfect_zero():
    # Arrange
    argument = 0

    # Act
    result = is_perfect(argument)

    # Assert
    assert result is False, "is_perfect(0) should return False"


def test_perfect_negative():
    # Arrange
    argument = -6

    # Act
    result = is_perfect(argument)

    # Assert
    assert result is False, "is_perfect(-6) should return False"


def test_perfect_true():
    # Arrange
    argument = 496

    # Act
    result = is_perfect(argument)

    # Assert
    assert result is True, "is_perfect(496) should return True"


def test_perfect_false():
    # Arrange
    argument = 12

    # Act
    result = is_perfect(argument)

    # Assert
    assert result is False, "is_perfect(12) should return False"


if __name__ == "__main__":
    test_none()
    test_empty()
    test_one_element()
    test_array()

    test_perfect_none()
    test_perfect_zero()
    test_perfect_negative()
    test_perfect_true()
    test_perfect_false()
