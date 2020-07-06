'''
mark1 = float(input("enter your first subject numbers: "))
mark2 = float(input("enter your second subject numbers: "))
mark3 = float(input("enter your third subject numbers: "))
mark4 = float(input("enter your fourth subject numbers: "))
mark5 = float(input("enter your fifth subject numbers: "))

mark6 = (mark1 + mark2 + mark3 + mark4 + mark5)
percen = (mark6 / 500) * 100
print(percen)

if percen > 90:
    print("A")

elif percen > 80:
    print("B")

elif percen > 70:
    print("C")

elif percen > 60:
    print("D")
    
elif percen > 50:
    print("E")

print("enter your name")

name = input()
print("lastname")
lastname = input()

print(name )
print(lastname )

print("enter your class")
clas = input()


print(percen)

'''
name = input('enter your name: ')
clas = input('class: ')

subject = ["math", "chem", "phys", "urdu", "comp"]
arrM = [0 ,0 ,0 ,0 ,0]

# input subject marks
totalval = 0
i = 0 
while i< 5:
    print("Enter "+ subject[i] + " marks")
    arrM[i] = int(input())
    totalval = totalval + arrM[i] 
    i = i+1

print("Name: "+name)
print("class: "+ clas)

print("==========")
#print marksheet 
y = 2
while y < 5:
    print("| "+subject[y] +" "+str(arrM[y])+" |" )
    y = y + 1
print("=========")


print("total marks", totalval)
percen = (totalval / 500) * 100
print("Percentage: ",percen)

if percen > 90:
    print("Grade: A")

elif percen > 80:
    print("Grade: B")

elif percen > 70:
    print("Grade: C")

elif percen > 60:
    print("Grade: D")
    
elif percen > 50:
    print("Grade: E")
else:
    print("YOU ARE FAIL!")

