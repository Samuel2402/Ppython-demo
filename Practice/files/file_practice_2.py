teams = ['Manchester United', 'Chelsea', 'Manchester City', 'Crystal Palace', "West Ham"]

file = open('teams_new.txt', 'w+')
for name in teams:
    file.write(name + "\n")
file.close()

file = open('teams_new.txt', 'r') 
lines_to_read = [0,3]
for line in file:
    for position, line in enumerate(file):
        if position in lines_to_read:
            print(line)
file.close()