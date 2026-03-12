# functions basics 


def greet():
    print("hello world")

greet()

# function with parameters



def name(name):
    print("hello", name)

name("aman")
name("anmol")



# function returning values 

def add(a,b):
    return a+b

sum = add(5,12)
print(sum)





# string basics 


name = "anmol"

print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])



# list operations


lst3 = [1,2,3,4,5]

lst3.append(99)


print(lst3)

# pop remome by index 
# removes 3 
lst3.pop(lst3[1])

print(lst3)

lst3.pop(1)
print(lst3)

# reove elemnt by value

lst3.remove(1)
print(lst3)


# simple practice problem 


# greeting function

def greet(name):
    print("hello", name)

greet("anmol")


# print all even numbers from 1 to 20




for i in range(1,21):
    if i % 2 == 0:
        print(i)
    


# sum of list [ 5 ,10 ,15, 20]

lst4 = [5,10,15,20]
total  = 0

for i in lst4:
    total = total + i
print(total)

