# ✅ Task 1 — Duplicate Exists

arr = [1,2,3,1]
dub = {}

for i in arr:
    if i in dub:
        print(True)
        break
    else:
        dub[i] = 1
else:
    print(False)






# Task 2 — First Unique Element
ar = [2,2,3,4,3]
fu = {}
for i in ar:
    if i in fu:
        fu[i] += 1
    else:
        fu[i] = 1
for i in ar:
    if fu[i] == 1:
        print(i)



#  Task 3 — Count Pairs = Target

arr1 = [1,2,3,4]
target = 5

seen = {}
count = 0

for num in arr1:
    needed = target - num

    if needed in seen:
        count += 1
    
    seen[num] = 1

print(count)