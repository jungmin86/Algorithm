import math

a = 4.90938e-07

max_n = 0

n = 80000
while True:
    n_log_n = n * math.log2(n)
    
    left_side = 60
    
    if left_side >= a * n_log_n:
        max_n = n
    else:
        break
    
    n += 1

print("자연수 n의 최댓값:", max_n)
