
#1. 최단경로 출력
# def floyd(g, n):
#     # node number는 1부터 n
#     D = g
#     for k in range(n): #중간
#         for i in range(n): #출발
#             for j in range(n): #도착
#                 D[i][j] = min(D[i][j], D[i][k] + D[k][j])
#     return D
print("1. 최단경로 출력")

def allShortestPath(g, n):
    for i in range(n):
        for j in range(n):
            print(g[i][j], end= " ")
        print()
    D = g
    P = [[0] * n for i in range(n)] # 마지막으로 거친 노드 인덱스 (+1) 저장 -> 안거치면 0
    for k in range(n): #k 0부터 채워나가자
        for i in range(n):
            for j in range(n):
                if (D[i][k] + D[k][j]) < D[i][j]: 
                    P[i][j] = k+1 #중간 노드 저장 (가장 마지막에 방문)
                    D[i][j] = D[i][k] + D[k][j] #더 짧은 길이로 초기화
    return D, P

def path(P, q, r):
    if P[q - 1][r - 1] != 0: #배열의 인덱스는 0부터 시작이니까 -1 해주어야 함
        k = P[q - 1][r - 1]
        path(P, q, k)
        print("v", k)
        path(P, k, r)

def printMatrix(d): 
    n=len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(d[i][j],end=" ")
        print()


inf=1000
# g=[[0,1,inf, 1,5], [9,0,3,2,inf], [inf,inf,0,4,inf], [inf,inf,2,0,3], [3,inf,inf,inf,0]]
g = [[0, 4, inf, inf, 4], [6, 0, inf, inf, inf], [1, 2, 0, 1, inf], [inf, inf, 4, 0, inf], [9, inf, 3, 5, 0]]
d, p = allShortestPath(g,5)
print()
printMatrix(d)
print()
printMatrix(p)
path(p, 2, 4)


#2. 연쇄행렬 최소 곱셈 알고리즘
print("2. 연쇄행렬 최소 곱셈 알고리즘")
import utility

def order(p,i,j):
    if i == j:
        print("A", str(i), end="")
    else:
        k = p[i][j]
        print("(", end="")
        order(p, i, k)
        order(p, k+1, j)
        print(")", end="")

# d=[5,2,3,4,6,7,8] #7개
d=[2,3,4,3,2,4] 
n=len(d)-1 
m=[[0 for j in range(1,n+2)] for i in range(1,n+2)] # 최소 곱셉 횟수
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)] # 최소 곱셈 순서

def minimum_multiply(n, d, p):
    m = [[0] * (n+1) for _ in range(n+1)]

    for diagonal in range(1, n): # 부분 체인의 길이
        for i in range(1, n - diagonal + 1): #시작점
            j = i + diagonal #끝점
            min_val = float('inf')
            min_k = 0

            for k in range(i, j): #시작과 끝 사이에 가능한 모든 분할지점
                val = m[i][k] + m[k+1][j] + (d[i-1] * d[k] * d[j])
                if val < min_val:
                    min_val = val
                    min_k = k

            m[i][j] = min_val
            p[i][j] = min_k
    utility.printMatrix(m) 

    return m[1][n]


minimum_multiply(n,d,p)

print() 
utility.printMatrix(p) 
order(p,1,5)