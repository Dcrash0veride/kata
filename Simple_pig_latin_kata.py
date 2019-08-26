def pig_it(text):
    words = text.split()
    sentence = ""
    for word in words:
        if '!' in word[0] or '?' in word[0]:
            pigd = word[1:] + word[0]
            sentence += " " + pigd
        else:
            pigd = word[1:] + word[0] + 'ay'
            sentence += " " + pigd
    return sentence.strip()