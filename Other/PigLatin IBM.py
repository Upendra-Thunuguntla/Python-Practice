import re

VOWELS = ['a', 'e', 'i', 'o', 'u']
TAIL = 'ay'

def translate(word):
    op = []   # List of converted words to Pig Latin
    if len(word.split()) >1:
        return "Invalid input"
    else:
        idx = re.search("[aeiou]", word, re.IGNORECASE)

        if idx.start() == 0:
            op.append(word +"-y" +TAIL)

        elif word[idx.start()] == 'u' and word[idx.start() - 1]  == 'q':
            op.append(word[idx.start() + 1:] + word[:idx.start() + 1] + TAIL)

        else:
            op.append(word[idx.start():] + "-"+word[:idx.start()] + TAIL)

    return " ".join(op)

print(translate(input()))