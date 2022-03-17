loop = "Y"
while loop == "y" or "Y" or "":
    print("welcome to math calculator v2")

    number1 = input("number 1? ")
    owo = input("? ")
    number2 = input("number 2? ")

    if owo == "+":
        math = float(number1) + float(number2)
    else:
        if owo == "-":
            math = float(number1) - float(number2)
        else:
            if owo == ":" or "/" and number2 == "0":
                math = "USER ERROR"; print("wtf are you doing?")
            else:
                if owo == ":" or "/" and number2 != "0":
                    math = float(number1) / float(number2)
                else:
                    if owo == "*" or owo == "x":
                        math = float(number1) * float(number2)
                    else:
                        if owo == "^": math = float(number1) ^ float(number2)
                        else:
                            print("cant do that dave")

    print("The anwser is: " + str(math)); print()
    loop = input("Try again? Y/n")
