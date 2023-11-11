#1. Dijkstra 알고리즘
inf = 1000
w=[[0,2,3,inf,inf,4],[inf,0,4,5,3,inf],
[inf,inf,0,6,2,inf], [inf,inf,inf,0,2,inf], [inf,inf,inf,inf,0, inf], [inf,inf,inf,inf,1,0]] 
n=6
f=set()
touch=n*[0]
length=n*[0]
save_length=n*[0]
# NoC = 0

for i in range(1,n):
    length[i] = w[0][i]
for i in range(1,n):
    minD = inf
    for j in range(1,n): #직접 가는 길 있으면 초기화
        if length[j] >= 0 and length[j] < minD: # vi에서 가장 가까운 노드 찾기 (직접 연결)
            minD = length[j]
            vnear = j
    save_length[vnear] = minD
    print(touch[vnear], vnear)
    e = (touch[vnear], vnear)
    f.add(e)
    for k in range(1,n):
        # if(0 < w[vnear][k] < inf): #vnear부터 k까지 가는 이음선(아크)이 있다면 변경될 가능성 있다. (최대횟수 증가)
            # NoC += 1
        if length[vnear] + w[vnear][k] < length[k]:
            length[k] = length[vnear] + w[vnear][k]
            touch[k] = vnear
    length[vnear] = -1
print("최단경로: ", f)
# print(NoC)
print("각 노드별 최단거리: ", save_length)
# print(touch)
