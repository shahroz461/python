print("for add press 1")
print("for sub press 2")
'''user input leygay hum is variable '''
print("select your menu: ")
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

    print("error: Select vslid input")


