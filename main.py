print("welcome to math calculator")
owo = "+"

number1 = input("number 1? ")
owo = input("? ")
number2 = input("number 2? ")

if owo == "+":
    math = float(number1) + float(number2)
else:
    if owo == "-": math = float(number1) - float(number2)
    else:
        if owo == ":" or "/": math = float(number1) / float(number2)
        else:
            if owo == "*" or "x": math = float(number1) * float(number2)
            else:
                if owo == "^": math = float(number1) ^ float(number2)



print(math)