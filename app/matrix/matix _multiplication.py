import unittest


def multiplication(A, B):
    n = len(A)
    C = [[0 for x in range(0, n)] for y in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = 0
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k]*B[k][j]
    return C


class MultiplicationTest(unittest.TestCase):

    A = [[1,2,3] ,[4,5,6], [7,8,9]]
    B = [[1,2,3] ,[4,5,6], [7,8,9]]
    C = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]

    def test_multiplcation(self):
        self.assertEqual(multiplication(MultiplicationTest.A ,MultiplicationTest.B), MultiplicationTest.C)


if __name__ == "__main__":
    unittest.main()
