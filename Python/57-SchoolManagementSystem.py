# School Management system


student = list()
studentids = set()
fees = list()

def addStudentInfo():

    while(True):
        id = str(input('Enter Student id   :'))

        if id not in studentids:
            break

        print('Student id already Present')


    grade = {'English' : 0, 'Urdu' : 0, 'Math' : 0}
    name = str(input('Enter Student name :'))
    clas = str(input('Enter class : '))
    section = str(input('Enter section :'))
    phone = str(input('Enter phone :'))
    address = str(input('Enter address :'))
    grade = {'English' : 0, 'Urdu' : 0, 'Math' : 0}

    stu = [name.lower().title(),id.upper(),clas,section.upper(),phone,address.lower().title(),grade]
    student.append(stu)
    studentids.add(id)

    date = list()
    fees.append([id.upper(),date])

    

def showStudents():
    i = 1
    for x in student:
        print('Student : ', i)
        print('Name   :',x[0])
        print('Id     :',x[1])
        print('Class  :',x[2])
        print('Section:',x[3])
        print('Phone  :',x[4])
        print('Address:',x[5])

        for gr in x[6]:
            print(gr,':',x[6][gr], end = ' ')

        print('\n')
        i += 1


def UpdateStudent():
    while(True):
        id = str(input('Enter Student id   :'))

        if id in studentids:
            break

        print('Student id is not Present')

    index = student.index(next(( x for x in student if id == x[1])))

    grade = {'English' : 0, 'Urdu' : 0, 'Math' : 0}
    name = str(input('Enter Student name :'))
    clas = str(input('Enter class : '))
    section = str(input('Enter section :'))
    phone = str(input('Enter phone :'))
    address = str(input('Enter address :'))
    grade = student[index][6]

    stu = [name.lower().title(),id.upper(),clas,section.upper(),phone,address.lower().title(),grade]
    student[index] = stu
        

def searchStudents():
    while(True):
        id = str(input('Enter Student id   :'))

        if id in studentids:
            break

        print('Student id is not Present')

    x = next((x for x in student if id == x[1]))


    print('Name   :',x[0])
    print('Id     :',x[1])
    print('Class  :',x[2])
    print('Section:',x[3])
    print('Phone  :',x[4])
    print('Address:',x[5])

    for gr in x[6]:
        print(gr,':',x[6][gr], end = ' ')

    print('\n')

def editGrades():
    while(True):
        id = str(input('Enter Student id   :'))

        if id in studentids:
            break

        print('Student id is not Present')

    x = next((x for x in student if id == x[1]))

    print('Name : ',x[0])
    subject = input('Enter the subject : ')
    subject = subject.lower().capitalize()

    if subject in x[6]:
        marks = input('Enter the marks : ')
        x[6][subject] = marks
    else:
        print("Subject Doesn't exist.")

def removeStudents():
    while(True):
        id = str(input('Enter Student id   :'))

        if id in studentids:
            break

        print('Student id is not Present')

    student.remove(next((x for x in student if id == x[1])))

def studentsInEachClass():
    classstudents = dict()

    for stu in student:
        if stu[2] not in classstudents:
            classstudents.update({stu[2]:1})
        else:
            classstudents[stu[2]] += 1

    for x in classstudents:
        print('Class :', x , '  Students :',classstudents[x])

def makeResult():
    for stu in student:
        sum = 0
        for x in stu[6]:
            sum += int(stu[6][x])
        
        percentage = (sum * 100)/ (len(stu[6]) * 100)

        print(f"Name : {stu[0]}  Id : {stu[1]} Result : {percentage:.2f}")

def addFees():
    day = input('Enter the day :')
    month = input('Enter the month : ')
    year  = input('Enter the year : ')

    date = [day,month,year]

    for x in fees:
            x[1].append([date,'UNPAID'])

def showfees():
    for x in fees:
        print('Id :',x[0])

        for y in x[1]:
            lt = y[0]
            print('Date : ', f'{lt[0]} - {lt[1]} - {lt[2]}', ' Status :', y[1])

def updateFees():
    while(True):
        id = str(input('Enter Student id   :'))

        if id  in studentids:
            break

        print('Student id not Present')


    month = input('Enter the month : ')
    year  = input('Enter the year : ')
    status = input('Enter the status (paid , unpaid): ')
    status = status.upper()

    for x in fees:
        if id.upper() == x[0]:
            found = False
            for y in x[1]:
                date = y[0]
                if date[1] == month and date[2] == year:
                    y[1] = status
                    print('Fees Updated succesfully.')
                    found = True
            
            if not found:
                print('No Voucher Found.')

def studentfees():
    while(True):
        id = str(input('Enter Student id   :'))

        if id  in studentids:
            break

        print('Student id not Present')

    for x in fees:
        
        if id == x[0]:
            for y in x[1]:
                lt = y[0]
                print('Date : ', f'{lt[0]} - {lt[1]} - {lt[2]}', ' Status :', y[1])

def main():
    while(True):
        print('1. Add student Information')
        print('2. Update Student')
        print('3. Show All Students')
        print('4. Search Student')
        print('5. Edit Grades')
        print('6. Remove Student')
        print('7. Students in Each Class')
        print('8. Make result of all Students')
        print('9. Add Fees')
        print('10. Show Fees')
        print('11. Update Fees')
        print('12. Student Fees')
        print('13. Exit')

        choice = int(input("Enter your choice :"))

        if choice == 1:
            addStudentInfo()
        elif choice == 2:
            UpdateStudent()
        elif choice == 3:
            showStudents()
        elif choice == 4:
            searchStudents()
        elif choice == 5:
            editGrades()
        elif choice == 6:
            removeStudents()
        elif choice == 7:
            studentsInEachClass()
        elif choice == 8:
            makeResult()
        elif choice == 9:
            addFees()
        elif choice == 10:
            showfees()
        elif choice == 11:
            updateFees()
        elif choice == 12:
            studentfees()
        elif choice == 13:
            print('Program Exited Succesfully')
            break
        else:
            print('Invalid Input')


main()