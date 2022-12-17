the_file = open("day_1_input_1.txt")
elves = {}
counter = "0"
elves[counter] = 0
for line in the_file:
    line = line.rstrip()
    if line == "":
        counter = int(counter)
        counter += 1
        counter = str(counter)
        elves[counter] = 0
    else:
        elves[counter] += int(line) 
the_file.close()

total = 0
for i in range(3):
    max_calories_location = max(elves, key=elves.get)
    total += elves[max_calories_location]
    elves[max_calories_location] = 0 
print(total)