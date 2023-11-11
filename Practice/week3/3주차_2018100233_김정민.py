# 1. 이분검색 -> 정렬이 돼있어야 찾을 수 있다.

# def bs(data, item, low, high):
#     if low > high: # 없는 값을 찾다보면 이런 순간이 옴
#         return -1
#     mid_point = (low + high) // 2 #소수점 이하 버리고 정수만 (몫)
#     if item == data[mid_point]: 
#         return mid_point
#     elif item > data[mid_point]: # 2개 중 하나로 감 -> 연산 횟수 반으로 줄어듦 (로그)
#         return bs(data, item, mid_point+1, high)
#     else:
#         return bs(data, item, low, mid_point-1)    
def bs(data, item, low, high):
    while low <= high:
        mid_point = (low + high) // 2
        if item == data[mid_point]:
            return mid_point
        elif item > data[mid_point]:
            low = mid_point + 1
        else:
            high = mid_point - 1
    return -1



data=[1,3,5,6,7,9,10,14,17,19] 
n=10 
location=bs(data,14,0,n-1) 
print("1. 이분검색")
print(location)



# 2. 합병정렬1
def mergeSort(n, s):
    """
    n: 데이터 길이
    s: 데이터
    """
    if n > 1:
        h = n // 2
        m = n - h
        u = s[:h] # 앞쪽
        v = s[h:] # 뒷쪽
        mergeSort(h, u)  
        mergeSort(m, v)  
        merge(h, m, u, v, s)  

def merge(h,m,u,v,s):
    i = 0
    j = 0
    k = 0
    while i < h and j < m:
        if u[i] < v[j]:
            s[k] = u[i] # 더 작은 것 먼저 넣으면서 합병
            i += 1 # 합병된 인덱스만 증가
        else:
            s[k] = v[j]
            j += 1
        k += 1 # 반복문 돌 때마다 k는 1씩 증가
    while i < h: # j가 먼저 m에 도달해서 s에 합병할 게 남아있는 경우
        s[k] = u[i]
        i += 1
        k += 1

    while j < m:
        s[k] = v[j]
        j += 1
        k += 1


s=[3,5,2,9,10,14,4,8]
mergeSort(8,s)
print("2. 합병정렬1")
print(s)

# 3. 합병정렬2 (추가로 해보기)
def mergeSort2(s, low, high):
    if low < high:
        mid_point = (low + high) // 2
        mergeSort2(s, low, mid_point)
        mergeSort2(s, mid_point + 1, high)
        merge2(s, low, mid_point, high)

def merge2(s, low, mid, high):
    i = low
    j = mid + 1
    k = low #u에 들어갈 인덱스
    u = [0] * (high + 1)  # 개수니까 high + 1

    while i <= mid and j <= high:
        if s[i] < s[j]:
            u[k] = s[i]
            i += 1
        else:
            u[k] = s[j]
            j += 1
        k += 1

    while i <= mid: # 하위 반복문과 둘 중 하나만 실행됨
        u[k] = s[i]
        i += 1
        k += 1

    while j <= high:
        u[k] = s[j]
        j += 1
        k += 1

    for a in range(low, high + 1):
        s[a] = u[a] # u에다가 결과를 만들고 마지막에 복사해줌
    


s=[3,5,2,9,10,14,4,8]
mergeSort2(s,0,7) 
print("3. 합병정렬2")
print(s)

# 합병정렬3 (recursion X)
def mergeSort3(s):
    n = len(s)
    size = 1
    while size < n:
        for low in range(0, n, 2 * size):
            mid = low + size
            high = min(low + 2 * size, n)
            merge3(s, low, mid, high)
        size *= 2

def merge3(s, low, mid, high):
    i = low
    j = mid
    u = []
    while i < mid and j < high:
        if s[i] < s[j]:
            u.append(s[i])
            i += 1
        else:
            u.append(s[j])
            j += 1
    while i < mid:
        u.append(s[i])
        i += 1
    while j < high:
        u.append(s[j])
        j += 1
    for k in range(low, high):
        s[k] = u[k - low]

s = [3, 5, 2, 9, 10, 14, 4, 8]
mergeSort3(s)
print("4. 합병정렬3")
print(s)