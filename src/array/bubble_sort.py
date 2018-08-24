"""
input:
1st row(array) : 5 4 1 3 4 5
output:
sorted array : [1, 3, 4, 4, 5, 5]
"""


def bubble_sort(arry, size):
    for i in range(0, size):
        for j in range(0, size-1-i):
            if arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]


if __name__ == "__main__":
    arry = list(map(int, input().split()))
    bubble_sort(arry, len(arry))
    print(arry)
