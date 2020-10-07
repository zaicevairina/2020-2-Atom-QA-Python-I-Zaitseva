import pytest


class TestSet:

    @pytest.mark.parametrize("i", range(10))
    def test_add(self, i):
        test_set = {i}
        test_set.add(i)
        assert len(test_set) == 1 and i in test_set

    def test_remove(self):
        test_set = {1}
        test_set.remove(1)
        assert len(test_set) == 0

    def test_clear(self):
        test_set = {1, 2, 3, 4, 5}
        test_set.clear()
        assert len(test_set) == 0

    def test_issuperset(self):
        test_set1 = {1, 2, 3, 4}
        test_set2 = {1, 2}
        assert test_set1.issuperset(test_set2)

    def test_union(self):
        test_set1 = {1, 2, 3}
        test_set2 = {3, 4, 5}
        test_set3 = test_set1.union(test_set2)
        expected = {1, 2, 3, 4, 5}
        assert len(test_set3) == 5 and test_set3 == expected
