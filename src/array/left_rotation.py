"""
Input :
arry - 1 2 3 4 5
rotation - 4
Output :
left rotated array - 5, 1, 2, 3, 4
"""
import unittest


def left_rotaion(arry, rotation):
    n = len(arry)
    if n < rotation:
        rotation = rotation % n

    for i in range(rotation):
        tmp = arry[0]
        k = 1
        while k < n:
            arry[k-1] = arry[k]
            k += 1
        arry[k-1] = tmp
    return arry


class LeftRotaionTest(unittest.TestCase):

    arry = [1, 2, 3, 4, 5]
    rotation = 4

    def test_left_rotaion(self):
        self.assertEqual(left_rotaion(self.arry, self.rotation), [5, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
