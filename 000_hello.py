# IMAGES
from PIL import Image
img = Image.open("cat.jpg")
img.show()

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