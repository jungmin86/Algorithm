# import math
# def interpolationSearch(S, x):
#     low = 0
#     high = len(S) - 1
#     # mid = -1
#     location = -1
#     if S[low] <= x <= S[high]:
#         while low <= high and location == -1:
#             if x < S[low] or x > S[high]:
#                 break
#             denominator = S[high] - S[low]
#             if denominator == 0:
#                 mid = low
#             else:
#                 mid = low + math.floor((x-S[low])*(high-low) / denominator)
#             if x == S[mid]:
#                 location = mid
#             elif x < S[mid]:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#     return location

import math

def robustInterpolationSearch(S, x):
    low = 0
    high = len(S) - 1
    location = -1
    
    if S[low] <= x <= S[high]:
        while low <= high and location == -1:
            gap = math.floor(math.pow(high - low + 1, 1/2))
            if x < S[low] or x > S[high]:
                break
            denominator = S[high] - S[low]
            if denominator == 0:
                mid = low
            else:
                mid = low + math.floor((x - S[low]) * (high - low) / denominator)
            
            
            
            

            if x == S[mid]:
                location = mid
            elif x < S[mid]:
                mid = min(high - gap, max(mid, low + gap))
                
                high = mid - 1  # mid_copy를 사용하여 업데이트
            else:
                mid = min(high - gap, max(mid, low + gap))
                
                low = mid + 1  # mid_copy를 사용하여 업데이트

    return location

S = [1, 3, 4, 7, 8, 11, 13, 15, 16, 20, 22, 25, 29, 30, 33, 36, 37, 39, 41, 43, 45, 48]
x = 11
print(S)
print(f"Location of {x} is {robustInterpolationSearch(S, x)}th")
