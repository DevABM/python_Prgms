print("1.Introduction to Sting Data Type")
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

print("2.STRING CONCATENATION")
firstString = "WATER"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("3.Working with input Strings")
ques = input("What module are you working?")
print(ques)
name = input("whatis your name? ")
print(name)
print("Formatting output Strings")
color = input("what is your favorite color?")
animal = input("What is your favorite animal?")
print("{}, you like a {} {}!".format(name,color,animal))
