# find out the grade from the marks
# 90-100 A
#80-89  B
#70-79 C
#60-69 D
#0-59 F

marks= int(input("Enter marks: "))

grade= "F"
if marks >= 90 and marks <= 100 :
    grade = "A"
    print("Your grade is ", grade)
elif marks >= 80 and marks <= 89 :
    grade = "B"
    print("Your grade is ", grade)
elif marks >= 70 and marks <= 79 :
    grade = "C"
    print("Your grade is ", grade)
elif marks >= 60 and marks <= 69 :
    grade = "D"
    print("Your grade is ", grade)
else:
    grade = "F"
    print("Your grade is ", grade)