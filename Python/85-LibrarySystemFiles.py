# Files based Library Management System

import os
import re
import datetime

if not os.path.exists("Library"):
    os.makedirs("Library")

# Function to handle with the input errors

def inputValidation(text = str(),convert = ""):
    while True:
        userInput = input(text)

        if convert.lower() == "int":
            try:
                return int(userInput)    
            except ValueError:
                print('Please Enter a Number.')
        elif convert.lower() == "float":
            try:
                return float(userInput)    
            except ValueError:
                print('Please Enter a Number.')
        else:
            return userInput
            
# Function to avoid duplicates book ids

def checkIds(filename,txt):
    try:
        bid = open(f"Library/{filename}.txt","r")
    except FileNotFoundError:
        bid = open(f"Library/{filename}.txt","x")
        bid = open(f"Library/{filename}.txt","r")

    book = bid.readline()
    ids = book.split(" ")

    while True:
        id = inputValidation(txt,"int")
        if str(id) not in ids:
            bid.close()
            return id
        else:
            print("Id Already Exists.")

# Function to add Genre 

def addGenre():
    genre = input("Enter the Genre : ")

    fi =  open(r"Library\Genre.txt","a")

    fi.write(f"{genre.title()},\n")
    fi.close()

# Function to view Genre

def viewGenre():
    try:
        fi =  open(r"Library\Genre.txt","r")
        num = 1
        value = fi.readlines()
        for name in value:
            lt = name.split(",")
            print(f"{num}. {lt[0]}")
            num += 1

        fi.close()
    except FileNotFoundError:
        print("File Not Found.")

# Function to select Genre During adding a book

def selectGenre():
    print("Select Genre : ")
    viewGenre()
    try:
        fi =  open(r"Library\Genre.txt","r")
        value = fi.readlines()
        while True:
            inp = inputValidation("Enter your Choice","int")
            
            if inp in range(1,len(value) + 1):
                break
            else:
                print("Please Enter a valid Choice.")

        genre = value[inp - 1].split(",")
        fi.close()
        return genre[0]
            
    except FileNotFoundError:
        print("File Not Found.")
        fi =  open(r"Library\Genre.txt","a")
        fi.write("No Genre,\n")
        fi.close()
        return "No Genre"
        
    
# Function to add a book    

def addBook():
    bookId = checkIds("BookIds","Enter the Book id : ")
    title = inputValidation("Enter the Title : ")
    author = inputValidation("Enter the author : ")
    genre = selectGenre()
    avail = "Available"


    fi = open(r"Library\Books.txt","a")
    fi.write(f"{bookId},{title.title()},{author.title()},{genre.title()},{avail.title()},\n")
    fi.close()

    bid = open(r"Library/BookIds.txt","a")
    bid.write(f"{bookId} ")
    bid.close()

# Function To Display Books

def displayBook():
    try:
        re = open(r"Library\Books.txt","r")

        books = re.readlines()
        i = 1
        for b in books:
            lt = b.split(",")
            print("Book : ", i)
            print(f"{"BookId":<12} : {lt[0]}")
            print(f"{"Title":<12} : {lt[1]}")
            print(f"{"Author":<12} : {lt[2]}")
            print(f"{"Genre":<12} : {lt[3]}")
            print(f"{"Availibility":<12} : {lt[4]}")
            i += 1

        re.close()
    except FileNotFoundError:
        print("File not Found")


# Function To Display Books by using filter

def displayBookUsingFilter():
    while True:
        print("1. Filter By Genre.")
        print("2. Filter By Author.")
        print("3. Filter By Availibility.")

        user = inputValidation("Enter Your Choice : ", "int")
        if user in range(1,4):
            break
        else:
            print("Invalid Choice.")

    filterBy = ["Genre","Author","Availibility"]

    try:
        re = open(r"Library\Books.txt","r")
        ge = open(r"Library\Genre.txt","r")
        books = re.readlines()
        genre = ge.readlines()
        
        if filterBy[user - 1] == "Genre":
            for x in genre:
                g = x.split(',')
                i = 1
                print(f"\n{g[0]} : \n")
                for b in books:
                    lt = b.split(",")
                    if g[0] == lt[3]:
                        print("Book : ", i)
                        print(f"{"BookId":<12} : {lt[0]}")
                        print(f"{"Title":<12} : {lt[1]}")
                        print(f"{"Author":<12} : {lt[2]}")
                        print(f"{"Genre":<12} : {lt[3]}")
                        print(f"{"Availibility":<12} : {lt[4]}")
                        i += 1
        
        elif filterBy[user - 1] == "Author":
            author = list()
            for x in books:
                lt = x.split(",")
                author.append(lt[2])

            for x in author:
                i = 1
                print(f"\n{x} : \n")
                for b in books:
                    lt = b.split(",")
                    if x == lt[2]:
                        print("Book : ", i)
                        print(f"{"BookId":<12} : {lt[0]}")
                        print(f"{"Title":<12} : {lt[1]}")
                        print(f"{"Author":<12} : {lt[2]}")
                        print(f"{"Genre":<12} : {lt[3]}")
                        print(f"{"Availibility":<12} : {lt[4]}")
                        i += 1
        else:
            i = 1
            for b in books:
                lt = b.split(",")
                if lt[4] == "Available":
                    print("Book : ", i)
                    print(f"{"BookId":<12} : {lt[0]}")
                    print(f"{"Title":<12} : {lt[1]}")
                    print(f"{"Author":<12} : {lt[2]}")
                    print(f"{"Genre":<12} : {lt[3]}")
                    print(f"{"Availibility":<12} : {lt[4]}")
                    i += 1

        re.close()
        ge.close()
    except FileNotFoundError:
        print("File not Found")

# Function to check the emails

def checkEmail():
    while True:
        user = inputValidation("Enter the email : ")
        email = re.search(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",user)
        if email:
            return email.group()
        else:
            print("Please enter a valid email address.")

# function to check the phone number

def checkNumber():
    while True:
        user = inputValidation("Enter the Number : ")
        number = re.search(r"\b\d+[-._ ]*\d{2}\d+[-._ ]*\d{3}\d+\b",user)
        if number:
            return number.group()
        else:
            print("Please enter a valid Phone Number.")

            
# function to add user

def addUser():
    userId = checkIds("UsersIds","Enter the user id : ")
    name = inputValidation("Enter the name : ")
    email = checkEmail()
    number = checkNumber()

    fi = open(r"Library\Users.txt","a")
    fi.write(f"{userId},{name.title()},{email},{number},\n")
    fi.close()

    fid = open(r"Library\UsersIds.txt","a")
    fid.write(f"{userId} ")
    fid.close()

    print("User Added Succesfully.")

# function for viewing user
    
def viewUser():
    try:
        fi = open(r"Library\Users.txt","r")
        user = fi.readlines()

        i = 1
        for x in user:
            us = x.split(",")
            print("\nUser : ", i)
            print(f"{"UserId":<6} : {us[0]}")
            print(f"{"Name":<6} : {us[1]}")
            print(f"{"Email":<6} : {us[2]}")
            print(f"{"Phone":<6} : {us[3]}")
            i += 1

    except FileNotFoundError:
        print("File not found.")

# function to borrow book

def checkIdsPresent(filename,txt):
    try:
        bid = open(f"Library/{filename}.txt","r")
    except FileNotFoundError:
        bid = open(f"Library/{filename}.txt","x")
        bid = open(f"Library/{filename}.txt","r")

    book = bid.readline()
    ids = book.split(" ")

    while True:
        id = inputValidation(txt,"int")
        if str(id) in ids:
            bid.close()
            return id
        else:
            print("Id Doesn't Exists.")
            while True:
                user = input("Do you want to cancel Transaction (y/n)?")
                if user == 'y' or user == 'Y':
                    return False
                elif user == 'n' or user == 'N':
                    break
                else:
                    print("Invalid Input.")

# function to check avalibilty of book

def bookavailibility():
    while True:
        bookid = checkIdsPresent("BookIds","Enter the Book Id : ")
        if bookid:
            fi = open(r"Library/Books.txt","r+")
            book = fi.readlines()

            for x in range(len(book)):
                y = book[x].split(',')

                if str(bookid) == y[0]:
                    if y[4] == "Available":
                        book[x] = book[x].replace("Available","Unavailable")
                        fi.seek(0)
                        fi.writelines(book)
                        fi.close()
                        return bookid
                    else:
                        print("Book is Unavailable.")
                        while True:
                            user = input("Do you want to cancel Transaction (y/n)?")
                            if user == 'y' or user == 'Y':
                                return False
                            elif user == 'n' or user == 'N':
                                break
                            else:
                                print("Invalid Input.")
                        break
        else:
            return False
                    
# function to borrow book    

def borrowBook():
    transid = checkIds("TransIds","Enter the transaction id : ")
    bookid = bookavailibility()
    if bookid:
        userid = checkIdsPresent("UsersIds","Enter the User Id : ")
        if userid:
            borrowdate = datetime.date.today()
            day = inputValidation("Enter Number of Days : ", "int") 
            returndate = borrowdate + datetime.timedelta(days=day)

            fi = open(r"Library/Transaction.txt","a")
            fi.write(f"{transid},{bookid},{userid},{borrowdate},{returndate},\n")
            fi.close()

            fi = open(r"Library/TransIds.txt","a")
            fi.write(f"{transid} ")
            fi.close()

            print("Book Borrowed Succesfully.")

    else:
        print("Transaction Cancelled Succesfully.")
    

# function to getname

def getname(filename,id):
    try:
        fi = open(f"Library/{filename}.txt","r")
        tr = fi.readlines()
        
        for x in tr:
            ids = x.split(",")
            if ids[0] == str(id):
                return ids[1]
    except FileNotFoundError:
        return "No User"

# function to view transactions

def viewtransactions():
    try:
        fi = open(r"Library/Transaction.txt","r")
        tr = fi.readlines()

        i = 1
        for x in tr:
            trans = x.split(",")
            print("\nTransaction : ", i)
            print(f"{"Transaction Id ":<15} : {trans[0]}")
            print(f"{"Book Id":<15} : {trans[1]}")
            print(f"{"Book Title":<15} : {getname("Books",trans[1])}")
            print(f"{"User Id":<15} : {trans[2]}")
            print(f"{"User Name":<15} : {getname("Users",trans[2])}")
            print(f"{"Borrow Date":<15} : {trans[3]}")
            print(f"{"Return Date":<15} : {trans[4]}")
            i += 1

    except FileNotFoundError:
        print("File not found.")

# function to change book availibility

def changebookavailibility(bookid):
    try:
        fi = open(r"Library/Books.txt","r+")
        book = fi.readlines()

        for x in range(len(book)):
            y = book[x].split(',')

            if str(bookid) == y[0]:
                book[x] = book[x].replace("Unavailable","Available")
                fi.seek(0)
                fi.writelines(book)
                fi.close()
    except FileNotFoundError:
        print("File not found.")


# function to return a book
    
def returnbook():
    transid = checkIdsPresent("TransIds","Enter the Transaction id : ")

    if transid:
        try:
            fi = open(r"Library/Transaction.txt","r")
            tr = fi.readlines()

            i = 1
            for x in range(len(tr)):
                trans = tr[x].split(",")
                if trans[0] == str(transid): 
                    print("\nTransaction : ", i)
                    print(f"{"Transaction Id ":<15} : {trans[0]}")
                    print(f"{"Book Id":<15} : {trans[1]}")
                    print(f"{"Book Title":<15} : {getname("Books",trans[1])}")
                    print(f"{"User Id":<15} : {trans[2]}")
                    print(f"{"User Name":<15} : {getname("Users",trans[2])}")
                    print(f"{"Borrow Date":<15} : {trans[3]}")
                    print(f"{"Return Date":<15} : {trans[4]}")
                    i += 1
                    changebookavailibility(trans[1])
                    tr.pop(x)
                    wr = open(r"Library/Transaction.txt","w")
                    wr.writelines(tr)
                    wr.close()
                    fi.close()

                    fid = open(r"Library/TransIds.txt","r")
                    lt = fid.readline()
                    lt = lt.split(" ")
                    lt.remove(str(transid))
                    fid.close()

                    fid = open(r"Library/TransIds.txt","w")
                    for x in lt:
                        fid.write(x + " ")
                    fid.close()
                    
                    break

        except FileNotFoundError:
            print("File not found.")
    else:
        print("Transaction Not Found")


# main function

def main():
    while True:
        print('1. Add a Book.')
        print('2. Add Genre')
        print('3. Add User.')
        print('4. View Books')
        print('5. View Genre')
        print("6. View Users")
        print('7. View Books Using Filter')
        print('8. Borrow book.')
        print("9. View Borrow Books")
        print("10. Return a Book")
        print('11. Exit')

        choice = int(input("Enter your choice :"))

        if choice == 1:
            addBook()
        elif choice == 2:
            addGenre()
        elif choice == 3:
            addUser()
        elif choice == 4:
            displayBook()
        elif choice == 5:
            viewGenre()
        elif choice == 6:
            viewUser()
        elif choice == 7:
            displayBookUsingFilter()
        elif choice == 8:
            borrowBook()
        elif choice == 9:
            viewtransactions()
        elif choice == 10:
            returnbook()
        elif choice == 13:
            print('Program Exited Succesfully')
            break
        else:
            print('Invalid Input')

main()

