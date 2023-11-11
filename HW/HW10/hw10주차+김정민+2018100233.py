# 되추적 알고리즘
# import sys
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
print("10번째 해", results[9]) #10번째 해 (인덱스는 9)
print("상태공간 트리 총 개수", total_nodes[0]) #상태공간 트리 총 개수 출력