import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/')
from tasks.task_5_optional import fizzbuzz_optional
import pytest



@pytest.mark.parametrize("n, expected_result", [(5, ['1', '2', 'Fizz', '4', 'Buzz']),
                                                (10, [
                                                    '1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']),
                                                (15, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8',
                                                           'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']),
                                                (30, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz'])])
def test_fizzbuzz_yes(n, expected_result):
    """Tests whether fizzbuzz returns the correct result"""
    assert fizzbuzz_optional(n) == expected_result


@pytest.mark.parametrize("n, expected_error", [('5', TypeError),
                                               ("sth", TypeError),
                                               ([2, 4, 5], TypeError),
                                               (fizzbuzz_optional, TypeError),
                                               (5.3, TypeError)])
def test_fizzbuzz_error(n, expected_error):
    """Tests whether fizzbuzz returns the correct error when it gets an error"""
    with pytest.raises(expected_error):
        fizzbuzz_optional(n)


if __name__ == '__main__':
    pytest.main()
