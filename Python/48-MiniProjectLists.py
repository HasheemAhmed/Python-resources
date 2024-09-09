# School Grade Management system

Students = list()
StudentIds = set()


def add_student(name,ids):
    if ids not in StudentIds:
        grade = {'English':0, 'Urdu' : 0, 'Math' : 0}
        stu = (name,ids,grade)
        Students.append(stu)
        StudentIds.add(ids)

def editing_student_grade(ids,subject,grade):
    if ids in StudentIds:
        stu = next((x for x in Students if x[1] == ids))
        subject = subject.lower().capitalize()
        s = list(stu)
        s[2].update({subject:grade})
        updated_stu = tuple(s)

        index = Students.index(stu)
        Students[index] = updated_stu
    else:
        print('Student Not Found')

def calculate_average(subject):
    subject = subject.lower().capitalize()

    addition = 0

    for stu in Students:
        addition += int(stu[2][subject])

    print(f"Average of the {subject} is {addition/len(Students)}")

def show_Students():
    i = 1
    for stu in Students:
        print('\nStudent :',i)
        print(f"Id   : {stu[1]}")
        print(f"Name : {stu[0]}")

        i = i + 1
        for x,y in stu[2].items():
            print(f"{x} : {y}  ",end = '')

def main():
    while True:
        print("\nSchool Management System")
        print("1. Add a Student")
        print("2. Show All Students")
        print("3. Editing Grades")
        print("4. Calculate Average")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ids = input("Enter  Student id : ")
            name = input("Enter Student name : ")
            add_student(name,ids)
        elif choice == '2':
            show_Students()
        elif choice == '3':
            ids = input("Enter  Student id : ")
            subject = input("Enter Subject : ")
            grade = input("Enter grade : ")
            editing_student_grade(ids,subject,grade)
        elif choice == '4':
            sub = input("Enter the Subject : ")
            calculate_average(sub)
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()