#ursaminor

import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
bl = []
kievs = []
gdansks = []

random.seed(a=None,version=2)
output = open("plates", "w")
print("Numbers being generated")
while True:

    plate = ""
    let1 = random.choice(alphabet)
    let2 = random.choice(alphabet)
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    num3 = random.choice(numbers)
    num4 = random.choice(numbers)
    let3 = random.choice(alphabet)
    let4 = random.choice(alphabet)

    plate = let1 + let2 + " " + num1 + num2 + num3 + num4 + " " + let3 + let4

    while plate in bl:
        plate = let1 + let1 + " " + num1 + num2 + num3 + num4 + " " + let3 + let4
        
    bl.append(plate)
    output.write(plate + "\n")
    print("Kiev plates: " + str(len(kievs)))
    print("Gdansk plates: " + str(len(gdansks)))
    if plate[0] == "A" and plate[1] == "A":
        kievs.append(plate)
    if plate[0] == "G" and plate[1] == "D":
        gdansks.append(plate)

output.close()
