"""
input:
1st row(array) : 5 4 1 3 4 5
output:
sorted array : [1, 3, 4, 4, 5, 5]
"""
import unittest


def merge(arry, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = [0]*n1
    right = [0]*n2

    for i in range(0, n1):
        left[i] = arry[l+i]
    for j in range(0, n2):
        right[j] = arry[m+j+1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arry[k] = left[i]
            i += 1
        elif right[j] <= left[i]:
            arry[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arry[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arry[k] = right[j]
        j += 1
        k += 1


def merge_sort(arry, l, r):
    if l < r:
        mid = int((l+(r-1))/2)
        merge_sort(arry, l, mid)
        merge_sort(arry, mid+1, r)
        merge(arry, l, mid, r)
    return arry


class MergeSortTest(unittest.TestCase):

    arry = [5, 4, 1, 3, 4, 5]
    low = 0
    high = 6

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.arry, self.low, self.high-1), [1, 3, 4, 4, 5, 5])


if __name__ == "__main__":
    unittest.main()
