#1. 최적이진검색트리
print("1. 최적이진검색트리")
import utility

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data = data

def tree(key,r,i,j):
    k = r[i][j]
    if(k==0):
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key,r,i,k-i)
        p.r_child = tree(key,r,k+1,j)
        return p

# p1=4/16, p2=3/16, p3=6/16, p4=2/16, p5=1/16
key = [" ", "A","B","C","D", "E"]
p = [0,0.25, 0.1875, 0.375, 0.125, 0.0625]
# key = [" ", "A","B","C","D"]
# p = [0,0.375, 0.375, 0.125, 0.125]
n = len(p) - 1
a=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
r=[[0 for j in range(0,n+2)] for i in range(0,n+2)]
for i in range (1,n+1):
    a[i][i-1]=0
    a[i][i]=p[i]
    r[i][i]=i
    r[i][i-1]=0
a[n+1][n]=0
r[n+1][n]=0

for diagonal in range(1, n):
    for i in range(1, n - diagonal + 1):
        j = i + diagonal
        costs = []
        cost_sum = sum(p[i:j + 1])
        for k in range(i, j + 1):
            costs.append(a[i][k - 1] + a[k + 1][j]) # k별로 다 넣어봐
        a[i][j] = min(costs) + cost_sum
        r[i][j] = i + costs.index(min(costs))  # 최소 비용을 가지는 루트의 인덱스
minAvg = a[1][n]


utility.printMatrixF(a)
print()
utility.printMatrix(r)
root=tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)

#2. DNA 서열 맞춤
print("2. DNA 서열 맞춤")
import utility
a=['A','A','C','A','G','T','T','A','C','C']
b=['T','A','A','G','G','T','C','A']
# a=['C','A','G','A','C','T','A','A']
# b=['C','C','G','C','T','A','C']
m=len(a) 
n=len(b) 

table = [[0 for j in range(0, n+1)] for i in range(0, m+1)] # m+1 행, n+1 열
minindex = [[ (0,0) for j in range(0, n+1)] for i in range(0, m+1)] # 경로 추적

for j in range(n-1,-1,-1):
    table[m][j] = table[m][j+1]+2
for i in range(m-1,-1,-1):
    table[i][n] = table[i+1][n]+2

#구현

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        penalty = 0 if a[i] == b[j] else 1

        table[i][j] = min(table[i+1][j+1]+penalty, table[i+1][j]+2,table[i][j+1]+2)

        if(table[i][j] == table[i+1][j+1]+penalty): #대각선에서 올라온 경우 (불일치 Or 일치)
            minindex[i][j] = i+1,j+1
        elif(table[i][j] == table[i+1][j]+2): # 밑에서 올라온 경우 (b에 틈 발생)
            minindex[i][j] = i+1,j
        else: # 오른쪽에서 온 경우 (a에 틈 발생)
            minindex[i][j] = i, j+1
        


utility.printMatrix(table)
x=0
y=0

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y]) # 이전 경로
    (x,y) = minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx]," ", b[ty])
    elif x == tx and y == ty+1:
        print(" - ", " ", b[ty])
    else:
        print(a[tx], " " , " -")