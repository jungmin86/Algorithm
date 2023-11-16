# 깊이우선검색 (DFS)
print("깊이우선검색 (DFS)")
import utility
import queue
e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]} 
n=8
a = [ [0 for j in range(0,n)] for i in range(0,n)] 
for i in range(0,n-1):
    for j in range(i+1,n):
        if i in e:
            if j in e[i]: 
                a[i][j]=1 
                a[j][i]=1
utility.printMatrix(a)
visited =n*[0]
def DFS(a,v):
    q = queue.Queue()  # FIFO
    q.put(v)
    visited[v] = 1

    while not q.empty():
        u = q.get()
        print(u)

        for i in range(0, n):
            if a[u][i] == 1 and visited[i] == 0: #아직 검사 안했고, 꺼낸 거랑 연결되어 있는 것은?
                q.put(i)
                visited[i] = 1

DFS(a,0)

# 되추적 알고리즘
import sys
print("되추적 알고리즘")
def promising(i, col):
    switch = True
    k = 0
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
        k += 1
    return switch

def queens(n, i, col):
    if(promising(i,col)):
        if i == n - 1:
            print(col)
            results.append(col.copy())
        else:
            for j in range(0,n):
                col[i + 1] = j
                queens(n, i + 1, col)
    total_nodes[0] += 1





results = []
total_nodes = [0]
n=8
col=n*[0]
queens(n,-1,col)
print("해의 총 개수", len(results)) #해의 총 개수 출력
print("10번째 해", results[9])
print("상태공간 트리 총 개수", total_nodes[0]) #상태공간 트리 총 개수 출력



