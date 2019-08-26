def remove_duplicate_words(s):
    single_words = []
    words = s.split()
    for word in words:
        if word in single_words:
            pass
        else:
            single_words.append(word)

    my_string = ' '.join(single_words)
    return my_string