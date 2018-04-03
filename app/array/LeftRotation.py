'''
Input :
5 4
1 2 3 4 5
Output :
5, 1, 2, 3, 4
'''
def left_rotaion(n, q, arry):
    if n < q:
        q = q % n

    for i in range(q):
        tmp = arry[0]
        k = 1
        while k < n:
            arry[k-1] = arry[k]
            k += 1
        arry[k-1] = tmp
    return arry


if __name__ == "__main__":
    n, q = input().split()
    n = int(n)
    q = int(q)
    print("\n")
    print(n,q)

    arry = list(map(int,input().split()))
    arry = left_rotaion(n,q,arry)
    print(arry)