# 1. 순차검색 알고리즘
def seqsearch(s,x):
    index = -1
    for i in range(len(s)):
        if x == s[i]:
            index = i # break가 없으니 중복된 것 있으면 맨 마지막
    return index


s=[3,5,2,1,7,9]
loc = seqsearch(s,3)
print("1. 순차검색 알고리즘")
print(loc)

#2. 배열의 수 더하기
print("2. 배열의 수 더하기")
def sum1(s):
    result = 0
    for a in s:
        result += a
    return result
s = [3,5,2,1,7,9]
answer = sum1(s)
print(answer)


# 3. 교환정렬
s=[3,2,5,7,1,9,4,6,8]
n = len(s)
for i in range(0,n-1):
    for j in range(i+1, n):
        if s[i] > s[j]:
            s[i], s[j] = s[j], s[i]
print("3. 교환정렬")
print(s)

#4. 행렬곱셈
def matrix_multiplication(a,b):
    result = [[0] * len(a) for _ in range(len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i][j] = 0
            for k in range(len(a)):
                result[i][j] += a[i][k] * b[k][j]
    return result

a  = [[1,2], [3,4]]
b = [[4,1], [1,0]]
print(matrix_multiplication(a,b))

# 피보나치 수열
def fib1(n): #위에서부터 아래로 -> 트리구조 -> 반복계산 개많다 (오래걸림)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
    
def fib2(n):
    result = [0] * (n+1)
    if (n > 0):
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i-1] + result[i-2]
    
    return result[n]
print("피보나치")
print(fib2(10))
