"""
input:
array : -2 -4 3 -1  6 -3 4
output: 9
"""
import sys
import unittest


def find_max_subarray_sum(arry):
    length = len(arry)
    max = -sys.maxsize
    sum = 0
    for i in range(0, length):
        sum = sum + arry[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max


class FindMaxSubarraySumTest(unittest.TestCase):

    arry = [-2, -4, 3, -1,  6, -3, 4]

    def test_max_subarray_sum(self):
        self.assertEqual(find_max_subarray_sum(self.arry), 9)


if __name__ == "__main__":
    unittest.main()
