# Booleans

# True or False

# a = True
# b = False
#
# print(a == b)# False
# print(a != b)# True
# print(a >= True)# True
# print(b <= False)# True
#
# print(True and False)
# print(False and True)
# print(False or True)

# Booleans are useful for quickly checking the state of something

#Booleans with Datatypes

hi = "Hello world!"
# " " and "!" are not alphanumeric

# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith("!"))
# print(hi.startswith("H"))

x = 0
y = 2
z = -3

print(bool(x)) # False - 0 is always False
print(bool(y))
print(bool(z))

#None = Null in a lot of other languages

print(bool(None)) # False
x = None
print(x == False) # False
print(x == True) # False

# Checking if a variable is None

print(x == None)# direct comparison, more complex
print(x is None)# best practice for checking if something 'is None'

print(type(x)) # <class 'NoneType'>
