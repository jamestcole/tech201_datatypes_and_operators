# tech201_datatypes_and_operators
tech201_datatypes_and_operators

## Data types
There are many datatypes in python which are useful for different tasks, the most common being
Ints, Floats, Strings and Boolean. complex numbers are rare and longs are no longer in use but both
are worth being aware of.

- Numeric - Ints, Floats, longs, complex

- String - Text of any type

- Boolean - True or False

### Operators
Basic mathematical operators are useful for calculations in python, while comparison operators are used for comparisons between numbers.

- Arithmetic operators
 +,-,*,/

- Comparison operators
 >,<,==,!=,>=,<=

### Implementing numeric types

Integers store whole numbers, lets start by using these.

`a=24`
`b=16`

We can see by printing the following code, + returns an integer, since two intergers are added, while the comparison operators return a boolean.

`print(a + b)` #40
`print(a > b)` #True
`print(a < b)` #False

Let's have a look at what happens when floats are added together.

`FloatNum = 1.356` 
`IntNum = 4`
`print(FloatNum + IntNum)` #5.356

You can see it returns a float.
Dividing one by three returns the a float, however multiplying it by three returns 1, In this case the float is rounded up.

`one_third= 1/3` 
`print(one_third)` #0.33333333333
`print(one_third*3)` #1


## Strings

Strings can be contained in both single and double quotes, They can contain all kinds of characters, but bear in mind some characters can change the functioning of the string in certain formats such as f strings which we will see a little later.

`Single_quotes = 'Look! Single quotes'`
`Double_quotes = "Look! Double quotes"`

You can see both of these work , however make sure not to mix them.

`print(Single_quotes)`#Look! Single quotes
`print(Double_quotes)`#Look! Double quotes

In this case the string does not print correctly unless you use the \ key to cancel out the additional qoutation marks.

`string_failure = 'I said \'Wow\''`
`print(string_failure)`

Another way of printing quotes is just to use different quotes but this can be confusing.
`quote_in_quote = 'I said "Wow!"'`
`print(quote_in_quote)`

standard practice is to use double qoutes for strings and single within if needed.
`reverse_quote = "I said 'Wow'"`
`print(reverse_quote)`

###String slicing

Everything in code starts with 0 not 1 as can be demonstrated below, bare this in mind when slicing strings

H e l l o   W o r l d !
0 1 2 3 4 5 6 7 8 9 10 11

Hw = "Hello world!"

`print(Hw[7:])` # orld!
`print(Hw[-5:])` # orld!
`print(Hw[:5])` # Hello
`print(Hw[0:5])` # Hello

# # String methods
#
# # strip()
#
# white_space = "lot's of space at the end                   "
# print(len(white_space)) #44
# print(len(white_space.strip()))
# # A few more
# example_text = "Here's some text with lot's of text"
#
# # Count a substring within a string
# print(example_text.count("text"))
#
# # Make everything lowercase
# print(example_text.lower())
#
# #Make everything uppercase
# print(example_text.upper())
#
# #Capitalise things
# print(example_text.capitalize())
#
# #Replace characters/text
# print(example_text.replace("with" , ","))
#
# #Concatenation
#
# a = "here "
# b = "more "
# c = "much more"
# print(a + b + c)

#Casting

# x = 2
# y = 5.4
# z = " there's a number 25.4 unless we put a space in"
# #print(x + y + z)
# print(str(x) + ", " + str(y) + z)

# string to numeric
#
# int_string = "6"
# print(float(int_string))
# print(type(int(int_string)))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years and old {height_cm}cm tall")

#F-strings allow us to use methods/evaluations too

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS !!!")

# F-strings to specify precision in rounding and decimals

pi = 3.14159265359

print(f"Pi to 3 decimal places:{pi:.3f}") # Pi to 3 decimal places
print(f"Pi to 3 decimal places:{pi:.5f}") # Pi to 5 decimal places

score = 16
max_score = 26

print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:.2%}") # 61.54
print(f"You scored {score/max_score:.0%}") # 62%

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