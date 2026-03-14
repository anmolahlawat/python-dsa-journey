# accessing list with index number

lst = [1,2,3,4,50]
for i in range(len(lst)):
    print(lst[i])



# task 1
# print odd numebr 
lst1 = [3,6,1,8,5,10] 

for i in lst1:
    if i % 2 != 0:
        print(i)
 

# task 2
# sum of list

lst2 = [5,10,15,20]

sum = 0 
for i in lst2:
    sum = sum+i
print(sum)



# task 3
# find the smallest number 

lst3 = [4,7,2,9,1]
small = lst3[0]

for i in lst3:
    if i < small:
        small= i
print(small)


# Task 4 – Count Numbers Greater Than 5
lst4 = [3,6,9,2,7,1]
num = 0
for i in lst4:
    if i > 5:
        num= num + 1
print(num)

# leetcode style problem

# [1,2,3,4] - input

# [1,3,6,10] - output



ls = [1,2,3,4]
add = 0
store = []
for i in ls:
    add = add + i
    store.append(add)
print(store)



# task 5 - each number is double of each other 
# nums = [2,5,1,8]


nums = [2,5,1,8]
double_list = []
for i in nums:
    i = i*2
    double_list.append(i)
print(double_list)




# Task 6 – Find the Largest Number

nums1 = [4,7,2,9,1]
largest = nums1[0]
for i in nums1:
    if i > largest:
        largest = i
print(largest)


# Task 7 – Find the second Largest Number

nums2 = [4,7,2,9,1]
largest = nums2[0]
second = nums2[0]

for i in nums2:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print(second)