name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
country = input("Enter your country: ")


name_upper = name.upper()
country_upper = country.upper()
height = round(height, 2)


nickname = (name[0:2] + name[-2:]).upper()


print("Hello", name_upper)
print("You are", age, "years old.")
print("Your height is", height, "feet.")
print("You are from", country_upper + ".")
print("Your nickname is", nickname)