def is_pangram(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in s.lower():
        if i in alphabet:
            alphabet.remove(i)
    if len(alphabet) > 0:
        return False
    else:
        return True