#!/usr/bin/python3

"""
LC3794 Requirements:
You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.

"""

def reverse_prefix(in_string:str, prefix_len:int) -> str:
    """
    Reverses the first 'prefix_len' characters of a string.
    
    Args:
        in_string: The string whose substring will be reversed.
        prefix_len: The first 'prefix_len' characters to be reversed
    Returns:
        A string with the first 'prefix_len' characters reversed.
    Raises:
        TypeError: If either in_string or prefix_len are not of type 'str' and 'int' respectively.
        ValueError: If prefix_len is passed as non positive integer. 
    """
        

    if type(in_string) != str:
        raise TypeError(f"reverse_prefix expected type str, got {type(in_string).__name__}")
    if type(prefix_len) != int:
        raise TypeError(f"reverse_prefix expected prefix_len to be of type int, got {type(prefix_len).__name__}")  
    if prefix_len < 0:
        raise ValueError(f"prefix_len expected prefix_len a positive number, got {prefix_len}. ")


    left, right = 0, min(prefix_len, len(in_string)) - 1
    
    out_str = list(in_string)

    while left < right:
        out_str[left], out_str[right] = out_str[right], out_str[left]
        left += 1
        right -= 1

    return "".join(out_str)


if __name__ == "__main__":
    test_case = "test_string"
    res = reverse_prefix(test_case, 4) 
    print(res)