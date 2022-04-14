print("Welcome to TIC TAK TOE")

# ummmmmmmmmmmmmmmmmmm
# grid is 3x3 ?
a1 = "-"
a2 = "-"
a3 = "-"
b1 = "-"
b2 = "-"
b3 = "-"
c1 = "-"
c2 = "-"
c3 = "-"
# this makes grid printing into one command NYAA
def print_grid(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print(a1, a2, a3)
    print(b1, b2, b3)
    print(c1, c2, c3)
print_grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)

#input test
square = input("What square for player 1? a1 b2 c3 ect  ")
print(square)
square = "X"
a1 = "X"
print_grid(a1,a2,a3,b1,b2,b3,c1,c2,c3)