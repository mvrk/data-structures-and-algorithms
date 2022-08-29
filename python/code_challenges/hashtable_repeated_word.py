# from data_structures.hashtable import Hashtable
import re


def first_repeated_word(word):
    dic = set()
    reg = re.compile('[^a-zA-Z ]')
    words = reg.sub('', word).lower().split()
    for word in words:
        if word in dic:
            return word
        else:
            dic.add(word)
