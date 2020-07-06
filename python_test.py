#print("teacher name")
#teacher = str(input())
#
#print("subjects")
#
#subjects = str(["maths", "english", "urdu", "chemistry", "physics"])
#print(subjects)
#
#print("Marks /per subject 100")
#print("Press '1' to know how many subjects in there")
#marks = int(input())
#
#print(marks)
#
#while marks <= 4:
#    marks = marks + 1
#    print(marks + "there are five subjects")




sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")
