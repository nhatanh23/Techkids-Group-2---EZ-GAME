import random, string, time

def comparision(a, b):
    if a >= b:
        return True
    return False

def check_win_lose(time, choose, c, x, score, play):
    #win
    if time <= 10:
        if c == x and choose == "T":
            print(" YOU WIN ")
        elif c != x and choose == "F":
            print(" YOU WIN ")
        else:
            print(" YOU LOSE ")
    else:
        print(" YOU LOSE ")
    return score

def print_operation(x, a, b, c):
    if x == operation[0]:
        print(a, " + ", b, ' = ', c)
    elif x == operation[1]:
        print(a, " - ", b, ' = ', c)

score = 0

while True:
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        d = random.randint(0, 20)

        operation = [a + b, a - b]

        x = random.choice(operation)

        number_list = [d, x]
        c = random.choice(number_list)

        if comparision(a, b):
            print_operation(x, a, b, c)

            start_time = time.time()
            choose = input("True or False? ").upper()
            elapsed_time = time.time() - start_time

            check_win_lose(elapsed_time, choose, c, x, score)

            print("Your current score: ", score)
            print("Your answer time:", elapsed_time)
            print()
        else:
            print(end="")