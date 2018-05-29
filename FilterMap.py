original = [2,5,8,11,14,17]
even_copy = []
square_copy = []

print("\nOriginal List: {}".format(original))


# Copies Only The Even Numbers Out Of The List
for num in original:
    if((num % 2) == 0):
        even_copy.append(num)
print("Even Copy: {}".format(even_copy))


# Copies and Squares All Of The Numbers From The Original List
for num in original:
    square_copy.append(num*num)
print("Square Copy: {}".format(square_copy))


# Prints The Total Of All Of The Numbers From The Original List
total = 0
for num in original:
    total+=num
print("Total: {}\n".format(total))
