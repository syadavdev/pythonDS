"""
input:
5 4 1 3 4 9
output:
sorted array : 1 3 4 4 5 9
"""
import unittest


def insertion_sort(arry):
    for i in range(1, len(arry)):
        j = i - 1
        key = arry[i]
        while (j >= 0) & (arry[j] > key):
            arry[j+1] = arry[j]
            j -= 1
        arry[j+1] = key
    return arry


class InsertionSortTest(unittest.TestCase):

    arry = [5, 4, 1, 3, 4, 9]

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.arry), [1, 3, 4, 4, 5, 9])


if __name__ == "__main__":
    unittest.main()