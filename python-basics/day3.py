# while loop

i = 1
while i <=5:
    print(i)
    i = i+1


# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue


for i in range(11):
    if i == 5:
        continue
    print(i)


#  list slicing


lst = [10,20,30,40,50]


print(lst[0:3])
print(lst[:6])
print(lst[::-1])

lst1 = [10,20,30,40,50,60,70,80,90,100]
print(lst1[::3])




# practice


# Task 1
# Print numbers 1 to 10 using a while loop.

i = 0

while i < 101:
    i = i+1
    print(i)

# Task 2
# Print odd numbers from 1 to 20.

for i in range(21):
    if i % 2 == 0:
        print(i)


# Task 3
# Given list
# [4,7,2,9,1]
# Find the largest number without using max().

lst3 = [4,7,2,9,1]
largest = lst3[0]
for i in lst3:
    if i > largest:
        largest = i
print(largest)



# mini task
# Count even numbers in a list.

# Example: lst = [1,4,6,3,9,10]
# output = 3


lst4 = [1,4,6,3,9,10]
even_num = 0

for i in lst4:
    if i % 2 == 0:
        even_num = even_num+1
print(even_num)