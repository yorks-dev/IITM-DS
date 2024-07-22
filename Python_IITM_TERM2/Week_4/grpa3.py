from operator import itemgetter
from os import sep


def index_of_first_occurance(row: list, elem):
    """
    Given a list find the index of first occurance of 1 in it
    """
    for index, i in enumerate(row):
        if i == elem:
            return index


def index_of_last_occurance(row: list, elem):
    """
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    """
    index = len(row) - 1
    while index >= 0:
        if row[index] == elem:
            return index
        index -= 1


def is_valid_coordinate(x: int, y: int, M):
    """
    Checks if the x,y is a valid corrdinate(indices) in the matrix M(list of list). Assume coordinates are non-negative
    """
    return (x >= 0 and x <= len(M) - 1) and (y >= 0 and y <= len(M[0]) - 1)


def valid_adjacent_coordinates(x: int, y: int, M):
    """
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    """
    return {
        (x1, y1)
        for x1, y1 in [
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x + 1, y),
        ]  # all the possible adjacent coordinates
        if is_valid_coordinate(x1, y1, M)
    }


def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    """
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    """
    x, y = curr_coords
    valid_coords = valid_adjacent_coordinates(x, y, M)
    if prev_coords:
        valid_coords.discard(prev_coords)

    for x1, y1 in valid_coords:
        if M[x1][y1] == value:
            return (x1, y1)

    return None  # if next coord with value does not exist


def get_path_coordinates(M):
    """
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    """
    x_start, x_end = len(M) - 1, 0
    y_start, y_end = index_of_last_occurance(M[-1], 1), index_of_first_occurance(
        M[0], 1
    )

    if y_start == -1 or y_end == -1:
        return []  # path not possible

    curr_coord = (x_start, y_start)  # first coord
    prev_coord = None
    path = [curr_coord]  # first coord

    while curr_coord != (x_end, y_end):
        next_coord = next_coordinate_with_value(curr_coord, 1, M, prev_coord)
        if next_coord == None:
            break
        path.append(next_coord)
        prev_coord = curr_coord
        curr_coord = next_coord

    return path


def print_path(M):
    path = get_path_coordinates(M)
    print(*path, sep="\n")


def alternate_path(M):
    path = get_path_coordinates(M)
    for index, (x1, y1) in enumerate(path):
        if (index + 1) % 2 == 0:
            M[x1][y1] = 2


def count_path(M):
    path = get_path_coordinates(M)
    for index, (x1, y1) in enumerate(path):
        M[x1][y1] = index + 1


def mirror_horizontally(M):
    path = get_path_coordinates(M)
    if path != None:
        for x1, y1 in path:
            M[x1][abs(y1 - (len(M[0]) - 1))] = 1


def mirror_vertically(M):
    path = get_path_coordinates(M)
    if path != None:
        for x1, y1 in path:
            M[abs(x1 - (len(M) - 1))][y1] = 1


# matrix = [[0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1]]
# mirror_horizontally(matrix)
# print(matrix)


# LAMBDA FUNCTION
sum1 = lambda x: [
    [j for j in range(i + 1) if j % 2 == 0] for i in range(0, x) if i % 2 == 0
]
print(sum1(10))

# FILTER FUNCTION
# keep is True only
list1 = {"A1": 40, "A2": 50, "A3": 60}
list2 = dict(filter(lambda item: item[1] >= 50, list1.items()))
print(list2)

# MAP

# 1 Squares of items in dict which are greater than 50
list1 = {"A1": 40, "A2": 50, "A3": 60, "A4": 80, "A5": 90, "A6": 100}
print(
    dict(
        map(
            lambda item: (
                (item[0], (item[1] ** 2)) if item[1] >= 50 else (item[0], (item[1]))
            ),
            list1.items(),
        )
    )
)

list2 = {
    item[0]: (item[1] ** 2) if item[1] >= 50 else item[1] for item in list1.items()
}
print(list2)
