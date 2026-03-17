# Problem: Two Sum (Easy)

nums = [2,7,11,15]
target = 9
otp = []

for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
            otp.append(i)
            otp.append(j)
print(otp)



# pallindrome check 

print()


x = -121

if str(x) == str(x)[::-1]:
    print(True)
else:
    print(False)



#  Question 1480 – Running Sum of 1d Array

print()


nums1 = [1,2,3,4]
total = 0
op = []
for i in nums1:
    total = total + i
    op.append(total)

print(op)


# Question 1920 – Build Array from Permutation

nums2 = [0,2,1,5,3,4]
new = []
for i in range(len(nums2)):
    new.append(nums2[nums2[i]]) 
print(new)