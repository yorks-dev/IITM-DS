# Tasks

# Accumulation - Accumulating a final result
# sum_until_0: Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
# total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". Print the total price of all items.
# Filtering - Selecting based on a criterion
# only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). Print only those strings that end with "ed" or "ing" (case insensitive).
# reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.
# Mapping - Applying the same operation to different items
# double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
# odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
# Filter and Map - Applying an operation to selected items
# only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.
# Filter and Accumulate - Accumulating a result with selected items
# only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.

# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while n != 0:  # the terminal condition
        total += n  # add n to the total
        n = int(input())  # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while True:  # repeat forever since we are breaking inside
        line = input()
        if line == "END":  # The terminal condition
            break
        quantity, price = line.split()  # split uses space by default
        quantity, price = int(quantity), int(price)  # convert to ints
        total_price += quantity * price  # accumulate the total price
    print(total_price)

elif task == "only_ed_or_ing":
    word_list = []
    word = input()
    while word.upper() != "STOP":
        if word.lower().endswith(("ed", "ing")):
            word_list.append(word)

        word = input()
    print(*word_list, sep="\n")

elif task == "reverse_sum_palindrome":
    number_list = []
    num = input()
    while int(num) != -1:
        sum_num = int(num) + int(num[-1::-1])
        if str(sum_num) == str(sum_num)[::-1]:
            number_list.append(num)
        num = input()

    print(*number_list, sep="\n")

elif task == "double_string":
    line = input()
    line_list = []

    while len(line) != 0:
        line_list.append(line * 2)

        line = input()

    print(*line_list, sep="\n")

elif task == "odd_char":
    line = input()
    line_list = []

    while True:
        line_list.append(line[0::2])
        if line.endswith("."):
            break

        line = input()

    print(*line_list, sep=" ")

elif task == "only_even_squares":
    line = input()
    even_square_list = []

    while line != "NAN":
        if (even_square := (int(line) ** 2)) % 2 == 0:
            even_square_list.append(even_square)

        line = input()

    print(*even_square_list, sep="\n")

elif task == "only_odd_lines":
    line = input()
    line_list = []
    i = 1
    while line != "END":
        if i % 2 != 0:
            line_list = [line] + line_list

        i += 1
        line = input()
    print(*line_list, sep="\n")
