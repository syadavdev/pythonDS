import unittest


def quick_sort(arry, low, high):
    if low < high:
        divider = partition(arry, low, high)
        quick_sort(arry, low, divider - 1)
        quick_sort(arry, divider + 1, high)


def partition(arry, low, high):
    piviot = arry[high]
    i = low - 1
    for j in range(low, high):
        if arry[j] <= piviot:
            i += 1
            arry[i], arry[j] = arry[j], arry[i]
    arry[i+1], arry[high] = arry[high], arry[i+1]
    return i + 1


class TestQuickSort(unittest.TestCase):

    arry = [45, 12, 3, 45, 178, 44, 56, 87, 43, 1]
    result = [1, 3, 12, 43, 44, 45, 45, 56, 87, 178]

    def test_Quick_sort(self):
        quick_sort(self.arry, 0, len(self.arry) - 1)
        self.assertEqual(self.arry, self.result)


if __name__ == "__main__":
    unittest.main()
