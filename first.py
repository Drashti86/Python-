#how to declare variables and how to store value and how to print

# print("Hello Word")
# name  = "Java"
# age = 23

# name = "Drashti"
# age = 43.89

# is_adualt = True
# print(is_adualt)
# print(age)
# print(name)

# first exersize
# first_name = "patoliya"
# Last_name = "Drashti"
# age = 51
# is_a_genius = Trueh
# print(first_name)
# print(Last_name)
# print(age)
# print(is_a_genius)

#how to take a input from a user
# name  = input("what is your name !.")
# #how to concate string
# print("HEllo " + name)
#exersize
# name = input("what is your father name : ")
# print("my father name is a " + name)

#type conversion
# old_age = input("enter the age : ")
# new_age = int(old_age) + 2 #old age take as a string not a avriable thatwhy i convert into a integer
# print("New one is " + str(new_age))

# we can conversion into four types : 
#primitive data types is int,flot,string etc.
# float()
# str()
# int()
# bool()

# when we take integer value thna and that not take as a intger that take as a string
# first = input("enter the first number : ")
# second = input("enter the second number : ")
# sum = int(first) + int(second) # first + second this is a out as a string 
# print("sum of the variable is : " + str(sum))

#strings in python
# we can replace the entier string
#original string not replace 
# we can replace with characters
#in this string position or index strat with a 0
#return -1 

# name = "Java Python"
# # methods
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.find('P'))  
# print(name.find('p'))
# print(name.find("Java"))
# print(name.replace("Java Python", "c and c++")) 

# check the string is a exist or not in the actual string usin in keyword
# print('P' in name) # exits = truev, not exits = false
# print('Q' in name)
# print('Java' in name)
# print('java' in name)

# arithmetic operators
# opertor like +,-,/,%,**,(rimider or modulo),==,*,
# // ( this is not take value after decimal point only take a integer value)
# >,<,<=,>=,!=
# print(5 + 2)
# print(5 - 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 == 2) # return boolean value
# print(5 ** 2) #5 to the power 2 = 25

#conditional operator
# print(5 > 2)
# print(5 < 2)
# print(5 <= 2)
# print(5 >= 2)
# print(5 != 2)  #not qeual

#logical operator (or, and, not)
# print(2 > 3 or 2 > 1) # ans is true, only one condition true then conditions becomes true
# print(2 > 3 and 2 > 6) # ans is false,both condition true then condition becomes true otherwise false
# print(not 2 > 3) # true becomes false and false becomes true

#operations sortcut
# i = 5
# i = i + 5
# i += 5
# i -= 5
# i *= 2

#operator precedence = (*,/,+) (which operator would be first operate)
# results  = 2 + 3 + 4 * 9 # ans is 41 
# print(results) 

#comments strat with a  " # "

#if else condition
# if is a keywor 
# elif is a keyword
# else is a keyword
# age  = 5
# if age >= 18:  
#     print("you are an adult")
#     print("you can vote")
# elif age < 18 and age > 3: 
#     print("you are in school")
# else:   
#     print("you are a kid")
    
# print("this is a leader of if else")

#exersize
# make a calculater
# first = input("enter the first number : ")
# operator = input("enter the operator (+, -, /, %, *) : ")
# second = input("enter the second number : ")
# first = int(first)
# second = int(second)

# if operator == "+":
#     print(first + second)  
# elif operator == "-":
#     print(first - second)
# elif operator == "%":
#     print(first % second)    
# elif operator == "/":
#     print(first / second)
# elif operator == "*":
#     print(first * second)
# else:
#     print("INVALID")

# range store numbers range is a keyword or a function
# numbers = range(5) # length
# print(numbers)

#loops

#1.While Loop
# i = 1
# while i <= 5:
#     print(i * "*")
#     i = i + 1 

#output is :
# *
# **
# ***
# ****
# *****
    
# i = 5
# while i >= 0:
#     print(i * "*")
#     i = i - 1 

#output is : 
# *****
# ****
# ***
# **
# *
# i = i + 1 also write i+=1
#not write infinite loop i = i + 1 this is a required line for itrate
#number multiplai by string that means print that time string  like this  print(i * "*")

# 2. for loop object or take a seqance of items using for loop

# for items in range(5):
#     print(items + 1)

#list in pythom - collection of items or data types
# marks = [95,76,89,98,"Maths"]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[-1]) # take a value of index from last side
# print(marks[-2])
# print(marks[-3])
# print(marks[-4])
# print(marks[0:3]) # 0 ,1,2 include 3 is not include 
# for score in marks:
#     print(score)
    
# marks list store in score

#operations
# marks = [95,76,89,98,"Maths"]
# marks.append(99) #insert in last
# print(marks)
# marks.insert(3,2)  #insert at specific position
# print(2 in marks) # 2 is exits or not check using this line
# print(len(marks)) #print length

# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1
    
# marks.clear() # we can clear the list
# print(marks)
# for loop
# marks = [95,76,89,98,"Maths"]
# for score in marks:
#     print(score)

#sets in python set is a store uniqe value
# marks = {1,2,3,4,5,7,7}

# for m in marks:
#     print (m)

#dictonary : key and value
# marks = {"eng" : 56,"chemistry" : 90}
# marks["loop"] = 90
# print(marks)
# marks["eng"] = 90
# print(marks)

#functions:-->

# //1.in-bult fucntion = int(),str(),bool(),etc..
# //2.module function = releted function and releted variables store in one file = 
# //3.user-defined function

# import math 
# print(dir(math))

# from math import sqrt
# print(sqrt(16))


# from math import *
# print(sqrt(16))

# def print_sum(first,second):
#     print(first + second)

# print_sum(1,2)



def print_sum(first,second = 8): # defualt para
    print(first + second)

print_sum(1)