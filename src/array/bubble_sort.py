"""
input:
5 4 1 3 4 5
output:
sorted array : [1, 3, 4, 4, 5, 5]
"""
import unittest


def bubble_sort(arry):
    size = len(arry)
    for i in range(0, size):
        for j in range(0, size-1-i):
            if arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]
    return arry


class BubbleSortTest(unittest.TestCase):

    arry = [5, 4, 1, 3, 4, 5]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.arry), [1, 3, 4, 4, 5, 5])


if __name__ == "__main__":
    unittest.main()

