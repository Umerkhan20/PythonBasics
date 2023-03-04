# input in python
# name=input("What's your name? ")
# print ("Hello "+name)

# input conversion
# birth_year=input("What's your birth year: ")
# age=2023-int(birth_year)
# print ("Age is " )
# print(age)

# basic calculator code :
# value1=input("Enter value 1: ")
# value2=input("Enter value 2: ")
# sum=(int(value1)+float(value2))
# print("sum" + str(sum))

# multiple string
# course='''
# HI
# MY name is umer
# and i am ur abu
# '''
# print(course)

# objects by strings
# intro='my name is umer khan'
# print( intro.capitalize())

# in operator returns true/false
# intro='my name is umer khan'
# print('name'in intro)

# some arithmetic operations but there are many
# x=27
# x+=4
# y=73
# y-=4
# z=22
# z%=4
# print(x,y,z)

# operator precedence same as C/C++ as DMAS and bracket rule
# x=2*4+6
# print("value of x "+str(x))
# y=(2+6)/10
# print("value of y "+str(y))

# comparison operator same as C/C++ as there are many but we did two
# x=2>1
# print(x)
# y=2!=2
# print(y)

# logical rule same as C/C++ as there are and or not
# price=30
# print(price>25 and price >40)

# umer=20
# print(umer>21 or umer<23)

# shaka=54
# print( not shaka >43)

# if else else if statements
# temprature=input("Enter temprature: ")
# float(temprature)
# if float(temprature)>45:
#     print("It is hot")
# elif float(temprature)<20:
#     print("temprature is pleasent")
# else:
#     print("not hot")

# is_hot=False
# is_cold=False
# if(is_hot):
#     print("Drink water")
#     print("Stay Safe")
# elif(is_cold):
#     print("Weather is pleasent")
# else:
#     print("Its ok")

# exercise:
# weight=input('Enter weight: ')
# float(weight)
# demand=input("KG OR LBS ")
# if (demand.upper()=='K'):
#     float(weight)*0.453592
#     print("Weight in kgs is "+ str(float(weight)*0.453592))
# elif(demand.upper()=='L'):
#     print("weight in Lbs is "+ str(float(weight)/0.45))

# while loop:
# i=1
# while(i<=4):
#     print(i)
#     i=i+1

# lists in python:
# names=["Umer","Khan","Saad","Hamza","32"]
# names[1]="khn" #changing list value after list declaration
# print(names)

# list_number=[1,2,3,4,5,7]
# print (min(list_number))

# range of values in lists:
# names=["Umer","Khan","Saad","Hamza","32"]
# names[1]="khn" #changing list value after list declaration
# print(names[0:3])

# name='jenifer'
# print(name[1:-1])

# sorting lists
# numbers=[0,1,5,2,3,6,8,7]
# numbers.sort()
# print(numbers)

# formatted strings:
# first=input("Enter first name: ")
# last=input("Enter last name: ")
# final=f'{first} {last} welcome'
# print(final)

# play with strings
# name='Umer Khan'
# print(len(name))
# print(name.capitalize())
# print(name.count(name))
# print(name.find('e'))
# print(name.replace('e',str(2)))
# print(name.upper())
# print(name.lower())

# round functions:
# x=2.6
# print(round(x))
# # abs = absolute always return +value
# print(abs (-3.2))
# import math
# print(math.ceil(20.6))

# exercise:
# price=10000000
# is_goodcredit=True
# if(is_goodcredit):
#     downpayment=0.1*price
#     print("Downpayment has been given "+ str(downpayment))
# else:
#     downpayment=0.2*price
#     print("Downpayment has been given "+ str(downpayment))

# guess game:
# secret_no=7
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     user_no=input("Enter number to guess (range : 0-10) You only have 3 chances: ")
#     guess_count+=1
#     if user_no==str(secret_no):
#         print("You won !")
#         break
#     else:
#         print("You failed ! Try again : ")
   
  # car game:
# command=""
# started=False
# while command.upper()!="QUIT":
#     command=input("enter value > ".upper())
#     if command.upper()=='START':
#             if started:
#                   print("Car is already started ")
#             else:
#                   started=True
#                   print("Car started ")
#     elif command.upper()=='STOP':
#             if  not started:
#                print("Car is already stopped")
#             else:
#                 started=False
#                 print("Car stopped")
#     elif command.upper()=='HELP':
#         print("""
#           Press start to Start the Car
#           press stop to stop stop the car
#           press quit to quit the car
#         """)
#     elif command.upper()=='QUIT':
#             print("You quit the game ")
#             break
#     else:
#           print("Oh i did'nt recognize any value")
#           break

 
# for loop
# for names in ['umer','khan','hello','muneeba','saad']:
#    print(names)
        
# for numbers in range(12):
#    print(numbers)

# prices=[10,40,32]
# total=0
# for price in prices:
#    total += price
#    print(f"Total: {total}") 

# no=[1,1,1,1,5]
# for l_count in no:
#     print('L'*l_count)


# 2D lists:
matrix=[
    [0,1,2],
    [1,4,3],
    [2,3,5]
]
# matrix[1][1]=40
# print(matrix[1][1])
# for rows in matrix:
#     for items in rows:
#         print(items)

# play with lists:
# numbers=[1,4,3,2,5]
# numbers2=numbers.copy()
# numbers.remove(23)
# print(numbers2)

# unpacking
# coordinates=(1,2,4,)
# x,y,z=coordinates
# print(x,y,z)

# dictionary
# personal_info={
#     "name":"Umer Khan",
#     "age":20,
#     "profession":"Software engineer"
# }
# personal_info["birthdate"]="july 1 2002"
# print("Name is "+personal_info.get("name")+" and Age is "+str(personal_info.get("age"))+ " Whereas profession is "+personal_info.get("profession"))
# print(personal_info["birthdate"])

# exercise:
# phone=input("Enter phone no: ")
# digits={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine",
# }
# output=""
# for ch in phone:
#     output="digits are : " + digits.get(ch,"!") +" "
#     print(output)

# emoji convertor:

# functions
# def emoji_convertor(message):
#   words=message.split(' ')
#   emojis={
#     ":)":"😊",
#     "(:":"😌"
#   }
#   output=""
#   for word in words:
#    output+=emojis.get(word,word)+" "
#   return output


# message=input("Enter message: ")
# print(emoji_convertor(message))

# functions in python:
# def sum_fun(value1,value2):
#     sum=0
#     sum=  value1+value2
#     print(f'Sum will be : "{sum}')

# print("Start")
# sum_fun(12,34) 

# exception in python:
# try:
#     name=input("Enter the name: ")
#     age=int(input("Enter age: "))
#     print(f'Name is {name} and Age is {age}')
# except ValueError:
#     print("Invalid statement")

# classes in python:
# class person:
#     #  constructor:
#      def __init__(self,name) : 
#         self.name=name
#      def talk(self):
#         print(f'Hi ! I am {self.name}')

# p1=person("Umer Khan")
# p2=person("ALI")
# p1.talk()
# p2.talk()
       
# from  convertors import kgs_to_lbs
# kgs_to_lbs(27)  
   
# dice game:
import random
class Dice:
    def roll(self):
       first = random.randint (1, 6)
       second= random.randint  (1, 6)
       return first,second
    

d1=Dice()
print(d1.roll())
    