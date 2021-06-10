file = open("teams.txt", "r+")

teams = "PSG\n" + "Man-U\n" + "AC-Milan\n" + "Chelsea\n" + "West Ham\n"
for i in range(1,5):
     file.write(teams)
file.close()

file = open("teams.txt", "r") 
for line in file:
    for position, line in enumerate(file):
        if position in lines_to_read:
            print(line)
file.close()

#file = open("teams.txt", "r")

#line = file.readline()
#print(line)



