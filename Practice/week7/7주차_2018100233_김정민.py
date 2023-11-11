# 1. Prim 알고리즘
print("1. Prim 알고리즘")
import utility

inf = 1000
w = [
    [0,1,3,inf,inf],
    [1,0,3,6,inf],
    [3,3,0,4,2],
    [inf,6,4,0,5],
    [inf,inf,2,5,0]
]

F = set()
utility.printMatrix(w)
n = len(w)

nearest = n*[0] #가까운 리스트
distance = n*[0] #그에 따른 거리
for i in range(1,n): #v(1)과 매핑시켜놓는다. (초기화)
    nearest[i] = 0
    distance[i] = w[0][i]

for i in range(n-1): # n-1개 정점을 추가
    minD = inf
    for j in range(1, n): #v(1)은 빼고 돌려도 됨 (기본값)
        if distance[j] >= 0 and distance[j] < minD: # v(i)에 연결된 가장 거리가 짧은 노드 찾는 과정
            minD = distance[j]
            vnear = j #가장 가까운 노드
    e = (vnear, nearest[vnear]) # 연결선
    F.add(e)
    distance[vnear] = -1 # 더 이상 고려 대상 아님

    for i in range(1,n):
        if w[i][vnear] < distance[i]: # distance 갱신
            distance[i] = w[i][vnear]
            nearest[i] = vnear

print()
print(F)

#2. Kruskal 알고리즘
print("\n2. Kruskal 알고리즘")
parent = dict()
rank = dict() #집합의 크기

def make_singleton_set(v):
    parent[v] = v # 처음엔 모두 각자
    rank[v] = 1

def find(v): #최상위 부모 찾기
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(r1, r2): # 작은 집합을 큰 집합에 병합
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1 #합쳐지면
            rank[r1] += rank[r2]
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += rank[r1]

def kruskal(graph):
    vertices = graph['vertices']
    edges = list(graph['edges'])
    edges.sort()

    F = set()
    n = len(vertices)

    for i in range(n):
        make_singleton_set(i) #단일 집합으로 만들기
    
    t = 0
    while len(F) < n-1: # 간선의 개수 n-1 되면 스톱
        e = edges[t]
        (i, j) = (edges[t][1], edges[t][2])
        i = vertices.index(i)
        j = vertices.index(j)
        p = find(i) #최고부모
        q = find(j) #최고부모
        if (p != q): # 두 노드의 부모가 다르다 -> 사이클 생성하지 않는다.
            union(p,q)
            F.add(e)
        t += 1
    return F



graph = {
'vertices': ['A', 'B', 'C', 'D', 'E'], 
'edges': set([
(1, 'A', 'B'), (3, 'A', 'C'), (3, 'B', 'C'), (6, 'B', 'D'), (4, 'C', 'D'), (2, 'C', 'E'), (5, 'D', 'E'), 
    ])
}
mst=kruskal(graph)
print(mst)


