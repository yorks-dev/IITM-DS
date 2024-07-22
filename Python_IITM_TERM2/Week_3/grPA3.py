task = input()


if task == "permutation":
    x = input()
    for i in x:
        for j in x:
            if i != j:
                print(i + j)

elif task == "sorted_permutation":
    x = input()
    for i in x:
        for j in x:
            if i != j and i < j:
                print(i + j)

elif task == "repeat_the_repeat":
    num = int(input())
    for i in range(1, num + 1):
        out = ""
        for j in range(1, num + 1):
            out += str(j)
        print(out)

elif task == "repeat_incrementally":
    num = int(input())
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

elif task == "increment_and_decrement":
    num = int(input())
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
