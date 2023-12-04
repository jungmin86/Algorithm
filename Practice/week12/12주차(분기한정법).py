# 1. 배낭채우기 알고리즘 (분기한정법 가지치기 DFS)
def kp(i, profit, weight):
    global bestset
    global maxp

    if weight <= W and profit > maxp:
        maxp = profit
        bestset = include[:]
    if promising(i, weight, profit):
        include[i+1] = 1
        kp(i+1, profit + p[i+1], weight + w[i+1])
        include[i+1] = 0
        kp(i+1, profit, weight)

def promising(i, weight, profit):
    global maxp
    if weight >= W:
        return False
    else:
        j =i+1
        bound = profit
        tot_weight = weight
        while j < n and tot_weight + w[j] <= W:
            tot_weight += w[j]
            bound += p[j]
            j+=1
        k = j
        if k < n:
            bound += (W-tot_weight) * p[k]/w[k]
    return bound > maxp


n = 4
W = 16
p = [40,30,50,10]
w = [2,5,10,5]
maxp = 0
include = [0]*n
bestset = [0]*n
kp(-1,0,0)
print(maxp)
print(bestset)

