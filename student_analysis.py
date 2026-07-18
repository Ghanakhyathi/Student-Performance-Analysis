import pandas as pd
import numpy as np


# LOAD STUDENT DATA

def load_data():
    try:
        students = pd.read_csv("students.csv")
        return students
    
    except FileNotFoundError:
        print("students.csv File Not Found.")
        return None
    

# VIEW STUDENTS DATA

def view_students(students):
    print("\n ----STUDENTS DATA ---- ")
    print(students)


# SEARCH STUDENT

def search_student(students):
    name = input("Enter Student Name  : ").lower()
    name = name.lower()
    
    result = students[students["Name"].str.lower() == name]
    
    if result.empty:
        print("Student Not Found.")
    else:
        print(result)


# SHOW AVERAGE MARKS

def average_marks(students):
    students["Average"] = students[["Python" , "Java", "Math"]].mean(axis = 1)

    print("\n Average marks ")
    print(students[["Name","Average"]])


# HIGHEST SCORER

def highest_scorer(students):
    students["Average"] = students[["Python", "Java" , "Math"]].mean(axis = 1)
    highest = students.loc[students["Average"].idxmax()]

    print( "\n HIGHEST SCORER " )
    print(highest)


# LOWEST SCORER

def lowest_scorer(students):
        students["Average"] = students[["Python", "Java" , "Math"]].mean(axis = 1)
        lowest = students.loc[students["Average"].idxmin()]

        print("\n LOWEST SCORER ")
        print(lowest)


# SUBJECT WISE AVERAGE

def subject_average(students):
    print("\n SUBJECT AVERAGE ")
    print("Python : " , np.mean(students["Python"]))
    print("Java : " , np.mean(students["Java"]))
    print("Math : " , np.mean(students["Math"]))


#MAIN MENU

def menu ():
    students = load_data()

    if students is None:
        return
    
    while True :

        print("====STUDENT PERFORMANCE ANALYSIS====")
        print("1.VIEW STUDENTS")
        print("2.SEARCH STUDENT")
        print("3.AVERAGE MARKS")
        print("4.HIGHEST SCORER")
        print("5.LOWEST SCORER")
        print("6.SUBJECT AVERAGE")
        print("7.EXIT")

        try:

            choice = int(input("Enter Your Choice : "))
            print(choice)

            if choice == 1:
                view_students(students) 
            
            elif choice == 2:
                search_student(students)

            elif choice == 3:
                average_marks(students)

            elif choice == 4:
                highest_scorer(students)

            elif choice == 5:
                lowest_scorer(students)

            elif choice == 6:
                subject_average(students)

            elif choice == 7:
                print("Thank You!")

                break

            else:
                print("Invalid Choice")
        
        except ValueError:
            print(" Please Enter Numbers Only! ")
menu()

    












    