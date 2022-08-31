from data_structures.hashtable import Hashtable
import pytest_watch


def left_join(synonyms, antonyms):
    result = []
    for key, value in synonyms.items():
        if antonyms.get(key):
            join_left = [key, value, antonyms.get(key)]
            result.append(join_left)

        else:
            result.append([key, value, 'NONE'])

    return result
