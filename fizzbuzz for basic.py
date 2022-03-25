#if  the number is divisible by 3  then print "Fizz"
#  else if (theNumber is divisible by 5) print "Buzz"

times = input("Until how many? ")

counter = 0
while counter < int(times):
    counter = counter + 1
    #print(counter)


    fizz = counter / 3
    buzz = counter / 5
    #print(fizzbuzz)
    fizzcheck = float(fizz) - int(fizz)
    buzzcheck = float(buzz) - int(buzz)

    if fizzcheck + buzzcheck == 0:
        print(counter * 10, 'print "fizzzbuzz"')
    else:
        if fizzcheck == 0:
            print(counter * 10, 'print "fizz" ')
        else:
            if buzzcheck == 0:
                print(counter * 10, 'print "buzz" ')
            else:
                print(counter * 10, "print", counter)



