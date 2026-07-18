#!/usr/bin/python3

'''
LC344 Requirements:
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

'''

def reverse_string(in_string:str) -> str:
    '''
    Reverses a string
    '''

    if type(in_string) != str:
        raise TypeError(f"Expected type str, recieved {type(in_string).__name__}")

    left, right = 0, len(in_string) - 1
    out_string = list(in_string)

    while left < right:
        out_string[left], out_string[right] = out_string[right], out_string[left]
        left += 1
        right -= 1
    return "".join(out_string) 


if __name__ == "__main__":
    test_case = "abcdefg"
    res = reverse_string(test_case)
    print(res)