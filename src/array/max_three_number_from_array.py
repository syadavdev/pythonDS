"""
input:
1st row(array) : 78 45 198 45 47 100 101 102
output:
sorted array : (198, 102, 101)
"""
import sys


def max_elements(arry):
    first = -sys.maxsize
    second = -sys.maxsize
    third = -sys.maxsize
    for i in range(0, len(arry)):
        if arry[i] > first:
            third = second
            second = first
            first = arry[i]
        elif arry[i] > second:
            third = second
            second = arry[i]
        else:
            third = arry[i]
    return first, second, third


if __name__ == "__main__":
    arry = list(map(int, input().split()))
    print(max_elements(arry))
