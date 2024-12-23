import random
import json
from zxcvbn import zxcvbn
from base import max_characters
import csv
from base import extract_features, count_english_words

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "~!@#$%^&*()_-=+\\/|?.<>,;:"
all_characters = lowercase + uppercase + digits + special_characters

data = []
num_len = []

def generate_password(length):
    return ''.join(random.choice(all_characters) for _ in range(length))

def add_password_data(filename, start_line, line_cap):
    with open("./data/data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        with open(filename, 'r', encoding='latin-1') as file:
            lines = file.readlines()[start_line:]
            line_cnt = 0
            for line in lines:
                password = line.strip()

                if(len(password) > max_characters or len(password) == 0):
                    continue

                lowercase_count, uppercase_count, digits_count, special_count = extract_features(password)

                if (lowercase_count + uppercase_count + digits_count + special_count) != len(password):
                    continue

                words_count = count_english_words(password)

                analysis = zxcvbn(password)
                crack_time = analysis['crack_times_seconds']['offline_fast_hashing_1e10_per_second']

                new_row = [password, len(password), lowercase_count, uppercase_count, digits_count, special_count, words_count, crack_time]

                writer.writerow(new_row)

                line_cnt += 1
                if line_cnt >= line_cap:
                    break
    
if __name__ == "__main__":
    # 1 -> 174983
    # 7000001 -> 7038495
    # 
    add_password_data("./data/rockyou.txt", 7000000, 100000)

    for i in range(0, max_characters+1):
        num_len.append(0)
    # with open("data/data.csv", "r") as file:
    #     reader = csv.reader(file)
    #     for index, row in enumerate(reader):
    #         if(index > 0):
    #             num_len[int(row[1])]+=1
    # with open("./data/rockyou.txt", "r", encoding='latin-1') as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         password = line.strip()
    #         if(len(password) > max_characters or len(password) == 0):
    #             continue
    #         num_len[len(password)] += 1
    print(num_len)

    # add_password_data("./data/random.txt", 0, 1000)