# write a python program which take a num from user and tell whether the 1st num is greater or
#less or equal

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")