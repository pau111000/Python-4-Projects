#Create a series of instructions in Python to declare a variable “var” 
#and assign it the value “Hello”. Then, the program must check whether the variable “var” 
#is an integer or a string. If it is an integer, 
#the program should print “Integer” on the console, and if it is a string, 
#the program will print “String” on the console.

var = "Hello"
if isinstance(var, int):
    print("Integer")
elif isinstance(var, str):
    print("String")