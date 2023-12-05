from day1.solution import find_first_number, find_last_number


def test_find_first_number():
    assert find_first_number('1') == 1
    assert find_first_number('abc1asda') == 1
    assert find_first_number('aasdc3as4da') == 3
    assert find_first_number('adwq93asda') == 9


def test_last_first_number():
    assert find_last_number('1') == 1
    assert find_last_number('5abc2asd') == 2
    assert find_last_number('abc6asd3q') == 3
