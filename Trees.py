file = open("trees.dat","r")

num_of_trees = 0
average_height = 0
height_of_tallest = 0
height_of_shortest = 10000

for line in file:
    num_of_trees += 1
    average_height += float(line)

    if(height_of_tallest < float(line)):
        height_of_tallest = float(line)
    if(height_of_shortest > float(line)):
        height_of_shortest = float(line)

average_height /= num_of_trees
#average_height*= 100

print("Total Trees = {}".format(num_of_trees))
print("Average Height = {:.1f}".format(average_height))
print("Shortest Tree = {}".format(height_of_shortest))
print("Tallest Tree = {}".format(height_of_tallest))
