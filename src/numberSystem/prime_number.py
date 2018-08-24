import unittest


def is_prime(num):
    sqrt = int(num**0.5)
    for i in range(2, sqrt):
        if (num % i == 0):
            return False
        return True


class PrimeNumberTest(unittest.TestCase):

    def test_is_prime_one(self):
        self.assertEqual(is_prime(13), True)

    def test_is_prime_two(self):
        self.assertEqual(is_prime(14), False)


if __name__ == "__main__":
    unittest.main()
