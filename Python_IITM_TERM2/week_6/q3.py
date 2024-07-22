from functools import reduce
from math import inf


def is_num_sorted(num) -> bool:
    """
    Check if a number is sorted.
    sorted means the digits of a number are sorted in ascending order.
    Eg. 1468 - sorted , 4948 - not sorted.

    Argument: num: int
    Return: bool
    """
    num = str(num)
    return reduce(
        lambda acc, el: acc and (True if el[1] >= num[el[0] - 1] else False),
        enumerate(num[1:], start=1),
        True,
    )


def sorted_num_count(nums: list) -> int:
    """
    Given a list of nums(int) find the count of sorted numbers in the list.

    Arguments: nums - list[int]
    Return: count - int
    """
    return reduce(lambda acc, x: acc + 1 if is_num_sorted(x) else acc, nums, 0)


def common_substring(words: list) -> list:
    """
    Given a list of words check whether there is a word in words
    that is a substring of all other words.
    If there is a word return that word else return None

    Hint: only the smallest word can be a substring of all other words.

    Arguments: words - list[str]
    Return: common_substr_word - str
    """

    shortest_word = min(words, key=len)
    words.remove(shortest_word)
    is_common_substring = True

    for word in words:
        if shortest_word not in word:
            is_common_substring = False
            break

    if is_common_substring == True:
        return shortest_word
    else:
        return None


def is_valid_phone_number(phone_no: int) -> bool:
    """
    Check if a number is valid for a specific operator.

    A phone number is valid if
        - it has 10 digits
        - should begin with 98123
        - same digit should not occur more that 5 times.
    """
    number = str(phone_no)
    num_dict = {i: number.count(i) for i in set(number)}

    return (
        max(num_dict.values()) <= 5 and len(number) == 10 and number.startswith("98123")
    )


def validate_phone_numbers(phone_nos: list) -> dict:
    """
    Given a list of phone numbers, create a dict with
    phone numbers as keys and the string "VALID" or "INVALID"
    depending on the validity of the phone number as described by the above funtion.

    Arguments: phone_nos - list
    Return: validity_dict - dict[int,str]
    """
    return {
        number: ("VALID" if is_valid_phone_number(number) == True else "INVALID")
        for number in phone_nos
    }


def get_election_winner(votes: dict) -> str:
    """
    Given a dictionary with candidate name as key and number of votes as values,
    Find the winner of the election who has the maximum votes

    Arguments: votes - dict[str, int]
    Return: winner - str
    """
    return max(votes, key=votes.get)


def misspelt_words(vocab: str, sentence: str) -> list:
    """
    Given a comma separated string of vocabulary,
    and a space separated string sentence,
    return a list of misspelt words in the order they occur in the sentence.

    The words which are not in the vocabulary are considered misspelt.

    Arguments:
        vocab - str: comma separated string with vocabulary
        sentence - str: space separated string of sentence
    Return:
        misspelt_words - list
    """
    return [word for word in sentence.split(" ") if word not in vocab.split(",")]


def count_sock_pairs(sock_colors: list) -> int:
    """
    Given a list of sock colors representing the color of each sock,
    find the number of sock pair (both having same color) is there.
    Eg. ["red","blue","green","green","red","green","red","red","blue","black"]
    2 red+ 1 green+ 1 blue = 5 pairs

    Arguments: sock_colors - list: of sock colors
    Return: number of pairs of sock - int
    """
    sock_dict = {i: sock_colors.count(i) for i in set(sock_colors)}
    sock_dict = dict(
        map(
            lambda sock: (
                sock[0],
                (sock[1] / 2 if sock[1] % 2 == 0 else (sock[1] - 1) / 2),
            ),
            sock_dict.items(),
        )
    )
    return int(sum(sock_dict.values()))


def is_vowely(word: str) -> bool:
    """
    Check if a given word is vowely. A word is vowely if
    - it has all the vowels in it.
    - the vowels occur in ascending order.

    Assume no letter repeats in the given word.

    Eg. abecidofu - vowely, tripe - not vowely, eviaoqu - not vowely

    Argument: word - a string with no letter repeated
    Return: bool

    Hint: if the non-vowels are removed from the word, it would be just aeiou
    """
    # return "aeiou" == "".join([i for i in word if i.lower() in "aeiou"])
    return "aeiou" == "".join(filter(lambda x : x in "aeiou", word))



def vowely_count(words: list) -> int:
    """
    Given a list of words find the number of vowely words from the list.

    Arguments: words :list[str]

    Return: int - number of vowely words
    """
    return reduce(lambda acc, x: acc + 1 if is_vowely(x) else acc, words, 0)


def format_name(first: str, middle: str, last: str) -> str:
    """
    Given three lower case parts of name,
    return the full name with first letter capitalized in each part.

    Note that middle name can be empty.
    """
    
    return first[0].upper()+first[1:] + (" " if len(middle) == 0 else " " + middle[0].upper()+middle[1:] + " " )+ last[0].upper()+last[1:]

def double_palindromes(n: int) -> list:
    """
    Given a number n, find all the positive integers till n (including)
    that are double_palindrome. A number is double palindrome if
    it is a palindrome and its square is a palindrome.

    Eg.
    8 - palindrome, not double palindrome
    11 - palindrome and double palindrome
    12 - not palindrome and not double palindrome

    Arguments: n - int: range of numbers to search
    Return: list of integers which are double palindrome in the ascending order
    """

    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    return [i for i in range(1, n + 1) if is_palindrome(i) and is_palindrome(i ** 2)]



def scores_spx(kakashi_moves: list, guy_moves: list):
    """
    Given the series of moves played by Kakashi and Guy in a Stone-Paper-Scissor game,
    find the scores of Kakashi and guy respectively.
    Rules - Stone beats Scissor, Scissor beats Paper and Paper beats Stone
    Score - Number of times won
    Symbols - Stone - S, Paper - P, Scissor - X

    Arguments:
    kakashi_moves and guy_moves - list of moves where each move
        is a string corresponding to the symbol

    Return: kakashi_score:int , guy_score:int
    """
    
    results = {'S': 'X', 'X': 'P', 'P': 'S'}
    k_score, g_score = 0, 0
    for k, g in zip(kakashi_moves, guy_moves):
        if results[k] == g:
            k_score += 1
        elif results[g] == k:
            g_score += 1
    return k_score, g_score
    # return k_score, g_score


# print(is_num_sorted(12689))
# print(sorted_num_count([1, 2, 3, 121, 23, 32, 450]))
# print(common_substring(["mantle", "man", "mango", "raman", "manager", "manage"]))

# print(count_sock_pairs(["red", "red", "yellow", "red", "red", "yellow"]))

# print(is_vowely("abecidofu"))
# words = ['abecidofu', 'tripe', 'abxyepiforu', 'uredfzxn', 'aqetiol', 'eviaoqu']
# print(vowely_count(words))
# print(format_name(first="Ayush", middle="Italia", last="Dutta"))