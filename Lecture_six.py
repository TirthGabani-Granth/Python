# #function definition
# def calc_sum(a, b): #parameters
#     return a + b #return function return value which we store in any variable it's gives output and we can print also

# sum = calc_sum(1, 2) #function call; or (1, 2) called arguments
# print(sum)

# #it's print hello
# def print_hello(): # why function use cause redundancy decrease that's why we can use function so less code work more.
#     print("hello")

# print_hello()
# #which function not return anuthing so output we get is none value.
# output = print_hello()
# print(output) #None

# #average of 3 number
# def calc_avg(a, b, c): # we can add loop, if elif else but with proper identation(spacing)
#    sum = a + b + c
#    avg = sum / 3
#    print(avg)
#    return avg

# calc_avg(98, 97, 95)

# #Types of function
# # 1) built in function

# #print is also function ther have different proprty also
# print("apnacollege", end="$") #sep = "" defult proprty
# print("shradhakhapra") #end = "\n"
# # len()
# # range()

# # 2) User defined functions
# # which function who program by we programmer so it's user defined function

# #Default Parameters
# #Assigning a defualt value to parameter, which is used when no argument is passes.
# def cal_prod(a, b=1): #we add 1 so it's by defult assume this arguments.
#     print(a * b) #we can do single value as defualt
#     return a * b #But in in single value  in second parameter only possible cause first we do then it's both take by defult first so error occur.
# #when we give defualt value we prfer last to give value
# cal_prod(1)

# qs1
cities = ["delhi", "gurgaon", "noida", "pune", "mumabai", "chennai"]
heroes = ["thor", "ironmn", "captain america", "shaktiman"]
fruits = ["apple", "banana", "litchi"]

def print_len(list): #Means we can print any list length cause we add directly list that's why
    print(len(list))

print_len(cities)
print_len(heroes)
print_len(fruits)

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)
print_list(heroes) #triling character but here we can ignore
print_list(fruits)
print()

#q3 
n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)

# q4
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(73)

# q5
def odd_num(n):
    """Return 'EVEN' if n is even, otherwise 'ODD'. Expect n to be an integer."""
    if n % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


print(odd_num(3))

#Recursion
#prints n to 1 backwards
#recursive function
def show(n):
    if(n == 0): # Base case 
        return 
    print(n)
    show(n-1)
    print("END")

show(3)

#returns n!  [n! = (n-1)! x n this is recurrence relation]
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(6))

#write a recursive function to calculate the sum of first n natrual numbers
def cal_sum(n): # so we can caalculate 1 to any number sum calculate.
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(10)
print(sum)

#write a recursive funnction to print all elements in a list
#hint : use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "banana", "litchi"]

print_list(fruits)