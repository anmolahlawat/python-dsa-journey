#  two pointers 
# ✅ Task 1 – Print Unique Elements
arr = [1,1,2,2,3]
i = 0 
for j in range(i+1,len(arr)):
    if arr[j] != arr[i]:
        i = i+1
        arr[i] = arr[j]

print(arr[:i+1])

print()

# Task 2 – Count Unique Elements
arrr = [1,1,2,3,3,4,5]
i = 0
for j in range(i+1, len(arrr)):
    if arrr[j] != arrr[i]:
        i = i+1
print(i)
print()


# Task 3 – Store Unique Elements
ar1 = [1,1,2,2,3]
ar2 = [ar1[0]]
i = 0
for j in range(1,len(ar1)):
    if ar1[j] != ar1[i]:
        i = i+1
        ar1[i] = ar1[j]
        ar2.append(ar1[i]) 
print(ar2)
print()

# LeetCode #26 – Remove Duplicates from Sorted Array

ar = [1,1,2]
i = 0
for j in range(len(ar)):
    if ar[j] != ar[i]:
        i = i+1
        ar[i] = ar[j]
print(ar[:i+1])