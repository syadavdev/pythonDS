"""
input:
1st row(array) : 12
output:
Binary form : 1100
"""
import unittest


def decimal_to_binary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimal_to_binary(int(num/2))


sum = 0
factor = 1


def decimal_to_binary2(num):
    global sum
    global factor
    if num == 0:
        return 0
    else:
        reminder = num % 2
        sum = sum + reminder * factor
        factor = factor * 10
        decimal_to_binary2(int(num/2))
        return sum


class DecimalToBinaryTest(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(12), 1100)

    def test_decimal_to_bibary(self):
        self.assertEqual(decimal_to_binary2(12), 1100)


if __name__ == "__main__":
    unittest.main()
