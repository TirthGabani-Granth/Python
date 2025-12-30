#Dictionary in python
info = {
    "subjects" : ["python", "c", "Java"],
    "topics" : ("dict", "set"),
    "key" : "value",
    "name" : "apnacollege",
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4
}

print(type(info))
print(info["topics"])
print(info["subjects"])
print(info["name"])
info["name"] = "shradha"
info["name"] = 23 #overwrite
info["surname"] = "khapra"
print(info)

null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)

#Nested Dictionaries
student = {
    "name": "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student["subjects"]["chem"])
#Dictionary Method
print(len(list(student.keys())))
print(list(student.values()))
print(len(list(student.values())))

pairs = (list(student.items()))
print(pairs[0])

print(student["name"]) #error
print(student.get("name2")) #no error -> None

new_dict = {"city" : "delhi", "age": 16}
student.update(new_dict)
print(student)

#Set in Python
collection1 = {1, 2, 3, 4, "hello", "world"}
#if we repeat value then set removes the duplicate values.
print(collection1)
print(type(collection1))
print(len(collection1)) #totall number of items

collection = set() #empty dictionary; syntax
print(type(collection))

# Set Methods
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add((1, 2, 3))
# collection.add([1, 2, 3]) #unhashable value immutable -> hash value 1  1 same value hashable value not change  change then no problem like tuple
#unhashable -> dict, lists, sets
# collection.clear() it's clear sets elements
print(collection.pop())
print(collection.pop())
print(len(collection))

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #(1, 2, 3, 4)
print(set1.intersection(set2)) #{2,3} common element leave and show


dict = {
    "table" : ["a pieace of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dict)

setclass = {"python", "java", "c++", "Js", "python", "java", "python", "java", "c++", "c"}
print(len(setclass))

marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)

# values = {9, "9.0"} # In python 9 and 9.0 same so we store as string so we can access
# print(values)

values = { # this two possible solution to store this value pne is this pair store in tuple.
    ("float", 9.0),
    ("int", 9)
}
print(values)