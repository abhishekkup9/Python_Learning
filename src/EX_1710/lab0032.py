# take the input from user whether he are eligible for vote or not

age = input("Enter your age: ")
age = int(age)

if age > 18:
    print("You are Eligible for vote.")
else:
    print("You are not eligible for vote.")

# which one max value

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
#
# if num1 > num2:
#     print("Max number is ", num1)
#     elif num1 < num2:
#     print("Max number is ", num2)
# else:
#     print("equal number")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 > num2:
    print("Max number is", num1)
elif num1 < num2:
    print("Max number is", num2)
else:
    print("Both numbers are equal")
