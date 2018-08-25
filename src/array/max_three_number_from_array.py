"""
input:
array : 78 45 198 45 47 100 101 102
output:
max three elements : (198, 102, 101)
"""
import sys
import unittest


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


class MaxThreeElementsTest(unittest.TestCase):

    arry = [78, 45, 198, 45, 47, 100, 101, 102]
    result = (198, 102, 101)

    def test_max_elements(self):
        self.assertEqual(max_elements(self.arry), self.result)


if __name__ == "__main__":
    unittest.main()
