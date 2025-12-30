# class Student:
#     college_name = "ABC College"
#     # name = "anonymous" #class attr
  
#     def __init__(self, name, marks): #contructor is for object initailization if we not create python automatically creates
#         self.name = name #If we want work during making of object and create new attributes which we do in contructor 
#         self.marks = marks
 
#  #class ni ander function hoi ene j apde methods kevi chi
#     def welcome(self): #method in methods we write self this is class function
#         print("welcome student,", self.name)

#     def get_marks(self):
#         return self.marks
    
#     #Two type of constructor
# #In constructor first parameter is self and then we can take different parameter also

#     # #defualt constructor 
#     # def __init__(self):
#     #     pass

#     # #parameterized constructor
#     # def __init__(self, name, marks):
#     #     self.name = name #obj attr > class attr
#     #     self.marks = marks
#     #     print("adding new student in Database..")

# s1 = Student("karan", 97)
# s1.welcome()
# print(s1.get_marks())

# # print(s1.name, s1.marks) #karan

# # s2 = Student("arjun", 88)
# # print(s2.name, s2.marks)

# # print(s2.college_name)
# # print(Student.college_name)

#   # #defualt constructor
#     # def __init__(self):
#     #     pass

# # print(s1.name)

# # s2 = Student()
# # print(s2.name)

# # class Car:
# #     color = "blue"
# #     brand = "mercedes"

# # car1 = Car()
# # print(car1.color)
# # print(car1.brand)

# #Class & Instance atrributes
# #Methods

# class Student:
#       def __init__(self, name, marks):
#           self.name = name
#           self.marks = marks
        
#       def get_avg(self):
#           sum = 0
#           for val in self.marks:
#               sum += val
#           print("hi", self.name, "your avg score is:", sum/3)

# s1 = Student("tony stark", [99, 98, 97])
# s1.get_avg()

# s1.name = "ironman"
# s1.get_avg()

# #Static Methods


#OOP in Python
#1) Abstraction
#Hiding the implementation details of aa class and only showing the essential features to the user.
class Car: #unnecesary details it's hide
    def __init__(self):  # this all class so it's only give result backend we hide
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

#2) Encapsulation
#Wrapping data and function into a single unit(object).
#capsule of two [data + funnction] we use till now example of methods class attributes which all is encapsulation

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "wad debited")
        print("total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)

# Del keyword
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("shradha")
print(s1.name)
del s1.name
print(s1.name)