import unittest


def multiplication_one(A, B):
    n = len(A)
    C = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = 0
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C


def multiplication_two(A, B):
    #To Do
    pass


class MultiplicationTest(unittest.TestCase):

    A = [[1,2,3] ,[4,5,6], [7,8,9]]
    B = [[1,2,3] ,[4,5,6], [7,8,9]]
    C = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

    def test_multiplication_one(self):
        self.assertEqual(multiplication_one(MultiplicationTest.A ,MultiplicationTest.B), MultiplicationTest.C)

    def test_multiplication_two(self):
        self.assertEqual(multiplication_two(MultiplicationTest.A, MultiplicationTest.B), MultiplicationTest.C)


if __name__ == "__main__":
    unittest.main()
