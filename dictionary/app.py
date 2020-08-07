import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        condition = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if condition == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif condition == "N":
            return "The word doesn't exist. Double check it."
        else:
            return "Don't understand your entry."
    else:
        return "The word doesn't exist."

word = input ("Enter words: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
