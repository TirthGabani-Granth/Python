# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])
# print(marks[:4]) #List slicing sublist like substring
# print(marks[-3:-1])

# student = ["karan", 95.4, 17, "Delhi"]

# #List Methods
# #adds one element at the end
# list = [2, 1, 3]
# list.append(4)
# print(list.sort()) #for Aescending Order for
# # print(list.sort(reverse=True)) #For Descending Order for
# print(list)

# list = ["banana", "Litchi", "apple"] # Uppercase prefrence first
# print(list.sort()) #also in string in sorting possible same as character
# print(list)

# list = ['a', 'd', 'e', 'f', 'c', 'b']
# # print(list.sort())
# print(list.reverse())
# print(list)

# #insert element at index list.index(idx, el)
# list = [2, 1, 3, 1]
# # list.insert(1, 5)
# # list.remove(1)
# list.pop(2)
# print(list)

#Tuples 
#if we want to inside datatype show tupple so afte string and int value afte(,) comma needed
tup = (1, 2, 3, 2, 2, 4)
print(tup)
print(type(tup))
print(tup[1:3])


#Tuple Methods
#returns index of first occurence
print(tup.index(1)) #tup.index(el)
#counts total occurrence
print(tup.count(2)) #tup.count(el)

#WAP to ask user to enter names of their 3 favorite movies & store them in a list.
# mov1 = input("Enter first movie: ")
# mov2 = input("Enter second movie: ")
# mov3 = input("Enter third movie: ")

# movie_list = [mov1, mov2, mov3]
# print(movie_list)
movies = []
movies.append(input("enter 1 st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rs movie: "))

print(movies)

#WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
list1 = [1, 2, 3]

copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")

# #WAP to count the number of students with the "A" grade in the following tuple.
# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))

#Store the above  values in a list & sort from "A" to "D".("Aescending")
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
