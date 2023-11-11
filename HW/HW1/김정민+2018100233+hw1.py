import time
import random

def selection_sort(rl): #비내림차순 >= 오름차순
    length = len(rl)
    for i in range(length):
        min_index = i # 바꿀 위치 (기준)
        for j in range(i + 1, length): 
            if rl[j] < rl[min_index]: # 더 작은 것이 있나 확인
                min_index = j
        rl[i], rl[min_index] = rl[min_index], rl[i] #swap


rl = [3, 9, 4, 9, 6, 1, 2, 7, 10, 8, 5] # random list
selection_sort(rl)
print(rl)


def merge_sort(rl2):
    length = len(rl2)
    if length < 2:
        return rl2
    mid = length // 2 # 중간지점
    left = merge_sort(rl2[:mid]) # 2개 미만이 될 때까지 쪼개기
    right = merge_sort(rl2[mid:])

    merged_rl2 = []
    i = 0 #초기화
    j = 0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            merged_rl2.append(left[i]) # 양쪽 블럭에서 더 작은 것을 먼저 넣기
            i += 1 #다음 것 비교
        else:
            merged_rl2.append(right[j])
            j += 1
    merged_rl2 += left[i:]
    merged_rl2 += right[j:]
    for i in range(length): # rl2도 바꿔주기
        rl2[i] = merged_rl2[i]
    return merged_rl2


rl2 = [3, 9, 4, 9, 6, 1, 2, 7, 10, 8, 5] # random list (mutable)
merge_sort(rl2)
print(rl2)

def time_check(size):
    if size == 80000:
        rl = [random.randint(1, 1000) for x in range(size)]
        rl1 = rl.copy()
        start_time = time.time()
        merge_sort(rl1)  
        end_time = time.time()
        time_B = end_time - start_time
        print(f"{size}, A, B\n{size}, X, {time_B:.5f}")
        pass
    rl = [random.randint(1, 1000) for x in range(size)]
    rl1 = rl.copy()
    rl2 = rl.copy()
    start_time = time.time()
    selection_sort(rl1)  
    end_time = time.time()
    time_A = end_time - start_time

    start_time = time.time()
    merge_sort(rl2)  
    end_time = time.time()
    time_B = end_time - start_time

    print(f"{size}, A, B\n{size}, {time_A:.5f}, {time_B:.5f}")

time_check(5000)
time_check(10000)