"""
input:
1st row(array) : 12
output:
Binary form : 1100
"""


def decimal_to_binary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * decimal_to_binary(int(num/2))


if __name__ == "__main__":
    number = int(input())
    print(decimal_to_binary(number))
