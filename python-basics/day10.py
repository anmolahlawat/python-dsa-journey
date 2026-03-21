# hashing 

# task 1
# Print first duplicate

arr = [1,2,2,3]
dic = {}

for num in arr:
    if num in dic:
        print(num)
        break
    else:
        dic[num] = 1

#  Task 2

arr1 = [4,5,6]
x = 5
if x in arr1:
    print(True)

# Task 3
arr2 = [1,1,2,2,3]
s = {}
for i in arr2:   
    if i in s:
        s[i] += 1
    else:
     s[i] = 1
        
print(s)


# tsak 4
# first non repeating number 

arrr = [1,2,2,3,3,4]
k = {}

for i in arrr:
    if i in k:
        k[i] +=1
    else:
        k[i] = 1

for i in arrr:
    if k[i] == 1:
        print(i)
        break

# Task 5 – Intersection of Two Arrays

arr4 = [1,2,2,3]
arr5 = [2,3,4]

s = {}
result = []

# Step 1: store arr4
for num in arr4:
    s[num] = 1

# Step 2: check arr5
for num in arr5:
    if num in s:
        result.append(num)

print(result)