import sys
sys.path.append('C:/Users/mrjoh/OneDrive/Рабочий стол/Python Office/python_2_rep/homework4/')
from tasks.task_2_mock_input import count_dots_on_i
import pytest

"""This test can fail on your machine. It occurs because site content changes every day and the number of i is too. But the last test case 'example.com' is static. """

@pytest.mark.parametrize("url, expected_result", [('https://en.wikipedia.org/wiki/JPMorgan_Chase', 30964),
                                                ('https://en.wikipedia.org/wiki/Mitsubishi_UFJ_Financial_Group', 12794),
                                                ('https://en.wikipedia.org/wiki/Bank_of_America', 31355),
                                                ('https://en.wikipedia.org/wiki/New_York_Stock_Exchange', 17571),
                                                ('https://example.com/', 59)])
def test_count_dots_on_i_yes(url, expected_result):
    """Tests whether count_dots_on_i returns the correct number of i on a web_page"""
    assert count_dots_on_i(url) == expected_result


@pytest.mark.parametrize("url, expected_error", [('htps://www.tiktok.com/STOP_WATCH_It_NOW!', ValueError),
                                               ('snapchat.com', ValueError),
                                               ('https://www.eror.er', ValueError),
                                               ('https://www.forgotify.ru', ValueError),
                                               ('online_games.wt', ValueError)])
def test_count_dots_on_i_error(url, expected_error):
    """Tests whether count_dots_on_i returns the ValueError error when it gets any error"""
    with pytest.raises(expected_error):
        count_dots_on_i(url)


if __name__ == '__main__':
    pytest.main()
