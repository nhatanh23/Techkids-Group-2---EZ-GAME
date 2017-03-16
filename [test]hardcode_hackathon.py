import random, string

def comparision(a, b):
    if a>= b:
        return True
    return False

def score(i):
    i += 1
    return i

def check_win_lose(c, tong, hieu, x, choose, i):
    if x == operation[0] and choose == "T":
        if c == tong:
            print(" ---YOU WIN--- ")
            score(i)
        if c != tong:
            print(" ---YOU LOSE--- ")
            print("Diem cua ban la: ", i)
            return False
    elif x == operation[0] and choose == "F":
        if c == tong:
            print(" ---YOU LOSE--- ")
            print("Diem cua ban la: ", i)
            return False
        if c != tong:
            print(" ---YOU WIN--- ")
            score(i)
    elif x == operation[1] and choose == "T":
        if c == hieu:
            print(" ---YOU WIN--- ")
            score(i)
        if c != hieu:
            print(" ---YOU LOSE--- ")
            print("Diem cua ban la: ", i)
            return False
    elif x == operation[1] and choose == "F":
        if c == hieu:
            print(" ---YOU LOSE--- ")
            print("Diem cua ban la: ", i)
            return False
        if c != hieu:
            print(" ---YOU WIN--- ")
            score(i)



while True:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 20)

    tong = a + b
    hieu = a - b

    operation = [" + ", " - "]

    x = random.choice(operation)
    i = 0

    if comparision(a, b):
        print(a, random.choice(operation), b, ' = ', c)
        choose = input("True or False (T,F)?: ").upper()
        check_win_lose(c, tong, hieu, x, choose, i)
    else:
        print(end="")




