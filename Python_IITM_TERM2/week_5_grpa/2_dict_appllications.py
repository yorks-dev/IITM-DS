from functools import reduce


def total_price(fruit_prices: dict, purchases) -> float:
    """
    Compute the fruit prices give the quantity of each fruit. Do not use the sum function.

    Arguments:
    fruit_prices: dict - fruit name as key and price as value
    purchases: l] - as list oist[tuplef tuples of (fruit, quantity)

    Return:
    total_price: float
    """
    return sum(fruit_prices.get(item, 0) * qty for item, qty in purchases)


def total_price_no_loops(fruit_prices: dict, purchases) -> float:
    """
    Compute the total price without loops.
    """
    return sum(fruit_prices[fruit] * quantity for fruit, quantity in purchases)  # type: ignore


def find_cheapest_fruit(fruit_prices: dict):
    """
    Find the cheapest fruit from the fruit_prices dict, do not use min function

    Arguments:
    fruit_prices: dict - fruit name as key and price as value

    Return:
    cheapest_fruit: str - the fruit with the lowest price
    """
    pass


def find_cheapest_fruit_no_loops(fruit_prices: dict) -> str:
    """
    Find the cheapest fruit using min function. Do not use loops
    """
    return min(fruit_prices)


# grouping
def group_fruits(fruits: list):
    """
    Group the fruits based on the first letter of the names. Assume first letters will be upper case.

    Arguments:
    fruits - list: list of fruit names

    Return:
    dict: dict with the first letters as keys and list of fruits sorted in ascending order as values.
    """

    dict_fruit = {}
    for fruit in fruits:
        if fruit[0] not in dict_fruit.keys():
            dict_fruit[fruit[0]] = [fruit]
        else:
            dict_fruit[fruit[0]].append(fruit)

    return dict_fruit


# binning
def bin_fruits(fruit_prices):
    """
    Classify the fruits as cheap, affordable and costly based on the fruit prices. Create a dictionary with the classification as keys and a set of fruits in that category.

    cheap - less than 3 (not inclusive)
    affordable - between 3 and 6 (both inclusive)
    costly - greater than 6 (not inclusive)

    Arguments:
    fruit_prices: dict - dictionary with fruits as keys and prices as values

    Return:
    binned_fruits: dict - dictionary with category as key and a set of fruits in that category as values.
    """
    binned_fruits = {i: set() for i in ["cheap", "affordable", "costly"]}

    for fruit, price in fruit_prices.items():
        if price < 3:
            binned_fruits["cheap"].add(fruit)
        elif 3 <= price <= 6:
            binned_fruits["affordable"].add(fruit)
        else:
            binned_fruits["costly"].add(fruit)


print(
    total_price(
        {"Apple": 2.0, "Banana": 3.0, "Orange": 4.0, "Grapes": 3.0, "Papaya": 5.0},
        [("Apple", 3), ("Orange", 5), ("Grapes", 4)],
    )
    == 38.0
)

print(group_fruits(["Apple", "Mango", "Avocardo", "Banana"]))

a = [1, 2, 3, 4, 5]
b = [8, 9, 10, 11, 12]
print(dict(zip(map(lambda x: str(x), a), b)))

a = [(1, 2), (3, 4), (5, 6), (7, 8)]
b = {"a": [(1, 2), (3, 4)], "b": [(1, 2), (5, 6)]}

for key in b.keys():
    b[key] = [tuple(sorted(i, reverse=True)) for i in (set(a) - set(b[key]))]

print(list(map(lambda x: tuple(sorted(x, reverse=True)), a)))

print(b)


def indices_of_big_words(words) -> list:
    """Given a list of words, find the indices of the big words(length greater than 5)."""
    # return list(
    #     filter(
    #         lambda x: type(x) == int,
    #         map(lambda x: x[0] if len(x[1]) > 5 else x[1], enumerate(words)),
    #     )
    # )

    return list(map(lambda x: x[0], filter(lambda y: len(y[1]) > 5, enumerate(words))))


print(indices_of_big_words(["AAAAAA", "AA", "BBBBBA"]))


dict1 = {
    "A": (1, 1, 1, 2, 3, 4, 5, 5, 5),
    "B": (1, 2, 2, 4, 5, 3),
    "C": (2, 2, 3, 5, 6),
    "D": (1, 2, 2, 0),
}

num_1_list = {}
{num_1_list.setdefault(v.count(1), []).append((k, v)) for k, v in dict1.items()}

print(dict(map(lambda x: (x[0], dict(x[1])), num_1_list.items())))
print(num_1_list)


student_data = {
    "A": {"Math": 80, "Chem": 90},
    "B": {"Math": 90, "Chem": 88},
    "C": {"Math": 99, "Chem": 60},
}

print(dict(sorted(student_data.items(), key=lambda x: x[1]["Math"], reverse=True)))


batsman_list = [
    ("Dhoni", 100, "CSK"),
    ("Koholi", 88, "MI"),
    ("A", 66, "MI"),
    ("B", 78, "CSK"),
    ("D", 88, "JPK"),
    ("E", 99, "DPRK"),
]

team_score = {}
{team_score.setdefault(team, []).append(score) for batsman, score, team in batsman_list}


team_score = dict(map(lambda x: (x[0], sum(x[1])), team_score.items()))
print(team_score)
print(list(sorted(team_score.items(), key=lambda item: item[1]))[:2])
