import pytest


class Test_001:
    def setup_class(self):
        print('------------->>>setup_class')
    def teardown_class(self):
        print('------------->>>teardown_class')
    def test_001(self):
        print('------------->>>test_001')
        assert True
