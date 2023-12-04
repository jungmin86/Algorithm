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
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
include = [0] * n
maxProfit = 0
bestset = [0] * n
node_count = 0
max_queue_size = 0

kp_BFS()
print("(가) 총 노드의 개수 :", node_count)
print("(나) Queue에 존재하는 최대 노드 개수 :", max_queue_size)
print("최적 조합", bestset)
