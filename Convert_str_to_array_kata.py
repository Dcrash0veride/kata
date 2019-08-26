def string_to_array(s):
    my_list = []
    words = s.split(" ")
    print(words)
    for word in words:
        my_list.append(word)
    return my_list