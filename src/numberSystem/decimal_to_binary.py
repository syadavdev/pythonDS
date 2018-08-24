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


if __name__ == "__main__":
    number = int(input())
    print(decimal_to_binary(number))
    print(decimal_to_binary2(number))
