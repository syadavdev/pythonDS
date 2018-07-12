'''
input:
1st row(array) : 5 4 1 3 4 9
output:
sorted array : 1 3 4 4 5 9
'''


def insertion_sort(arry):
    for i in range(1, len(arry)):
        j = i - 1
        key = arry[i]
        while (j >= 0) & (arry[j] > key):
            arry[j+1] = arry[j]
            j -= 1
        arry[j+1] = key


if __name__ == "__main__":
    arry = list(map(int, input().split()))
    print(arry)
    insertion_sort(arry)
    print(arry)
