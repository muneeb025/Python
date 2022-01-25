from datetime import datetime
import json
import time
import os
books_dic = {1:"English", 2:"Maths", 3:"Islamiat", 4:"Pakistan studies", 5:"physics"}
manue={1:"Issue book", 2:"Return book", 3: "List of issued book", 4: "Exit"}
userbooks = {}

def showmanue():
    for key, value in manue.items():
        print(key, value)

def listofbooks():
    for key, value in books_dic.items():
            print(key,value)

def userissuedbooks():
    print("List of Issued books")
    for key, value in userbooks.items():
        print(key, value)

def filewrite():
    with open(user_name, "w") as f:
        json.dump(userbooks, f)

def fileopen():
    with open(user_name) as f:
        userbooks=json.load(f)
    return userbooks

def issuebook():
    count2 = True
    while(count2):
        if len(userbooks)==3:
            print("you only issued 3 books at a time")
            break
        print("List of available books")
        listofbooks()
        userInput2=int(input("select your book "))
        if(userInput2==1):
            userbooks[1] = books_dic[1]
            recordtime = time.time()
        elif(userInput2==2):
            userbooks[2] = books_dic[2]
        elif(userInput2==3):
            userbooks[3] = books_dic[3]
        elif(userInput2==4):
             userbooks[4] = books_dic[4]
        elif(userInput2==5):
            userbooks[5] = books_dic[5]
        userInput3=int(input("Press 1 for select more books and 2 for return "))
        if(userInput3==1):
            count2 = True
        else:
            filewrite()
            break

def returnbook():
    count3 = True
    while(count3):
        with open(user_name) as f:
            userbooks=json.load(f)
            if len(userbooks)<=0:
                print("First you have to issue a book ")
                break
        print("List of Issued books")
        for key, value in userbooks.items():
            print(key, value)
        userInput5=input("select your book which you want to return or you want to return all books press y ")
        new_dict = {}
        for key, value in userbooks.items():
            if key is not userInput5:
                new_dict[key] = value
        userbooks = new_dict
        if(userInput5 == "y"):
            userbooks.clear()
        userInput6=int(input("\nPress 1 for more books you want to return or press 0 for returning main manue "))
        with open(user_name, "w") as f:
            json.dump(userbooks, f)
        if(userInput6 == 1):
            count3 = True
        else:
            break

print("***********Welcome to the LMS***********\n")
user_name = input("Please Registered your self with your name: ")
user_email = input("\nPlease enter your Email Adress ")
if (os.path.exists(user_name)):
    print("Welcome Back " + user_name)
    with open(user_name) as f:
        userbooks=json.load(f)
else:
    file = open(user_name,"w")

count1 = True
while(count1):
    showmanue()
    UserInput= int(input("Select your option "))

    if(UserInput == 1):
        issuebook()

    elif(UserInput == 2):
        returnbook()

    elif(UserInput == 3):
        if len(userbooks)<=0:
            print("First you have to issue a book ")
            continue
        userissuedbooks()
        userInput4=int(input("Press 1 for returning main manue "))
        if(userInput4==1):
            continue
        else:
            continue

    elif(UserInput == 4):
        print("Thank you for using LMS")
        filewrite()
        userbooks={}
        count1 = False