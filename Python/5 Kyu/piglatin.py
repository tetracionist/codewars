# In response to https://www.codewars.com/kata/520b9d2ad5c005041100000f

import string, re

def pig_it(text):
    translated_text = []
    for word in text.split(" "):
        if re.match('^[a-zA-Z0-9]*$',word):
            translated_text.append(f"{word[1:]}{word[0]}ay")
        else:
            translated_text.append(word)
            
    return ' '.join(translated_text)
            
