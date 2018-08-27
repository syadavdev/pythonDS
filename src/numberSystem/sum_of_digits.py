import unittest


def digits_sum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = int(num / 10)
    return sum


def digits_sum_one(num):
    return 0 if num == 0 else num % 10 + digits_sum_one(int(num / 10))


class DigitSumTest(unittest.TestCase):

    def test_digits_sum(self):
        self.assertEqual(digits_sum(1234), 10)

    def test_digits_sum_one(self):
        self.assertEqual(digits_sum_one(1234), 10)


if __name__ == "__main__":
    unittest.main()
