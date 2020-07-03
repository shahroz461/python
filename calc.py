'''
@author: shahroz461
@desc: simple calculator
'''
print("<(\"\")")
print(" ( )__")
print("  \___/")

print(" --.   ----")       
print("|     /     \ ")
print("|    / ----- \ ")
print(" --'/         \ ")
print("   /           \ ")
print("for sub press 2")
print("for multiplication press 3")
print("for division press 4")
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
