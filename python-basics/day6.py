# nested loops


for i in range(3):
    for j in range(2):
        print(i, j)


print()

# example 2 

for i in [1,2,3]:
    for j in [4,5]:
        print(i, j)



# Task 1 – Print All Pairs
# lst = [1,2,3]

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3


print()

lst = [1,2,3]

for i in lst:
    for j in [1,2,3]:
        print(i,j)

# Task 2 – Print Pair From Two Lists

# output

# 1 3
# 1 4
# 2 3
# 2 4

print()

lst1 = [1,2]
lst2 = [3,4]

for i in lst1:
    for j in lst2:
        print(i,j)

# Task 3 – Star Pattern

# *
# **
# ***
# ****
print()

for i in range(1,5):   # rows
    for j in range(i): # stars
        print("*", end="")
    print()


print()

# task 4 reverse star pattern

for i in range(4,0,-1):
    for j in range(i):
        print("*" , end = "")
    print()


# print number grid 
for i in range(3):
    print(1, 2, 3)



# star

print()

for i in range(1,4):
    for j in range(1,3):
        print(i,j, end="")
    print()

print()


# TRIANGLE pattern

# 1
# 12
# 123
# 1234

print()

for i in range(1,5):
    for i in range(1,i+1):
        print(i, end="")
    print()



# Problem – Count Equal Pairs

# Problem Statement

# You are given a list of numbers.

print()

nums = [1,2,3,1,1,3]
total = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j] and i < j:
            total = total + 1
print(total)

print()

nums1 = [1,3,2,4]
tot = 0 
for i in range(len(nums1)):
    for j in range(i+1,len(nums1)):
        if nums1[i] > nums1[j]:
            tot = tot + 1
print(tot)