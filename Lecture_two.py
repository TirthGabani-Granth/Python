#str1 = 'first way to write sring'
#str2 = "second way to write sring"
#str3 = """third way to write sring"""
#"""why this cause when we use this second's so second after single quot take as first half string where sing their double use where double their single"""

#str1 = "This is a string.\nwe are creating it in python."
#print(str1)

str1 ="apna"
len1 = len(str1)
print(len1)

str2 ="college"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2 # In lenght count space & special charecter also
print(final_str)
print(len(final_str))
# Indexing
print(str1[3])
print(str1[1])
print(str1[0:2])
print(str1[:2])# [0:2] python automatically takes this
print(str1[2:])# [5:len(str)]
print(str1[-4:-1])

str = 'I am studying python from ApnaCollege'
print(str.endswith("ege"))
#str = print(str.capitalize())
#print(str)
print(str.replace("python", "javascript"))
print(str.find("o")) #first time exist word or character index we get o = 18
print(str.find("q")) #for not exiting value for it's shows -1


# name = input ("enter your name :")
# print("length of your name is", len(name))

# str = "Hi, $Iam the $ symbol $99.99"
# print(str.count("$"))

light = "yellow"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")
print("end of code")

num = 5 # # both condition true but why it's shows first cause in elif it's show only one.

if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")

# age = 14

# if(age >= 18):
#     print("can vote") #identation = proper spacing
# else:
#     print("CANNOT vote")

marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print ("grade of the student ->", grade)

#nesting
age = 95

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

# WAP to check if a number entered by the user is odd or even.
num = int(input("enter number:  "))

if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

# WAP to find greater of 3 numbers entered by the user.
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if(a >=b and a >=c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("thirs is largest",c)

# WAP to find the largest of 4 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("First number is largest:", a)
elif b >= a and b >= c and b >= d:
    print("Second number is largest:", b)
elif c >= a and c >= b and c >= d:
    print("Third number is largest:", c)
else:
    print("Fourth number is largest:", d)

# WAP to check if a number is a multiple of 7 or not.
x = int(input("enter number: "))

if(x % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple")