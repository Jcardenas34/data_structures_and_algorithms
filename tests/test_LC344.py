import pytest
from LC344 import reverse_string


class TestReverseString:

    test_strings = [("abcdef", "fedcba" ), ("racecar", "racecar")]
    error_tests = [(120, TypeError), (list("string1"), TypeError), (tuple("string2"), TypeError)]

    @pytest.mark.parametrize("input, expected", test_strings, ids=[ c[0] for c in test_strings ])
    def test_valid_reverse(self, input, expected):
        assert reverse_string(input) == expected

    @pytest.mark.parametrize("input, expected", error_tests)
    def test_type_errors(self, input, expected):
        with pytest.raises(expected):
            reverse_string(input)