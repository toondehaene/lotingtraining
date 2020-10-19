import random

names = ["Dries", "Raf", "Marijke", "Ward", "Sander", "Lieve", "Li", "Arnout", "Thomas", "Toon", "Irina"]
# names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
namescpy = names.copy()
result = []

weeksamt = 3
# getting absences
absences = [None] * weeksamt
print("current names in system: " + str(names))
for i in range(weeksamt):
    absences[i] = input("who is absent in week " + str(i + 1) + "? (separate by comma and space)").split(", ")

# seeding the random
var = input("give random seed: ")
if isinstance(var, str):
    seed = 0
    for char in var:
        seed += ord(char)
else:
    seed = var
random.seed(int(seed), 3)

# adding people in result
while len(result) < weeksamt * 6:  # fill until all weeks full
    if len(namescpy) == 0:
        namescpy = names.copy()  # keep picking people from list: once all people are picked once, start over
    nextlst = []
    while len(namescpy) != 0:
        nextlst.append(namescpy.pop(random.randint(0, len(namescpy) - 1)))  # pick a random nextperson
        closestsix = len(result) - len(result) % 6
        if nextlst[-1] not in list(set(result[closestsix:]) | set(absences[len(
                result) // 6])):  # if nextperson is already in this week or can't be present, break isn't reached
            nextperson = nextlst.pop(-1)  # pass nextperson out of the while loop
            for name in nextlst: namescpy.append(
                name)  # re-add the failed and not chosen names in case week changes in next iteration
            break

    result.append(nextperson)

# print results
# #writing to file, too lazy to implement relative paths so fill in you own depends on machine
# file = open("results.txt", "w")
# file.write("week 1: " + str(result[(1 - 1) * 6: 1 * 6]))
# file.write("week 2: " + str(result[(2 - 1) * 6: 2 * 6]))
# file.write("week 3: " + str(result[(3 - 1) * 6: 3 * 6]))
#
# file.close()
#
print("week 1: " + str(result[(1 - 1) * 6: 1 * 6]))
print("week 2: " + str(result[(2 - 1) * 6: 2 * 6]))
print("week 3: " + str(result[(3 - 1) * 6: 3 * 6]))
