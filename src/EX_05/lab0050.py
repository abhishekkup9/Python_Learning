# Function
# No Return type and no parameter/Argument --NRNP

def greet():
    print("Hello World")

result= greet()
print(result)


#No return type with arguments
def greet_by_name(name):
    print("Hello," ,name)

greet_by_name('Abhishek')


#No return type and with default arguments

def say_hello_default_arg(name='Abhishek'):
    print("Hello," ,name)

say_hello_default_arg()
say_hello_default_arg("Amit")


def multiple_arg(Name1='Abhishek',Name2='Amit',Name3='Akash'):
    print("Multiple Argument",Name1,Name2,Name3)
multiple_arg(Name1='Ram' , Name2='Shyam',Name3='Manoj')


#argument and return_type
def sum_of_two_numbers(num1,num2):
    return num1 + num2
result= sum_of_two_numbers(20,24)
print(result)