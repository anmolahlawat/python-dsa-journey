# sliding window
 
# arr = [1,2,3,4]
# k=2
# window_sum = sum(arr[:k])

# for i in range(k,len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     print(window_sum)



# Task 1 — Max Sum Subarray of Size K
arr = [2,1,5,1,3,2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum   # first window considered

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    
    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)
    

#  Task 2 — First Window Sum
arr1 = [1,4,2,10]
l = 2

wind_sum = sum(arr1[:l])
print(wind_sum)

for i in range(l , len(arr1)):
    wind_sum = wind_sum - arr1[i-l] + arr1[i]
    print(wind_sum) 
