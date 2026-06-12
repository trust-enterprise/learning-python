# CALCULATOR WITH TRY EXCEPT
try:
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
except ValueError:
    print("enter a valid number")
    exit()

op = input("enter the operation to perform ((+, -, *, /): ")
result = None

if op == '+':
    result = num1+num2
elif op == '-':
    result = num1-num2
elif op == '*':
    result = num1*num2
elif op == '/':
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("second number can't be zero") 
        exit()
else:
    print("invalid operator")
    exit()

print("Result: ", result)