from code import interact


def n_hostile_pairs(L: list) -> int:
    """
    Given a list of integers, find the number of
    `hostile_pairs` in the given list.

    Two positive integers are called hostile
    if they have no common digits.

    Args:
        L: list[int] - numbers to check

    Return:
        int - number of hostile pairs
    """
    return len(
        {
            (L[i], L[j])
            for i in range(len(L))
            for j in range(i + 1, len(L))
            if set(str(L[i])).intersection(str(L[j])) == set()
        }
    )
