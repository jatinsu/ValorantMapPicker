import random
theMap = ["Ascent", "Bind", "Fracture", "Icebox", "Breeze", "Split"]
print("Welcome to a Python Valorant Map Picker!")

removeMap = input("What maps would you like to remove (enter each one with a space in between, or enter 'N' to remove none of them)? ").capitalize().split()
# captilize each element in removeMap
removeMap = [word.capitalize() for word in removeMap]

for i in range(len(removeMap)):
        if removeMap[i] in theMap:
            theMap.remove(removeMap[i])

print("Your map is", random.choice(theMap))