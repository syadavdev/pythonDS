import unittest


def replace_zero(num):
    if num == 0:
        return 0

    digit = int(num % 10)

    if digit == 0:
        digit = 5
    return replace_zero(int(num/10)) * 10 + digit


class ReplaceZeroTest(unittest.TestCase):

    num = 1040020

    def test_replace_zero(self):
        self.assertEqual(replace_zero(self.num), 1545525)


if __name__ == "__main__":
    unittest.main()
