def bandNameGen(a, b):
    bandName = a + " " + b
    return bandName
    
print("Welcome to your Band Name Generator")

city = input("Which city did you grew up in? ")

pet = input("What's the name of your first pet? ")

bandName = bandNameGen(city, pet)

print("Your Band Name: " + bandName)