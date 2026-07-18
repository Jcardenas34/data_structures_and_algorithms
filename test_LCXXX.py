import pytest
# from LCXXX import function_name

def function_name(in_str): pass


class TestFunctions:

    test_case = [("",True)]

    @pytest.mark.parametrize("input, expected", test_case, ids=[])
    def test_type(self, input, expected):
        assert function_name(input) == expected