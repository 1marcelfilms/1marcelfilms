print("Welcome to TIC TAK TOE")

# this makes grid printing into one command NYAA
#       a1   a2   a3   b1   b2   b3   b4   b5   b6
grid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#        0    1    2    3    4    5    6    7    8

# To print b2 do 'print grid[4]'    # To print entire grid 'print_grid(grid)'
def print_grid(grid):
    print(grid[0], grid[1], grid[2])
    print(grid[3], grid[4], grid[5])
    print(grid[6], grid[7], grid[8])

print_grid(grid)
counter = 9
while counter > 0:
    counter = counter - 1

    if float(counter/2) - int(counter/2) == 0:
        player = "X"
    else:
        player = "O"



    #input test
    # wtf am i doing ?
    userInput = input("Player "+ player + " What square to edit? a1, b2, c3 ect? ")

    if "a" in userInput:
        x = 0
    if "b" in userInput:
        x = 3
    if "c" in userInput:
        x = 6


    y = userInput[1]

    if int(y) > 3:
        print("REALLY PUNISH!")
        userIQ = 0 / 0
    total = int(x) + int(y) - 1
    #print(total)
    if grid[total] == "-":
        grid[total] = player
    else:
        print("cheaters lose a turn")


    print_grid(grid)
print("game is now over")
