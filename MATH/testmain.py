import random
import time

# a = random.randint(0,10)
# b = random.randint(0,10)
# d = random.randint(0,20)
# c = a + b
#print(a, b, c, d)

def play_or_exit():
    while True:
        choice = input("Play or Exit (P/E): ").upper()
        if(choice == "P"):
            return True
        elif(choice == "E"):
            return False
        else:
            print("Choice again: ")

while play_or_exit():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    d = random.randint(0, 20)
    c = a + b
    print(a, b, c, d)

    start_time = time.time()
    click = input("True or False").upper()
    elapsed_time = time.time() - start_time

    if d == c and (elapsed_time < 2) and (click == "T"):
        print("win")
    elif d != c and (elapsed_time < 2) and (click == "F"):
        print("win")
    else:
        print("lose")