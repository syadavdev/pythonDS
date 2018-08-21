"""
input:
1st row(array) : -2 -4 3 -1  6 -3 4
output: 10
"""
import sys


def max_sub_array_sum(arry, low, mid, high):
    sum = 0
    left_max = -sys.maxsize
    left_index = 0
    for i in range(mid, low):
        sum = sum + arry[i]
        if sum > left_max
            left_max = sum
            left_index = i

    sum = 0
    right_max = -sys.maxsize
    right_index = 0
    for j in range(mid+1, high):
        sum = sum + arry[j]
        if sum > right_max:
            right_max = sum
            right_index = j

    return left_index, right_index, left_max+right_max


def max_sub_array(arry, low, high):
    if low == high:
        return low, high, arry[low]
    else:
        mid = int((low+high)/2)
        left_low, left_high, left_sum = max_sub_array(arry, low, mid)
        right_low, right_high, right_sum = max_sub_array(arry, mid+1, high)
        cross_low, cross_high, cross_sum = max_sub_array_sum(arry, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and  right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    arry = list(map(int, input().split()))
    print(max_sub_array(arry, 0, len(arry)))
