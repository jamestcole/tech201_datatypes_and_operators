print("What is your name,age,date of birth address and hobbies")
name = input("name:")
age = input("age:")
dob = input("date of birth:")
house_number = input("your house number is:")
street = input("your street is:")
Town = input("your Town is:")
PostCode = input("your Post code is:")
hobbies = input("your hobbies are:")

if int(age)<18:print(f"{name} is underage, come back in {18-int(age)} years")

print(f"{name.capitalize()}'s age is {age}, their date of birth is {dob} and their hobbies are {hobbies}")
print(f"{name.capitalize()}'s address is house number {house_number} on {street.capitalize()} street in {Town.capitalize()} with the following postcode: {PostCode.upper()}")