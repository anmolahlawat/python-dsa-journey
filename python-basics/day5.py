# Task 1 – Count Odd Numbers

# Count how many odd numbers are in the list.


lst = [3,6,1,8,5,10]
num = 0

for i in lst:
    if i % 2 != 0:
        num = num+1
print(num)



# Task 2 – Print Numbers Greater Than 7

lst1 = [4,8,2,9,1,7]
for i in lst1:
    if i > 7:
        print(i)


# Task 3 – Square Each Number

lst2 = [1,2,3,4]
sq_lst = []

for i in lst2:
    i = i**2         # we can also use i = i*i
    sq_lst.append(i)
print(sq_lst)


# Task 4 – Sum of Even Numbers

lst3 = [1,2,3,4,5,6]
total = 0
for i in lst3:
    if i % 2 == 0:
        total = total + i
print(total)


# Task 5 – Reverse a List (Important)

# Without using .reverse().

lst4 = [1,2,3,4]
print(lst4[::-1])
# using loop



lst5 = [1,2,3,4]
rev = []

for i in range(len(lst5)-1, -1, -1):
    rev.append(lst5[i])

print(rev)