import unittest


def gcd(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    if num1 == num2:
        return num1
    if num1 > num2:
        return gcd(num1-num2, num2)
    return gcd(num1, num2 - num1)


def gcd1(num1, num2):
    if num2 != 0:
        return gcd1(num2, num1 % num2)
    return num1


class GreatestCommonDivisonTest(unittest.TestCase):

    num1 = 98
    num2 = 56

    def test_gcd(self):
        self.assertEqual(gcd(self.num1, self.num2), 14)

    def test_gcd_one(self):
        self.assertEqual(gcd1(self.num2, self.num1), 14)


if __name__ == "__main__":
    unittest.main()
