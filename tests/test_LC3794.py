import pytest
from LC3794 import reverse_prefix


class TestReversePrefix:

    test_prefix =    [(("racecar", 4), "ecarcar"), (("juan_cardenas", 13), "sanedrac_nauj")]
    in_string_type_errors =     [((1, 5), TypeError), ((list("juan_cardenas"), 6), TypeError), ((dict(first='juan', last='cardenas'), 5), TypeError)]
    prefix_len_type_errors =    [(("trial_test", "5"), TypeError), (("juan_cardenas", list('6')), TypeError), (("Arlington, Texas", dict(name='Juan')), TypeError)]
    prefix_len_non_positive =   [(("racecar", -3), ValueError), (("juan_cardenas", -8), ValueError)]
    edge_cases = [(('', 12), )]

    @pytest.mark.parametrize("input, expected", test_prefix, ids=[ str(c[0]) for c in test_prefix ])
    def test_reverse_prefix(self, input:tuple[str, int], expected:str):
        in_string = input[0]
        prefix_len = input[1]
        assert reverse_prefix(in_string, prefix_len) == expected

    @pytest.mark.parametrize("input, expected", in_string_type_errors, ids=[str(c[0]) for c in in_string_type_errors])
    def test_in_string_type_errors(self, input:tuple[int, int], expected:type[TypeError]):
        in_string = input[0]
        prefix_len = input[1]
        with pytest.raises(expected, match=f"reverse_prefix expected type str, got {type(in_string).__name__}"):
            reverse_prefix(in_string, prefix_len)

    @pytest.mark.parametrize("input, expected", prefix_len_type_errors, ids=[str(c[0]) for c in prefix_len_type_errors])
    def test_prefix_len_type_errors(self, input:tuple[str, int|list|dict], expected:type[TypeError]):
        in_string = input[0]
        prefix_len = input[1]
        with pytest.raises(expected, match=f"reverse_prefix expected prefix_len to be of type int, got {type(prefix_len).__name__}"):
            reverse_prefix(in_string, prefix_len)

    @pytest.mark.parametrize("input, expected", prefix_len_non_positive, ids=[str(c[0]) for c in prefix_len_non_positive])
    def test_prefix_len_non_positive(self, input, expected):
        in_string = input[0]
        prefix_len = input[1]
        with pytest.raises(expected):
            reverse_prefix(in_string, prefix_len)

