# Warm Up - fix this function.

# This function is supposed to take a list of words and return a new 
# list with the one-letter words removed. It's not doing that. First,
# run the function with some test word lists to see what it is doing
# then fix it so it has the desired output.

test = ["A", "B", "Boy", "Tree", "D"]


def remove_short_words(word_list):
    for i, word in enumerate(word_list):
        if len(word) <= 1:
            word_list.remove(i)
    print(word)
    print(len(word))
    return word_list


print(remove_short_words(test))

