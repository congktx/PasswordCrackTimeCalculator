import nltk
from nltk.corpus import words
nltk.download("words")

max_characters = 30

def extract_features(password):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "~!@#$%^&*()_-=+\/|?.<>,;:"

    lowercase_count = sum(1 for c in password if c in lowercase)
    uppercase_count = sum(1 for c in password if c in uppercase)
    digits_count = sum(1 for c in password if c in digits)
    special_count = sum(1 for c in password if c in special_characters)

    return [lowercase_count, uppercase_count, digits_count, special_count]


def count_english_words(input):
    english_words = set(words.words())

    words_count = []
    words_count.append(0)

    for i in range(1, len(input)):
        words_count.append(words_count[i - 1])
        for j in range(1,i):
            if input[j:(i+1)] in english_words:
                words_count[i] = max(words_count[i], words_count[j - 1] + 1)

    return words_count[len(input) - 1]

if __name__ == "__main__":
    print(count_english_words("bullshit"))