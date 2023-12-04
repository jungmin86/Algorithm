# 1. DFS
print("1. DFS")
def kp(i, profit, weight):
    global bestset
    global maxp
    global node_count
    node_count += 1

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
W = 7
p = [18,10,12,4]
w = [3,5,6,4]
maxp = 0
include = [0]*n
bestset = [0]*n
node_count = 0
kp(-1,0,0)
print("(가) 최댓값을 주는 해와 그 때의 이익 :", bestset, maxp)
print("(나) 생성된 총 노드의 개수 :", node_count)


print("2. BFS")
import queue

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.include = include

def kp_BFS():
    global maxProfit
    global bestset
    global node_count
    global max_queue_size

    q = queue.Queue()

    v = Node(-1, 0, 0, include)
    node_count += 1
    q.put(v)

    while not q.empty():
        max_queue_size = max(max_queue_size, q.qsize())
        v = q.get()

        u = Node(0, 0, 0, v.include.copy())
        node_count += 1
        u.level = v.level + 1
        u.weight = v.weight + w[u.level]
        u.profit = v.profit + p[u.level]

        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit
            u.include[u.level] = 1
            bestset = u.include.copy()

        if compBound(u) > maxProfit:
            q.put(u)

        u = Node(0, 0, 0, v.include.copy())
        node_count += 1
        u.level = v.level + 1
        u.weight = v.weight
        u.profit = v.profit

        if compBound(u) > maxProfit:
            q.put(u)

    return maxProfit, bestset

def compBound(u):
    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j < n and totweight + w[j] <= W:
            totweight = totweight + w[j]
            result += p[j]
            j += 1
        k = j 
        if k < n:
            result += (W - totweight) * p[k]/w[k]
        
        return result

n = 4
W = 7
p = [18,10,12,4]
w = [3,5,6,4]
include = [0] * n
maxProfit = 0
bestset = [0] * n
node_count = 0
max_queue_size = 0

kp_BFS()
print("(가) 총 노드의 개수 :", node_count)
print("(나) Queue에 존재하는 최대 노드 개수 :", max_queue_size)
print("최댓값을 주는 해와 그 때의 이익", bestset, maxProfit)


