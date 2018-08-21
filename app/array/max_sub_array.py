"""
input:
1st row(array) : -2 -4 3 -1  6 -3 4
output: 9
"""
import sys


def find_max_subarray_sum(arry, length):
    max = -sys.maxsize
    sum = 0
    for i in range(0, length):
        sum = sum + arry[i]
        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max


if __name__ == "__main__":
    arry = list(map(int, input().split()))
    print(arry)
    print(find_max_subarray_sum(arry, len(arry)))
