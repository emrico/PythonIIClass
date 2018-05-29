import random as r

results = [0] * 11
max = 1000000

def roll_dice():
    return r.randint(1,6) + r.randint(1,6)

for i in range(max):
    num = roll_dice()
    results[num-2] += 1


print("\nNumber\tProbability")
print("======\t===========")
for j in range(11):
    print("{}\t{:.2f}%".format(j+2,((results[j])/max)*100))
print("\n")
