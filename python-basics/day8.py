#  Question 136 – Single Number


nums = [4,1,2,1,2,4,3]

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1
    
    if count == 1:
        print(nums[i])


print()

# Problem 121

# 🔢 Best Time to Buy and Sell Stock (LeetCode #121)


prices = [7,1,5,3,6,4]
profit = 0 

for i in range(len(prices)):
    for j in range(i+1 ,len(prices)):

        pr = prices[j] - prices[i]


        if pr > profit:
            profit = pr
print(profit)
        
    

