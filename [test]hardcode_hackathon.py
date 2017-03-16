import random, string

while True:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 20)
    tong = a + b
    hieu = a - b
    operation = [" + ", " - "]

    x = random.choice(operation)

    if a >= b:
        print(a, random.choice(operation), b, ' = ', c)
        choose = input("True or False (T,F)?: ").upper()
        if x == operation[0] and choose == "T":
            if c == tong:
                print(" ---YOU WIN--- ")
            else:
                print(" ---YOU LOSE--- ")
        elif x == operation[0] and choose == "F":
            if c == tong:
                print(" ---YOU LOSE--- ")
            else:
                print(" ---YOU WIN--- ")
        elif x == operation[1] and choose == "T":
            if c == hieu:
                print(" ---YOU WIN--- ")
            else:
                print(" ---YOU LOSE--- ")
        elif x == operation[1] and choose == "F":
            if c == hieu:
                print(" ---YOU LOSE--- ")
            else:
                print(" ---YOU WIN--- ")
    else:
        print()




