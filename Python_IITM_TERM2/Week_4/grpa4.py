# mapping
import enum
from functools import reduce


def is_greater_than_5(numbers: list) -> list:
    """Given a list of numbers, return a list of bools corresponding to whether the number is greater than 5"""
    return list(map(lambda number: number > 5, numbers))


# filtering
def filter_less_than_5(numbers: list) -> list:
    """Given an list of numbers, return a list of numbers that are less than 5"""
    return list(filter(lambda x: x < 5, numbers))


# aggregation with filtering
def sum_of_two_digit_numbers(numbers: list):
    """Given a list of numbers find the sum of all two_digit_numbers."""
    return reduce(lambda acc, i: acc + i if i >= 10 and i <= 99 else acc, numbers, 0)


# aggregation with mapping
def is_all_has_a(words: list) -> bool:
    """Given a list of words check if all words has the letter a(case insensitive) in it."""
    return reduce(
        lambda acc, word: acc and (True if "a" in str(word).lower() else False), words
    )


# enumerate
def print_with_numbering(items):
    """
    Print a list in multiple lines with numbering.
    Eg. ["apple","orange","banana"]
    1. apple
    2. orange
    3. banana
    """
    for index, item in enumerate(items):
        print(f"{index+1}. {item}")


# zip
def parallel_print(countries, capitals):
    """
    Print the countries and capitals in multiple line seperated by a hyphen with space around it.
    """
    print(*[" - ".join(x) for x in zip(countries, capitals)], sep="\n")


# key value list to dict
def make_dict(keys, values):
    """Create a dict with keys and values"""
    return dict(zip(keys, values))


# enumerate with filtering and map
def indices_of_big_words(words) -> list:
    """Given a list of words, find the indices of the big words(length greater than 5)."""
    # return [index for index, word in enumerate(words) if len(str(word)) > 5]
    # return map(lambda, enumerawords)
    return list(
        filter(
            lambda x: type(x) == int,
            list(
                map(
                    lambda word: word[0] if len(word[1]) > 5 else word[1],
                    enumerate(words),
                )
            ),
        )
    )


# zip with mapping and aggregation
def decode_rle(chars: str, repeats: list) -> str:
    """
    Create a string with i-th char from chars repeated i-th value of repeats number of times.

    Note rle refers to Run-length encoding
    """
    return reduce(
        lambda agg, i: agg + i, map(lambda x: x[0] * x[1], zip(chars, repeats))
    )


# list1 = [1, 2, 3, 4, 5, 6, 7, -1, -2]
# sum_positive = reduce(lambda acc, i: acc if i < 0 else acc + i, list1, 100)
# print(sum_positive)

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = list(map(lambda x: x * -1, list1))

# print(*["".join(x) for x in zip([str(x) for x in list1], [str(x) for x in list2])])

# print(sum_of_two_digit_numbers([8, 10, 11, 12, 1]))

# print(list(enumerate(["a", "b", "c"])))

# list1 = ["Ayush", "James", "A", "BC"]
# list1_map =

# list2 = (filter(lambda x: type(x) == str, list1),)
