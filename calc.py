'''
@author: shahroz461
@desc: simple calculator
'''

print("For Addition press 1")
print("For Subtraction press 2")
print("Select Your Menu: ")
username = input()

print("Enter First value: ")
a = int(input())
print("Enter Second Value: ")
b = int(input())

if username=="1":
    print("Addition")
    c = a + b
    print(c)

elif username=="2":
    print("Subtraction")
    d = a - b
    print(d)

else:
    print("error: Select valid input")
