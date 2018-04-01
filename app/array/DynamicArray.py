#Hacker Rank Dynamic Array Problem

'''
Input :
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

Output :
[7, 3]
'''
def dynamic_array(n , queries):
    seqList = [[] for i in range(n)]
    lastAns = 0

    arry = []

    for lst in queries:
        choose = lst[0]
        x = lst[1]
        y = lst[2]
        pos = (x ^ lastAns) % n;
        if choose == 1:
            seqList[pos].append(y)
        elif choose == 2:
            index = y % len(seqList[pos])
            lastAns = seqList[pos][index]
            arry.append(lastAns)

    return arry


if __name__ == '__main__':
    n, q = map(int, input().split())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    print(queries)
    print(dynamic_array(n,queries))