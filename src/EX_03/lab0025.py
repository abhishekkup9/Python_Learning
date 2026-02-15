#String
name="Abhishek"

#str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))

a="90"

print(a)
print(type(a)) #str because it is under ""

age=45
print(age)
print(type(age)) # int

name="This is a big line"
name=name+"1" # we cannot add directly 1, we need to convert it into str
print(name)

first_name=('Abhishek')
last_name="Kumar"
full_name=first_name+ last_name
print(full_name)

#None data type

val=None
print(type(val))

#id
age=10
age2=10
print(id(age))
print(id(age2))