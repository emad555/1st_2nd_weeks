
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def transelate(vocab):
    vocab = vocab.lower()
    if vocab in data:
        return data[vocab]
    elif len(get_close_matches(vocab,data.keys()))>0:
        instead = input("Did you mean %s instead? Enter Y if yes, or N if no." %get_close_matches(vocab,data.keys())[0])
        if instead == "Y" or instead == "y":
            return data[get_close_matches(vocab,data.keys())[0]]
        elif instead == "N" or instead == "n":
            return "The word does not exist, please double check it!"
        else:
            return "Wrong input!"
    else:    
        return "The word does not exist, please double check it!"

vocab = input("Enter vocabulary:")
last = transelate(vocab)

if type(last) == list:
    x = 0
    for i in last:
        x = x + 1
        print("%s"%x ,i)
else:
    print(last)
