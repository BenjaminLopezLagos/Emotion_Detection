# This is a sample Python script.
import nltk
from EmotionLex import EmotionLex, Phrase


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('corpus')
    nltk.download('wordnet')

    emotion_lex = EmotionLex()
    phrase = Phrase("I love rabbits very much 1.")
    emotion_lex.find_emotions(phrase)

    print(phrase.tokens)
    print(phrase.emotions)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
