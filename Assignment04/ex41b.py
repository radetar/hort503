import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
        "class %%%(%%%):":
            "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
            "class %%% has-a __init__ that takes self and *** params.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has-a function *** that takes self and @@@ params.",
        "*** = %%%()":
            "Set *** to an instance of class %%%.",
        "***.***(@@@)":
            "From *** get the *** function, call it with params self, @@@.",
        "***.*** = '***'":
            "From *** get the *** attribute and set it to '***'."
}

# do they want to drill ohrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

#gets a random snippet and a random phrase.

# a snippet is a key from the dictionary, phrase is its value
def convert(snippet, phrase):
    #Randomly makes set of words that are capitalized for class name, and lower case for other names from the list
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
#try block, keeps going untill exception
try:
    #This prevents from going forever, try block will go false when cntrl-D
    while True:
        #takes the Dictionary 'PHRASES' and gets all the kets for the different words
        #snippets becomes a list of these keys
        snippets = list(PHRASES.keys())
        print("These will be the snippet order this time", snippets)
        #Shuffles the keys
        random.shuffle(snippets)
        #
        #For each key in list 'snippets'python calls this
        for snippet in snippets:
            #Calls up one of the phrases from the dictionary using a key from snippet (the first, which is always random)
            phrase = PHRASES[snippet]
            print("This is a cool   phrase!!!", phrase)
            #Calls 'convert' function to assign question and answer
            question, answer = convert(snippet, phrase)
            #if phrase_first is true, then we flip
            #This prints the question
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
# an EOFError is 'End of File Error'. 'Except' is part of the try block
except EOFError:
    print("\nBye")
