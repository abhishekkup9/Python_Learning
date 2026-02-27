# factorial

num = int(input("Enter the int number"))
fact = 1
if num == 0 and num == 1:
    fact = 1
    print(1)
else:
    for i in range(1, num + 1, 1):
        fact = fact * i
print(fact)
