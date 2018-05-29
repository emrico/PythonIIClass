# This code utilizes the upper and lower functions

file = open("alice_in_wonderland.dat","r")
filecontents = file.read()
number_of_e = 0.0
letter_count = 0

for character in filecontents:
    if(character.isalpha()):
        letter_count+=1
        if(character.lower()=="e"):
            number_of_e += 1
file.close()


print("\nTotal Number Of Letters: {}".format(letter_count))
print("Number of e's: {}".format(number_of_e))
print("{:.1f}% of all the letters are e's\n".format((number_of_e / letter_count)*100))
