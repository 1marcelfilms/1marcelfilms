ask = "y"
while ask != "N" or ask != "n":
    howmany = input("Until how much do you want to do 1+2+3+4... ect ")
    ans = 0
    counter = 0
    while counter < int(howmany):
        counter = counter + 1
        ans = ans + counter
    print(ans)
