import pytest


class TestString:

    @pytest.mark.parametrize("i", range(6))
    def test_index(self, i):
        test_string = '012345'
        assert test_string[i] == f'{i}'

    def test_isdigit(self):
        test_string = '12'
        assert test_string.isdigit()

    def test_isdigit_negative(self):
        test_string = '21asda'
        assert not test_string.isdigit()

    def test_add(self):
        test_string1 = '12'
        test_string2 = '34'
        assert test_string1 + test_string2 == '1234'

    def test_split(self):
        test_string = '1,2,3'
        result = test_string.split(',')
        expected = ['1', '2', '3']
        assert result == expected
