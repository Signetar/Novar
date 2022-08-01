# Novar (v1.0)

A short name for NoVariations, made to be able to detect any v4r1ati0ns in text.

[![Downloads](https://pepy.tech/badge/novar)](https://pepy.tech/project/novar)

## Table of Contents
1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Simple Usage](#Simple-Usage)
4. [Similarities of two strings with variations](#Text-Similarity)
5. [Pronunciation similarities of two strings](#Pronunciation-Similarity)
6. [Customizations](#Customizations)

## Introduction
Novar is a collection of functions that could be used for chat moderation and NLP. It is also highly customizable, allowing users to configure the functions.

Novar has five functions, which are: `novar`, `compare`, `average_stuck_keyboard_enjoyer`, `text_variation`, and `pronunciation_similarity`. Besides those, there are other accessible functions which were made for the functionality of `novar`, which you can find in the source code.

If you have anything to ask me directly, e-mail me or add me on Discord at Signetar#3735


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Novar.

```bash
pip install novar
```
## Simple Usage
I've combined (nearly) all functionalities of Novar into one function for accessibility.
```python
novar(typed, target, groups=corresponding, softsounds=softsounds, ignored=ignored, delete_ignored=True) -> dict
```
### Parameters
- *typed* : The 'typed' word. String that has variations in it.
- *target* : The original string that consists of alphabets only. It doesn't have any variations.
- *groups* : A list of tuples that have the same meaning in a string with variations, it's set to ```corresponding``` by default.
- *softsounds* : A list of characters that have 'soft' sounds. This includes vowels, and it determines which characters should be removed when finding the pronunciation similarities of two strings.
- *ignored* : A list of characters that get ignored when placed after a vowel.
- *delete_ignored* : Whether to delete characters in `ignored` or not when determining pronunciation similarity. It's set to ```True``` by default.

### Examples
```python
import novar

one, two = "4stat111ne33e", "astatine"
print(novar.novar(one, two))
```
Which would return:
```
{
    'text_variation' : {
        'Similarity' : 1.0
    },
    'pronunciation_similarity' : {
        'Similarity' : 0,
        'Error': 'One or more of the words contains non-alphabet characters.'
    }
}
```
As *4stat111ne33e* is simply a variation (with a lot of special characters and spams) of *astatine*, `text_variation` is 1.0, meaning they are the same. However, as it contained special characters, `pronunciation_similarity`, a function designed for strings that only consist of alphabetic characters, would return an error.

For another use case:
```python
one, two = "accede", "exceed"
print(novar.novar(one, two))
```
Would return
```
{
    'text_variation' : {
        'Similarity' : 0.0
    },
    'pronunciation_similarity' : {
        'Similarity' : 1.0,
        'Confidence' : 1.0
    }
}
```
As *accede* and *exceed* are two different words, `text_variation` would be 0, while `pronunciation_similarity` would be 1.0 with the confidence of 1.0, as the two words are homophones.

## Text Similarity
There are two functions to perform this task, which are `average_stuck_keyboard_enjoyer` (made by 
screechingviolet) and `text_variation`. Keep in mind that both functions, despite working differently, can both handle recurring characters and special characters. 
The descriptions and use cases of both functions are shown below:

### `Average Stuck Keyboard Enjoyer`
Returns True if what was typed is the target word, when recurring characters and stand-ins are disregarded. 
### Parameters
- *typed* : The 'typed' word. String that has variations in it.
- *target* : The original string that consists of alphabets only. It doesn't have any variations.
- *corresponding* : A dictionary it uses to convert special characters to alphabetic characters. Set to *corresponding2* by default.
```python
print(novar.average_stuck_keyboard_enjoyer('v4r14710ns', 'variations'))
```
Would return:
```
True
```

### `Text Variation`
Returns a float value between 0 and 1 based on how similar `typed` is to `target`.
### Parameters
- *typed* : The 'typed' word. String that has variations in it.
- *target* : The original string that consists of alphabets only. It doesn't have any variations.
- *groups* : Set to `corresponding` by default, a group of characters that have the same meaning in a string with variations.
```python
print(novar.text_variation('v4r14710ns', 'variations'))
```
Would return
```
{'Similarity': 1.0}
```
And even with recurring special characters,
```python
print(novar.text_variation('v4r1ationx', 'variations'))
print(novar.text_variation('v4444aAar1ationx', 'variations'))
```
The output would be the same.
```
{'Similarity': 0.9}
{'Similarity': 0.9}
```

## Pronunciation Similarity
Although there are other algorithms such as Soundex, novar presents a different method to determine how similar two strings of characters sound when pronounced.

`Similarity` refers to how similar two strings sound, and `Confidence` shows how likely it is for the similarity score to be correct.

### Usage
```python
print(novar.pronunciation_similarity("masked", "masqued"))
print(novar.pronunciation_similarity("cue", "queue"))
```
```
{'Similarity': 1.0, 'Confidence': 1.0}
{'Similarity': 1.0, 'Confidence': 1.0}
```
What you see above are homophones, words that sound the same despite being spelt differently. Here are more examples:
```python
print(novar.pronunciation_similarity("nature", "mature"))
print(novar.pronunciation_similarity("elephant", "jellyfish"))
```
```
{'Similarity': 0.5, 'Confidence': 1.0}
{'Similarity': 0.0, 'Confidence': 0.8}
```
### Disclaimer
This function is not compatible with numeric or special characters, only alphabetic. Hence, when a string with numbers or special characters is inputted, it would simply return an error.
```python
print(novar.pronunciation_similarity("impossible", "3mpossible"))
```
```
{'Similarity': 0, 'Error': 'One or more of the words contains non-alphabet characters.'}
```
But by using the `compare` function that comes with novar, you can try converting such characters to alphabetic characters.
```python
print(novar.pronunciation_similarity("impossible", "empossible"))
```
```
{'Similarity': 1.0, 'Confidence': 1.0}
```
## Customizations
Novar heavily relies on arrays of characters and nuances, and most of them were configured for general use and hence lack accuracy in some aspects. By tweaking them to fit your needs, the functions would perform much better.

### Tweaking groups for text similarity
Two functions that process text with variations, `average_stuck_keyboard_enjoyer` and `text_variation`, use **corresponding** and **corresponding2** respectively. 
```python
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
```
As seen above, both work differently. For the case of ``corresponding``, elements its tuples are in the same group, and is recognised as the same character by it. Which means, *Astat1ne* and *Astatine* are the same as *1* and *i* are in the same group, and so on. In some cases, this wouldn't work very well, as *l* is also in the same group as *i*, and could lead to possible false positives.

For `corresponding2`, the value for a certain key contains a list of all the characters that could stand in for it, including the key itself.

### Tweaking hardsounds, softsounds, ignored, and nuances for pronunciation similarity
`pronunciation_similarity` function uses four arrays to determine how similar two strings sound when pronounced. This is because it first gets rid of *softsounds*, *nuances*, and *ignored* by default.
```python
hardsounds = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v' ,'x', 'z', 'r'] # these won't be ignored
softsounds = ['a', 'e', 'i', 'o', 'u', 'y', 'w'] # these 'soft' sounds are ignored
ignored = ['w', 'h', 'r',] #if this is not placed at the start or the end, it will be deleted

# These are nuances in pronunciations. Any second elements will be converted to their first elements. e.g. tia->sha, ph->f
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
```
A string is processed using these. It is best to configure *softsounds*, *hardsounds* and *nuances* according to the words you are trying to pick up, to put more emphasis on certain characters.
