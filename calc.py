print("for add press 1")
print("for sub press 2")
print("for multiplication press 3")
print("for division press 4")
'''user input leygay hum is variable '''
print("select your menu: ")


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
    
elif username=="3":
    print("multiplication")
    e = a * b
    print(e)
elif username=="4":
    print("division")
    f = a / b
    print(f)

else:

    print("error: Select vslid input")



    print("error: Select valid input")
