import unittest


def reverse_number(num):
    reverse = 0
    while num != 0:
        reverse = reverse * 10 + (num % 10)
        num = int(num / 10)
    return reverse


reverse = 0
factor = 1

#ToDo
def reverse_number_one(num):
    global reverse
    global factor
    if num > 0:
        reverse_number(int(num / 10))
        reverse += (num % 10)*factor
        factor *= 10
    return reverse


class ReverseNumberTest(unittest.TestCase):

    def test_reverse_number(self):
        self.assertEqual(reverse_number(1234), 4321)

    def test_reverse_number_one(self):
        self.assertEqual(reverse_number_one(1234), 4321)


if __name__ == "__main__":
    unittest.main()
