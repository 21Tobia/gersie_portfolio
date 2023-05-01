# gersie_portfolio
CS-4395 (NLP)

portfolio_0 
https://github.com/21Tobia/gersie_portfolio/blob/main/NLP-%20Portfolio%20setup%20assignment.pdf

portfolio_1
https://github.com/21Tobia/gersie_portfolio/tree/main/portfolio1_ggt210000

Portfolio_2
https://github.com/21Tobia/gersie_portfolio/tree/main/NLP%20HW-2 

porfolio_3
https://github.com/21Tobia/gersie_portfolio/blob/main/HomeWork3_worldNet.ipynb%20-%20Colaboratory.pdf

Porfolio_4
https://github.com/21Tobia/gersie_portfolio/tree/main/NLP_HW3

Porfolio_5
https://github.com/21Tobia/gersie_portfolio/blob/main/Parsing%20Sentenses.pdf

Portfolio_6
https://github.com/21Tobia/gersie_portfolio/tree/main/NLP%20HW6

porfolio _7
https://github.com/21Tobia/gersie_portfolio

Porfolio _8
https://github.com/21Tobia/gersie_portfolio

Porfolio _9
https://github.com/21Tobia/gersie_portfolio


Human Language Technology Portfolio (CS 4395) Summary

This is Gebresilassie Takele’s portfolio for class CS 4395.001 (Human Language Technologies). This portfolio is for the Spring2023 semester at the University of Texas at Dallas, the course taken from Professor Karen Mazidi.
Assignment0: Portfolio setup
The goal of this task was to make a GitHub portfolio for this class. Additionally, we were required to write a paragraph about our own personal interests in NLP and a summary of the historical and contemporary approaches to NLP. This was assignment0 which we call it Portfolio setup.
Assignment 1: Text processing
The target of this assignment was to settle in programming in Python, utilizing framework contentions, making classes, coding standard articulations, and performing document I/O and pickling. This program takes an argument in the form of a.csv file with the name "data.csv," reformats the text in that file, and then displays the reformatted text on the screen. The text is held in by a Person class, and the.display() function displays the reformatted text. At long last, there is some pickling involved — basically we simply compose the reformatted text into a .py record and read it in to show the data.
You ought to have the option to ordinarily run the code; Nonetheless, I used PyCharm to work on and run it. The .py record ought to as of now have the data.csv document as a framework contention.
Regarding Python's strengths and weaknesses in text processing, I believe that the language's ease of writing is a strength. Preceding Python, I generally had insight with C++ and Java, and similarly talking, composing code in Python than the other two languages is a lot more straightforward. It feels more natural and doesn't have a lot of unnecessary syntax. Another advantage is the abundance of useful text processing methods, such as.upper(),.lower(), and.capitalize(), which make the job much simpler. However, one flaw I've noticed is that the program sometimes loads slowly, especially when you run it for the first time.
After I completed this assignment, I got comfortable in the Python coding environment of my choice. I got experience in coding a Python program that uses sysarg and gain experience in writing a simple class in Python.  I can do code regular expressions for text processing and able to do code file I/O and pickling.
Assignment 2: Word Guessing Game
This assignment required Python's NLTK libraries to explore a text file and develop a word-guessing game for users to play. We had to read from a text file called "anat19.txt," tokenize the text, and figure out the lexical diversity for this assignment. Additionally, we were required to perform some preprocessing on the text, which included limiting the tokens to alpha characters with a length greater than 5 that were not on the NLTK stopword list. The tokens were then lemmatized, a list of unique lemmas was compiled, part of speech tags were applied, and a list of lemmas that were only nouns was compiled.
We used that list of nouns as our word bank for the guessing game after all the preprocessing. Users would have to guess a word from the list that the program selected at random.
There was the basic guessing game: For each letter in the word that the user had to guess, there would be a line. Guessing all of the word's letters was the goal. The game would continue to provide players with new words to guess for an infinite amount of time if the user achieved that. Additionally, a scoring system was implemented. The user's score would increase if they correctly guessed a letter. Their score would decrease if they missed a letter. If the player entered "!", the game would end. character or if their score was less than zero or negative.
Assignment 3: WordNet
The objective of this task was to get familiar with a few fundamental abilities involving WordNet and SentiWordNet in Python for normal language handling. The assignment basically consists of a series of steps that demonstrate how to use both softwares.
Some of these steps for our exploration with WordNet are as follows: generating a noun's synsets; utilizing the noun-specific.definition(),.examples(), and.lemmas() functions; generating the hypernyms, hyponyms, meronyms, and other terms. from those nouns; etc. We also needed to run the Wu-Palmer similarity metric, the Lesk algorithm, and the WordNet noun hierarchy.
We used SentiWordNet to discover the sentiments of an "emotionally charged word," compute its polarity and sentiment scores, and then construct a sentence and compute sentiment scores for each word in that sentence.
In the last piece of this task we investigate collocations a piece too. We were required to calculate the point-wise mutual information, or PMI, score for one of the collocations in a particular text that is text4, the Inaugural corpus.
Assignment 4: N Gram Language Model
The aim of this assignment was to obtain proficiency in creating n-grams from text and building language models from those n-grams. Furthermore, we were required to contemplate the usefulness of such language models. To achieve this goal, we constructed unigram and bigram dictionaries for English, French, and Italian using some supplied training data. In these dictionaries, the key represents the unigram or bigram text, while the value denotes the count of that particular unigram or bigram in the data. Following the creation of these dictionaries, we used additional test data (also provided) to compute probabilities. The test data consisted of a list of sentences in a file, separated by a newline, and each sentence was either in English, French, or Italian. Our task was to determine the probabilities that the given sentence was in each language. After calculating the probabilities for each sentence in all three languages, we wrote the language with the highest probability into a file. Finally, we compared our output in that file to a solution file and generated an accuracy score.
Assignment 5: Web Crawler
The purpose of this assignment was to grasp the significance of corpora in NLP tasks, understand the structure of HTML, and gain insight into how websites operate. To accomplish this goal, we were instructed to create a web crawler and conduct web scraping using various APIs, including BeautifulSoup. Initially, we constructed a web crawler function, which necessitated supplying a starting URL to collect at least 15 relevant URLs - in other words, URLs that were related to the topic we selected based on the starting URL. After obtaining these URLs, we extracted the text from each webpage and saved it in 15 individual files. Later, we cleaned the text by removing newlines, tabs, and reformatting it before saving it to 15 new files, bringing the total to at least 30 files. Next, we extracted the top 40 terms from all 15 pages and displayed them on the screen. From these 40 terms, we manually selected the best 10 terms and utilized them to create a knowledge base. The knowledge base was a Python dictionary in which the (key: value) pairs represented (terms: sentences from the 15 pages containing that term).
Assignment 6: Sentence Parsing
The objective of this assignment was to comprehend concepts linked to sentence syntax, learn about the three different kinds of sentence parsing (PSG, dependency, and SRL), and be capable of using syntax parsers. Initially, I created a relatively complicated sample sentence with at least 12 tokens and hand-drew a PSG tree for that sentence. I labeled the parts of speech and briefly defined the phrase terms that appeared in the sentence, such as S, SBAR, NP, VP, and so on. After that, I drew a dependency parse of the sentence by hand and labeled the dependency relationships. I also defined the dependency relations present, such as amod, cc, conj, etc. For the SRL parse, I listed the predicate for each frame of the sentence, its arguments, and its modifiers (if any were present). I then discussed the arguments and their relationship with the predicate/verb for each frame and defined any modifiers that were available.
Assignment 7: Text Classification
Text classification is a natural language processing technique that involves assigning predefined categories or labels to a given piece of text. It involves the use of machine learning algorithms to automatically classify texts into various categories based on the patterns and features present in the text. Text classification has various applications such as spam filtering, sentiment analysis, topic modeling, and language identification, among others. The performance of text classification models can be improved by using appropriate feature selection techniques, pre-processing methods, and evaluation metrics.
Assignment 8: ACL Paper Summary
The goal of this assignment was to pick one article from the 2022 ACL conference's Long Papers Proceedings and write a report on it.

For this task, we had to create a minimum of a two-page document that included the authors' names and affiliations, the issues they sought to address, their earlier work, the article's original contributions, the writers' appraisal and analysis of their own work, and finally, the total number of citations per author.

