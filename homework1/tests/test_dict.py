import pytest


class TestDict:

    def test_get(self):
        test_dict = {'dict': 1}
        assert 'dict' in test_dict and test_dict['dict'] == 1

    def test_update(self):
        test_dict = {'key': 'value'}
        test_dict.update([('key', 'value2'), ('key2', 'value3')])
        expected = {'key': 'value2', 'key2': 'value3'}
        assert test_dict == expected

    @pytest.mark.parametrize('i', range(10))
    def test_get(self, i):
        test_dict = {'key': i}
        assert test_dict.get('key') == i

    def test_clear(self):
        test_dict = {'key': 'value'}
        test_dict.clear()
        assert test_dict == dict()

    def test_pop(self):
        test_dict = {'key': 'value'}
        result = test_dict.pop('key')
        assert ('key' not in test_dict) and result == 'value'
