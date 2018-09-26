import unittest


def heapify(arry, n, i):
    left = (i<<1) + 1
    right = (i<<1) + 2
    largest = i
    if left < n and arry[left] > arry[largest]:
        largest = left
    if right < n and arry[right] > arry[largest]:
        largest = right
    if largest != i:
        arry[largest], arry[i] = arry[i], arry[largest]
        heapify(arry, n, largest)


def heap_sort(arry):
    length = len(arry)
    for i in range(int(length/2), -1, -1):
        heapify(arry, length, i)
    for i in range(length - 1, 0, -1):
        arry[0], arry[i] = arry[i], arry[0]
        heapify(arry, i, 0)


class TestHeapSort(unittest.TestCase):

    arry = [10, 13, 23, 1, 3, 8, 24, 25]
    result = [1, 3, 8, 10, 13, 23, 24, 25]

    def test_heap_sort(self):
        heap_sort(self.arry)
        self.assertEqual(self.arry, self.result)


if __name__ == "__main__":
    unittest.main()
