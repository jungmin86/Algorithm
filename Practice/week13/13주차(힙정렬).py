import math
class Heap(object):
    n = 0 
    def __init__(self, data):
        self.data = data
        self.n = len(self.data) - 1 # 인덱스 1부터. 2* 연산 가능하게끔
    def addElt(self, elt):
        self.data.append(elt)
        self.n += 1
        self.siftUp(self.n)

    def siftUp(self, i):
        while(i >= 2):
            if(self.data[i] > self.data[math.floor(i/2)]): # 부모의 값보다 크다면 -> 스왑
                temp = self.data[math.floor(i/2)]
                self.data[math.floor(i/2)] = self.data[i]
                self.data[i] = temp 
            i = math.floor(i/2) # i값도 변경
    def siftDown(self, i):
        siftkey = self.data[i]
        parent = i
        spotfound = False
        while 2 * parent <= self.n and not spotfound:
            if 2 * parent < self.n and self.data[2 * parent] < self.data[2 * parent+1]:
                largerChild = 2 * parent + 1
            else:
                largerChild = 2 * parent
            
            if siftkey < self.data[largerChild]:
                self.data[parent] = self.data[largerChild]
                parent = largerChild
            else:
                spotfound = True
        self.data[parent] = siftkey
    def makeHeap2(self):
        for i in range(math.floor(self.n/2), 0, -1):
            self.siftDown(i)
    def root(self):
        keyout = self.data[1]
        self.data[1] = self.data[self.n]
        self.n -= 1
        if self.n > 0:
            self.siftDown(1)
        return keyout
    def removeKeys(self):
        s = []
        for i in range(self.n, 0, -1):
            a = self.root() # 하나씩 빼면서 s에 집어넣는다.
            s.append(a)
        return s
    def makeHeap1(self):
        for i in range(1, self.n + 1):
            self.siftUp(i)
def heapSort(a):
    b = Heap(a)
    b.makeHeap2()
    s = b.removeKeys()
    return s
    
a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap2()
print(b.data)
b.addElt(50)
print(b.data)
s=heapSort(a)
print(s)

a=[0,11,14,2,7,6,3,9,5]
b=Heap(a)
b.makeHeap1()
print(b.data)
s=heapSort(a)
print(s)