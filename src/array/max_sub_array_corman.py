#Corman problem
"""
input:
1st row(array) : -2 -4 3 -1  6 -3 4
output: 9
"""
import sys
import unittest


def max_sub_array_sum(arry, low, mid, high):
    sum = 0
    left_max = -sys.maxsize
    for i in range(mid, low-1, -1):
        sum = sum + arry[i]
        if sum > left_max:
            left_max = sum

    sum = 0
    right_max = -sys.maxsize
    for j in range(mid+1, high+1):
        sum = sum + arry[j]
        if sum > right_max:
            right_max = sum

    return left_max+right_max


def max_sub_array(arry, low, high):
    if low == high:
        return arry[low]
    else:
        mid = (low+high)//2
        left_sum = max_sub_array(arry, low, mid)
        right_sum = max_sub_array(arry, mid+1, high)
        cross_sum = max_sub_array_sum(arry, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum
        elif right_sum >= left_sum and  right_sum >= cross_sum:
            return right_sum
        else:
            return cross_sum


class FindMaxSubarraySumTest(unittest.TestCase):

    arry = [-2, -4, 3, -1,  6, -3, 4]
    low = 0
    high = 7

    def test_max_subarray_sum(self):
        self.assertEqual(max_sub_array(self.arry, self.low, self.high-1), 9)


if __name__ == "__main__":
    unittest.main()
