hardsounds = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v' ,'x', 'z', 'r'] # these won't be ignored
softsounds = ['a', 'e', 'i', 'o', 'u', 'y', 'w'] # these 'soft' sounds are ignored
ignored = ['w', 'h', 'r',] #if this is not placed at the start or the end, it will be deleted

nuances = (
    ('sha', 'tia'),
    ('f', 'ph'),
    ('c', 'k'),
    ('c', 'q'),
    ('u', 'oo'),
    ('e', 'i'),
    ('a', 'e'),
    ('s', 'z'),
    ('c', 'x')
)

corresponding = [
    ('1', 'i', 'l', '!'),
    ('2', 'r'),
    ('3', 'e'),
    ('4', 'a', '@'),
    ('5', 's', '$'),
    ('6', 'b'),
    ('7', 't', '+'),
    ('0', 'o'),
    ('(', 'c')
]

corresponding2 = {
        'i': ['1', 'i', 'l', '!'],
        'l': ['1', 'i', 'l', '!'],
        'r': ['2', 'r'],
        'e': ['3', 'e'],
        'a': ['4', 'a', '@'],
        's': ['5', 's', '$'],
        'b': ['6', 'b'],
        't': ['7', 't', '+'],
        'o': ['0', 'o'],
        'c': ['(', 'c']
}

__version__ = 1.0
__author__ = "Signetar, 2022"
__meow__ = "meowwww owo"

def compare(typed_char, target_char, corresponding=corresponding2) -> bool:
    """Returns whether the typed character could stand in for the target character."""

    if target_char in corresponding.keys():
        return typed_char in corresponding[target_char]
    return target_char == typed_char


def average_stuck_keyboard_enjoyer(typed, target, corresponding=corresponding2) -> bool:
    """
    Returns True if what was typed is the target word, when recurring characters
    and stand-ins are disregarded. (sorry in advance)
    """
    typed = typed.lower()
    target = target.lower()
    i = 0  # target pointer
    j = 0  # typed pointer
    if len(target) == 0 and len(typed) != 0:
        return False
    if len(typed) < len(target):
        return False
    while j < len(typed):
        if not compare(typed[j], target[i], corresponding):
            return False
        if i == len(target)-1:
            break
        if j == len(typed)-1:
            return False
        if compare(typed[j+1], target[i+1], corresponding):
            j += 1
            i += 1
        elif compare(typed[j+1], target[i], corresponding):
            j += 1
        else:
            return False

    while j != len(typed):
        if not compare(typed[j], target[-1], corresponding):
            return False
        j += 1

    return True



def __ingroup(inputSet, groups) -> bool:
    """
    Returns True if all elements in inputSet are in group.
    """
    inputSet = set(inputSet)
    if len(inputSet) == 1:
        return True
    for x in groups:
        if inputSet.issubset(set(x)):
            return True  
    return False
    
def text_variation(typed, target, groups=corresponding) -> float:
    typed, target = typed.lower(), target.lower()
    typed_list = []
    string = ''
    for i in range(len(typed)):
        if len(string) == 0:
            string = typed[i]
        elif __ingroup(set((typed[i], string[-1])), groups):
            string += typed[i]
        else:
            typed_list.append(string)
            string = typed[i]
    typed_list.append(string)
    # same thing for target
    target_list = []
    string = ''
    for i in range(len(target)):
        if len(string) == 0:
            string = target[i]
        elif (target[i] == string[-1]):
            string += target[i]
        else:
            target_list.append(string)
            string = target[i] 
    target_list.append(string)
    # zip
    zipped = list(zip(typed_list, target_list))
    matrix = []
    for x in zipped:
        matrix.append(__ingroup([char for char in "".join([y for y in x])], groups=groups))

    return matrix.count(True) / len(typed_list)

def __delete_softsounds(word, softsounds=ignored) -> str:
    word = word.lower()
    first = word[0]
    last = word[-1]

    # remove first and last from word
    word = word[1:-1]
    for x in word:
        if x in softsounds:
            word = word.replace(x, '')
    return first + word + last

#wreck 

def strip_consonants(word, consonants=hardsounds, replace_nuances=True) -> str:
    word = word.lower()
    if replace_nuances==True:
        for nuance in nuances:
            if nuance[1] in word:
                word = word.replace(nuance[1], nuance[0])
    word = [char for char in word]
    toremove=[]
    for x in word:
        if x in consonants:
            toremove.append(x)  
    for x in toremove:
        word.remove(x)
    return word

    
def __latent(word, delete_ignored=True, softsounds=softsounds, ignored=ignored) -> str:
    word = word.lower()
    for nuance in nuances:
        if nuance[1] in word:
            word = word.replace(nuance[1], nuance[0])
    if delete_ignored:
        word = __delete_softsounds(word, ignored)
    output = []
    string = ''
    for i in range(len(word)):
        if len(string) == 0:
            string = word[i]
        elif word[i] == string[-1]:
            string += word[i]
        else:
            output.append(string)
            string = word[i]
    output.append(string)

    output = ["".join(list(set(x))) for x in output]

    toremove = []
    for x in output:
        if x in softsounds:
            toremove.append(x)

    for x in toremove:
        output.remove(x)
    
    return [x for x in output if x != '']



def __zip(one, two):
    output = []
    x = max(len(one), len(two))
    for i in range(x):
        output.append((one[i] if i < len(one) else '', two[i] if i < len(two) else ''))
    return output

def pronunciation_similarity(word1, word2, delete_ignored=True, softsounds=softsounds, ignored=ignored) -> float:
    """
    Takes in two words made entirely of alphabet characters and returns a float, similarity between 0 and 1 based on how they sound.
    """

    # check if there are characters that aren't alphabets in word1 and word2
    if not all(x.isalpha() for x in word1) or not all(x.isalpha() for x in word2):
        return {"Similarity" : 0, "Error" : "One or more of the words contains non-alphabet characters."}

    word1v = __latent(word1, delete_ignored, softsounds, ignored)
    word2v = __latent(word2, delete_ignored, softsounds, ignored)

    maximum = max(len(word1v), len(word2v))
    minimum = min(len(word1v), len(word2v))


    output = {}

    output["Similarity"] = [x[0]==x[1] for x in __zip(word1v, word2v)].count(True) / maximum
    output["Confidence"] = minimum / maximum
    return output

def novar(typed, target, groups=corresponding, softsounds=softsounds, ignored=ignored, delete_ignored=True,) -> dict:
    """
    A collection of novar's functions.
    """
    output = {}
    output["text_variation"] = {"Similarity" : text_variation(typed, target, groups)}
    output["pronunciation_similarity"] = pronunciation_similarity(typed, target, softsounds=softsounds, ignored=ignored, delete_ignored=delete_ignored)
    return output
