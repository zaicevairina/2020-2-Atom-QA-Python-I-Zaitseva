import pytest


class TestInt:

    def test_add(self):
        assert 2 + 2 == 4

    def test_sub(self):
        assert 1 - 1 == 0

    @pytest.mark.parametrize("i", range(10))
    def test_pow(self, i):
        assert i**2 == i*i

    def test_mod(self):
        assert 14 % 3 == 2

    def test_div(self):
        assert 3 // 2 == 1
