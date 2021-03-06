import unittest


def binery_search(arry ,low, high, ele):
    mid = (low+high)//2
    if low <= high:
        if arry[mid] == ele:
            return mid+1
        elif arry[mid] > ele:
            return binery_search(arry, low, mid-1, ele)
        return binery_search(arry, mid+1, high, ele)
    else:
        return -1


class BinarySearchTestCase(unittest.TestCase):

    arry = [3, 4, 5, 6, 7, 8, 9]
    low = 0
    high = 6

    def test_binery_search_one(self):
        self.assertEqual(binery_search(self.arry, self.low, self.high, 4), 2)

    def test_binery_search_two(self):
        self.assertEqual(binery_search(self.arry, self.low, self.high, 1), -1)


if __name__ == "__main__":
    unittest.main()
