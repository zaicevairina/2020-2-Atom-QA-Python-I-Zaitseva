import pytest


class TestList:

    def test_append(self):
        test_list = []
        test_list.append(2)
        assert len(test_list) == 1 and test_list[-1] == 2

    @pytest.mark.parametrize("i", range(10))
    def test_pop(self, i):
        test_list = [2, 3, 5, i]
        result = test_list.pop()
        assert len(test_list) == 3 and result == i

    def test_eq(self):
        test_list = [1, 2]
        test_list2 = [1, 2]
        assert test_list == test_list2

    def test_add(self):
        test_list = [1, 2]
        test_list2 = [3, 4]
        result = test_list + test_list2
        expected = [1, 2, 3, 4]
        assert len(result) == 4 and result == expected

    def test_clear(self):
        test_list = [1, 2]
        test_list.clear()
        assert test_list == []

    def test_mul(self):
        result = [1]*3
        expected = [1, 1, 1]
        assert len(result) == 3 and result == expected
