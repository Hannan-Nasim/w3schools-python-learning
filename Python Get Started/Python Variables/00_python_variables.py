# Variables
# Variables are containers for storing the data values.

# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "Jhon"
print (x)
print (y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # y is of type str

print(x)

# Casting 
# If you want to secify the data type of the variable it can be done with casting 
x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0

# Get the type
# You can get the data type of the variable with the type() function 

x = 5
y = "Jhon"

print(type(x))
print(type(y))

# Single or double quotes
# Strings can be declared either with single or  double quotes:

x = "Jhon"
# is same as
x = 'Jhon'

# Case-Sensitive 
# Variable names are case-sensitive 

# This will create two variables;
a = 4 
A = "Sally"
# A will not overwrite a

