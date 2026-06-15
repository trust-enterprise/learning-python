# API REQUEST
import requests

try:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)

    response.raise_for_status()
    data = response.json()
    print(f"status code: {response.status_code}")
    print(f"1 USD = data['rates']['INR'] INR")

except requests.exceptions.Timeout as e:
    print("timed out", e)
except requests.exceptions.HTTPError as e:
    print("HTTP error", e)
except requests.exceptions.RequestException as e:
    print("Request error", e)
except KeyError:
    print("key not found")
# GETTER, SETTER, DELETER
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @property
#     def result(self):
#         return "Pass"

#     @result.setter
#     def result(self, marks):
#         self.marks = marks
#         print(f"updated marks is {self.marks}")

#     @result.deleter
#     def result(self):
#         self.marks = None
#         print(f"result deleted")


# stu = Student("haris", 90)
# print(stu.result)

# print(stu.marks)
# stu.result = 95
# del stu.result


# # OOP: class variable, instance method, overriding, classmethod, staticmethod, inheritance
# class Employee:
#     job = "developer"

#     @classmethod
#     def change_job(cls, job):
#         cls.job = job

#     @classmethod
#     def string_emp(cls, string):
#         name, pay = string.split("-")
#         return cls(name, int(pay))

#     @staticmethod
#     def after_increment(pay):
#         pay += 10000
#         return pay

#     def __init__(self, name, pay):
#         self.name = name
#         self.pay = pay

#     def show(self):
#         return f"\n{self.name}\n{self.pay}"

#     def give_raise(self, amount):
#         self.pay += amount
#         return self.pay


# class Developer(Employee):
#     def __init__(self, name, pay, prog_lang):
#         super().__init__(name, pay)
#         self.prog_lang = prog_lang


# class Manager(Employee):
#     def __init__(self, name, pay):
#         super().__init__(name, pay)
#         self.emp_list = []

#     def add_emp(self, emp):
#         if not isinstance(emp, Employee):
#             raise TypeError("Must be a non-developer Employee")
#         if issubclass(Developer, Employee):
#             raise TypeError("Must be a non-developer Employee")
#         self.emp_list.append(emp)

#     def show_emp(self):
#         return self.emp_list


# mgr1 = Manager("Ziya", 125000)
# emp1 = Developer("Ali", 50000, "python")
# emp2 = Employee("Sara", 65000)
# emp3 = Employee.string_emp("Shalu-40000")

# # mgr1.add_emp(emp1)
# # mgr1.add_emp(emp2)
# # mgr1.add_emp(emp3)
# # print(f"{mgr1.show_emp()}\n")

# # emp2.job = "doctor"
# # print(f"\n{emp1.name} --> {emp1.job}")
# # print(f"{emp2.name} --> {emp2.job}")
# # print(f"{emp3.name} --> {emp3.job}\n")

# # Employee.change_job("architect")

# print(f"{emp1.name} --> {emp1.job}, {emp1.pay}, {emp1.prog_lang}")
# print(f"{emp2.name} --> {emp2.job}, {emp2.pay}")
# print(f"{emp3.name} --> {emp3.job}, {emp3.pay}\n")
# print(f"{mgr1.name} --> {mgr1.pay}\n")
# print(
#     f"{mgr1.name} recieves a raise of Rs. 25000, and his new salary is {mgr1.give_raise(25000)}"
# )

# print(
#     f"after increment, {emp1.name}'s salary is {Employee.after_increment(emp1.pay)}\n"
# )

# DUNDER/ MAGIC METHODS
# class Movie:
#     def __init__(self, title, rating):
#         self.title = title
#         self.rating = rating

#     def __str__(self):
#         return f"Movie: {self.title}"

#     def __repr__(self):
#         return f"Movie('{self.title}', {self.rating})"

#     def __add__(movie1, movie2):
#         return movie1.rating + movie2.rating

#     def __len__(self):
#         return len(self.title)


# movie1 = Movie("Interstellar", 9)
# movie2 = Movie("Sholay", 9.8)

# print(movie1)
# print(repr(movie1))
# print(movie1 + movie2)
# print(len(movie1))


# IMAGES
# from PIL import Image
# img = Image.open("cat.jpg")
# img.show()

# WRITING, APPENDING AND READING A FILE
# with open("names.txt", "w") as file:
#     file.write("flumen labs")

# with open("names.txt", "a") as f:
#     f.write("\nsheikh")
#     f.write("\nabdullah")

# with open("names.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# STORING FILE INTO A LIST + SORTING IT LATER
# namelist = []
# with open("names.txt") as f:
#     for line in f:
#         namelist.append(line.strip())

# print(namelist)

# for name in sorted(namelist):
#     print(name)

# READING FROM CSV ROW-WISE + OUTPUT AS LIST, DICTIONARY + SEARCHING DICTIONARY BY CONVERTING IT INTO A LIST FIRST
# import csv

# with open("students.csv", "r") as f:
#     # rows = csv.reader(f)
#     rows = csv.DictReader(f)
#     # print(rows)

#     # for row in rows:
#     #     print(row["name"])
#     #     print(row)

#     students = list(rows)
#     print(students[1]["city"])


# USING LAMBDA FUNCTION TO SORT LIST OF STUDENTS BASED ON CITY
# import csv
# stu_list = []
# with open("students.csv","r") as f:
#     students = csv.DictReader(f)
#     for student in students:
#         stu_list.append(student)

# print(stu_list)

# stu_list.sort(key= lambda student: student['city'])
# print(stu_list)

# LEARNING TRY EXCEPT
# try:
#     num = int("abc")
# except ValueError as e:
#     print(e)


# KEEP ASKING A NO. UNTIL ABOVE 100
# while True:
#     num = int(input('enter a no.: '))
#     if num>100:
#         print("good bye")
#         break
#     print("entered number is not greater than 100..")

# LOOP FOR EVEN NOS
# for i in range(2,21,2):
#     print(i)

# FORMAT STRING
# name = "sheikh"
# age = 42
# print(f"hello, this is {name} and i'm {age} yrs old")*.369
