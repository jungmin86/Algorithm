#1. 부분집합의 합
print("부분집합의 합")
def promising(i, weight, total):
    return (weight+total >= W) and (weight == W or weight+S[i+1] <= W)
def s_s(i, weight, total, include):
    global nodes
    nodes += 1
    if(promising(i, weight, total) == True):
        if weight == W:
            print("sol", include)
        else:
            include[i+1] = 1
            s_s(i+1, weight + S[i+1], total - S[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total - S[i+1], include)

n = 6
S = [1,2,3,5,7,8]
W = 9
nodes = 0
print("items =", S, "W =", W)
include = n*[0]
total = 0
for k in S: # 남아있는 것들 토탈으로
    total += k
s_s(-1, 0, total, include)
print("생성노드 수", nodes)


#2. 그래프 색칠하기
print("\n그래프 색칠하기")
def color(i, vcolor):
    global nodes
    nodes += 1 
    if promising(i, vcolor):
        if i == n-1:
            print(vcolor)
        else:
            for k in range(1,m+1):
                vcolor[i+1] = k
                color(i+1, vcolor)
def promising(i,vcolor):
    switch = True
    j = 0
    while j < i and switch:
        if W[i][j] and vcolor[i] == vcolor[j]:
            switch = False
        j += 1
    return switch

n = 6
W = [[0,1,1,0,0,0], [1,0,0,1,0,0], [1,0,0,1,1,0], [0,1,1,0,0,1], [0,0,1,0,0,1], [0,0,0,1,1,0]]
vcolor = n*[0]
nodes = 0
m = 2 # 그래프를 색칠하기 위한 최소 색깔 수
color(-1,vcolor)
print("생성노드 수",nodes)
