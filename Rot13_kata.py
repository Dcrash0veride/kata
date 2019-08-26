import codecs
def rot13(message):
    coded_message = codecs.encode(message, "rot13")
    return coded_message