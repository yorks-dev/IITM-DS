from functools import reduce


def are_anagrams(words: list) -> bool:
    """
    Check if all the given words are anagrams.

    Args: words - list[str]: list of lowercase words

    Return: bool - True if all the words are anagrams, else False.
    """
    first_word = set(words[0])
    # return set(map(lambda word: set(word) == first_word, words)) == {True}

    return reduce(
        lambda acc, word: acc
        and (len(word) == len(words[0]) and (set(word) == first_word)),
        words,
        True,
    )


print(are_anagrams(["listen", "silent", "enlist"]))
