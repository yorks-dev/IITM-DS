# accept a string of comma seperated words.
# find word that is substrings of all the other words

# "Apple","Applea","App", "Ap"


def word_substring(words: str):
    word_list = words.split(",")
    for idx, word in enumerate(word_list):
        all_sub = True
        for another_word in word_list[:idx] + word_list[idx + 1 :]:
            if word not in another_word:
                all_sub = False
                break
        if all_sub:
            return word
    return None


print(word_substring("Apple,Applea,App,Ap"))
