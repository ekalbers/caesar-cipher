import nltk
from nltk.corpus import words, names
import ssl

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(string, shift):
    new_string = ''
    for char in string:
        if char in upper or char in lower:
            if char in lower:
                index = lower.index(char)
            else:
                index = upper.index(char)
            index += shift
            if index > 25:
                index -= 26
            if char in lower:
                new_string += lower[index]
            else:
                new_string += upper[index]
        else:
            new_string += char
    return new_string


def decrypt(string, shift):
    new_string = ''
    for char in string:
        if char in upper or char in lower:
            if char in lower:
                index = lower.index(char)
            else:
                index = upper.index(char)
            index -= shift
            if index < 0:
                index += 26
            if char in lower:
                new_string += lower[index]
            else:
                new_string += upper[index]
        else:
            new_string += char
    return new_string


def crack(string):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
    nltk.download('words', quiet=True)
    nltk.download('names', quiet=True)
    word_list = words.words()
    name_list = names.words()
    top_counter = 0
    top_string = ''
    for x in range(25):
        decrypted_string = decrypt(string, x)
        lst = decrypted_string.split(' ')
        counter = 0
        for val in lst:
            if val in word_list or val in name_list:
                counter += 1
        if counter == len(lst) - 1:
            return decrypted_string
        elif counter > top_counter:
            top_counter = counter
            top_string = decrypted_string
    if top_counter < len(top_string.split(' ')) - 3:
        return ''
    else:
        return top_string


if __name__ == '__main__':
    pass
