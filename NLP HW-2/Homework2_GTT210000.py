import sys # for reading and exiting from file and program
import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import random


# preprocessing the input file
def preprocessing(raw_file):
    # tokenize the lower-case raw text
    tokens = word_tokenize(raw_file.lower())

    # and variable to store the stopwords
    stop_words = set(stopwords.words('english'))

    # reduce the tokens to only those that are alpha, not in
    # the NLTK stopword list, and have length > 5
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words and len(t) > 5]

    # lemmatize the tokens and use set() to make a list of unique lemmas
    Lemmas_unique = sorted(list(set([WordNetLemmatizer().lemmatize(r) for r in tokens])))

    # print the lexical diversity
    print("Lexical diversity: %.2f" % (len(Lemmas_unique) / (len(tokens))))

    # do pos tagging on the unique lemmas and print the first 20 tagged
    lemmasUniqueTags = nltk.pos_tag(Lemmas_unique)

    # print the first 20 Tagged items
    print('\nFirst 20 Tagged Words:', lemmasUniqueTags[:20])
    # create a list of only those lemmas that are nouns
    nounLemmas = list([x[0] for x in lemmasUniqueTags if x[1].startswith("N")])

    # print the output print total number of Tokens and nouns
    print('\nTotal Number of Tokens:', len(tokens))
    print('\nTotal Number of Nouns:', len(nounLemmas))

    # return tokens (not unique tokens) from step a, and nouns from the function
    return tokens, nounLemmas

# Guessing game function
def guess_game(list):
    # initial user score
    first_score = 5

    # Rrandomly choosing a word from the 50 words list
    random_word_picked = random.choice(list)[0]
    found_letter = []
    guess_by_user = []

    print("\nLet's play a word guessing game!")

    for element in random_word_picked:
        print('_', end=" ")

    # When the score is below 0 (negative) the game will end.
    while first_score > -1:
        letter_input = input('\nGuess a letter: ').lower()

        # for invalid input
        if not letter_input.isalpha() and letter_input != "!":
            print("\nPlease type a valid letter.")

        # for already tried attempted
        elif letter_input in guess_by_user:
            print("\nAlready attempted this letter, try again.")

        # When user enters '!' game will ends such like when the score becomes negative
        elif letter_input != "!":
            # All the guesses the user has made into a list
            guess_by_user.append(letter_input)
            if letter_input in random_word_picked:
                first_score += 1
                found_letter.append(letter_input)
                print("\nRight! Score is ", first_score)
            # if letter is not in word subtract 1 from score
            else:
                first_score -= 1
                print("Sorry, guess again. Score is ", first_score)
            count = 0
            for element in random_word_picked:
                if element in found_letter:
                    print(element, end=" ")
                    count += 1
                else:
                    print('_', end=" ")
            # If word is guessed game over.
            if count == len(random_word_picked):
                print("\nYou solver it!")
                retry_game = input("\nPlay again? (Y/N) ")
                if retry_game.lower() == "y":
                    guess_game(list)
                else:
                    print("\nThank you for playing!")
                    sys.exit(0)

        else:
            print("\nThanks for playing!")
            sys.exit(0)

    # Show user score if the lost.. show the word.
    print("\n\nYou lost by score...the word was:", random_word_picked)

    retry_game = input("\nPlay again? (Y/N) ")
    if retry_game.lower() == "y":
        guess_game(list)
    else:
        print("\nThanks for playing!")
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        print('Input file: ', input_file)

        with open('anat19.txt', 'r') as f:
            raw_text = f.read()

        tokens, noun_lemmas = preprocessing(raw_text)
        common_list =[]

        # dictionary of nouns
        counts = {t: tokens.count(t)
        for t in noun_lemmas}

        #  sort most common 50 words.
        words_sorted = sorted(counts.items(), key= lambda x: x[1], reverse = True)  # saving to be used in the game
        print("The 50 most common words in this text:")
        for i in range(50):
            common_list.append(words_sorted[i])
            print(words_sorted[i])

        guess_game(common_list)
    else:
        print('ERROR: File name is missing.')