#1. 부분집합의 합
print("부분집합의 합")
def promising(i, weight, total):
    return (weight+total >= W) and (weight == W or weight+w[i+1] <= W)
def s_s(i, weight, total, include):
    global nodes
    nodes += 1
    if(promising(i, weight, total) == True):
        if weight == W:
            print("sol", include)
        else:
            include[i+1] = 1
            s_s(i+1, weight + w[i+1], total - w[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total - w[i+1], include)

n = 4
w = [1,2,4,6]
W = 6
nodes = 0
print("items =", w, "W =", W)
include = n*[0]
total = 0
for k in w: # 남아있는 것들 토탈으로
    total += k
s_s(-1, 0, total, include)
print(nodes)

#2. 그래프 색칠하기
print("그래프 색칠하기")
def color(i, vcolor):
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

n = 4
W = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
vcolor = n*[0]
m = 3
color(-1,vcolor)