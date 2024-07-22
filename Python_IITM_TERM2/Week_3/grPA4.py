# this is to ensure that you cannot use the built in any, all and min function for this exercise but you can use it in the OPPEs.
any = None
all = None
min = None

task = input()


if task == "factors":
    number = int(input())
    if number > 0:
        for i in range(1, number + 1):
            if number % i == 0:
                print(i)

elif task == "find_min":
    number = int(input())
    if number > 0:
        minimum = float("inf")
        for i in range(5):
            num = int(input())
            if num < minimum:
                minimum = num
        print(minimum)

elif task == "prime_check":
    number = int(input())
    if number > 1:
        prime = True
        for i in range(2, int(number)):
            if number % i == 0:
                prime = False
                break
        print(prime)
    else:
        print(False)

elif task == "is_sorted":
    s = input()
    if len(s) > 0:
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                print("False")
                break
        else:
            print("True")

elif task == "any_true":
    number = int(input())
    for i in range(number):
        num = int(input())
        if num % 3 == 0:
            print("True")
            break
    else:
        print("False")

elif task == "manhattan":
    x_coord, y_coord = 0, 0
    while True:
        move = input().strip().upper()
        if move == "UP":
            y_coord += 1
        elif move == "DOWN":
            y_coord -= 1
        elif move == "LEFT":
            x_coord -= 1
        elif move == "RIGHT":
            x_coord += 1
        elif move == "STOP":
            print(abs(x_coord) + abs(y_coord))
            break
