__author__ = 'bliang'


def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)
