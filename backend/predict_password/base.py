from nltk.corpus import words
# import nltk
# nltk.download("words")
import math

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

    security_score = (1.01 ** lowercase_count) * (1.02 ** uppercase_count) * (1.03 ** digits_count) * (1.04 ** special_count)

    return [lowercase_count, uppercase_count, digits_count, special_count, security_score]


def count_english_words(input):
    input = input.lower()

    english_words = set(words.words())

    words_count = []
    words_count.append(0)

    for i in range(1, len(input)):
        words_count.append(words_count[i - 1])
        for j in range(1,i):
            if input[j:(i+1)] in english_words:
                words_count[i] = max(words_count[i], words_count[j - 1] + 1)

    return words_count[len(input) - 1]

def calculate_entropy(password):
    length = len(password)
    charset_size = 0
    
    if any(c.islower() for c in password):
        charset_size += 26  
    if any(c.isupper() for c in password):
        charset_size += 26 
    if any(c.isdigit() for c in password):
        charset_size += 10  
    if any(not c.isalnum() for c in password):
        charset_size += 33  
    
    entropy = length * math.log2(charset_size)
    return entropy

if __name__ == "__main__":
    print(count_english_words("acebigcatdogelffunhutjawkeymixowlpigratvanzip"))
    print("base.py")