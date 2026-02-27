# write a programme that print number from 1 to 100.
# Loop for however for multiple of 3 print "Fizz" instead of number
#for multiple of 5 print "Buzz" and for both 3 & 5 print "FizzBuzz" else number


for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)