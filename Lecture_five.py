# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)

# i = 1
# while i <= 5:
#     print("apnacollege", i)
#     i += 1

# print("Loop ended")

# #print numbers from 1 to 5
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# print("Loop ended")

# #Print numbers from 1 to 100
# i = 1 #Starting condition
# while i <= 100: #Stoppping condition
#     print(i)
#     i += 1
# print("1 to 100 complete")

# #Print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("100 to 1 complete")

# #print the multiplication table of a number n
# n = int(input("enter nummber : "))
# i = 1 
# while i <= 10:
#     print(n*i)
#     i += 1

# q4
nums = [1, 4 , 9, 16, 25, 36, 49, 64, 81, 100]
heroes = ["ironman", "thor", "superman", "batman"]

#traverse: any list or tuple or dict one on one comping. 
# idx = 0
# # while idx <= len(nums):
# #     print(nums[idx]) #nums[0], nums[1], nums[2]..
# #     idx += 1

i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding..")
        break
    i += 1

# Break & Continue statement in Python
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1
print("end of loop")

i = 0 
while i <= 5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1

#even numbers we want to skip only odd numbers they shows
i = 1
while i <= 10:
    if(i%2 == 0): #[i%2 != 0] give us odd number
        i += 1
        continue #skip
    print(i)
    i += 1 

# for loop
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]

for val in veggies : 
    print(val)

tup =  (1, 2, 3, 4, 2, 8, 9)

for num in tup:
    print(num)

str = "apnacollege"

#else is optional but here if we direct print end then it's print in future else is helpful
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")

#q1  Linear search = search in one line
lis = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49

idx = 0
for num1 in lis:
    if(num1 == x):
        print("number found at idx", idx)
    idx += 1

# range with loop
# seq = range(10)
# print(seq[0])
# print(seq[1])

# for i in range(10): #range(stop)
#     print(i)

# for i in range(2, 10): #range(start, stop)
#     print(i)

for i in range(2, 10, 2): #range(start, stop, step) # Step = ketla thi increase 
    print(i)
 
#print odd numbers
for i in range(1, 100, 2):
    print(i)


#print even numbers
for i in range(2, 101, 2):
    print(i)

#Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

#Print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)

#Print the multiplicaation table of a number n.
n = int(input("enter number : "))

for i in range(1, 11):
    print(n * i)

#pass statement
for i in range(5):
    pass
    
    if i > 5:
        pass
        print("some useful work")

# WAP to find the sum of first n numbers. (using while)
n = 5    #sum = 1 + 2 + 3 + 4 + 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum =", sum)

# WAP to find the factorial of first n numbers.(using for)
# factorial 1 * 2 * 3 * 4 * 5
# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("factorial=", fact)

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i
print("factroial =", fact)