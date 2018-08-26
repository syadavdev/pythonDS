#HackerEarth
"""
Input :
4
1 2 3 4
5
1 2
1 3
1 4
4 4
2 2
Output :
3
6
10
4
2
"""


def find_sum(arry, l, r, arry_sum):
    length = len(arry)
    while l > -1 or r < length:
        if l > -1:
            arry_sum = arry_sum - arry[l]
        if r < length:
            arry_sum = arry_sum - arry[r]
        l = l - 1
        r = r + 1
    return arry_sum


if __name__ == "__main__":
    n = input()
    arry = list(map(int, input().split()))          #find better solution for this array input than this
    arry_sum = sum(arry)
    q = int(input())
    for i in range(q):
        l, r = input().split()
        l = int(l)
        r = int(r)
        print(find_sum(arry, l-2, r, arry_sum))
