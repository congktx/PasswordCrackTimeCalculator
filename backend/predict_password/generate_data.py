import random
import json
from zxcvbn import zxcvbn
from base import max_characters
import csv
from math import sqrt
from base import extract_features, count_english_words

lowercases = "abcdefghijklmnopqrstuvwxyz"
uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "~!@#$%^&*()_-=+\/|?.<>,;:"
all_characters = lowercases + uppercases + digits + special_characters

data = []
num_len = []
eng_words = ["ace","big","cat","dog","elf","fun","hut","jaw","key","mix","owl","pig","rat","van","zip"]
array_5d = [[[[[0 
                for _ in range(max_characters + 1)] 
                for _ in range(max_characters + 1)] 
                for _ in range(max_characters + 1)] 
                for _ in range(max_characters + 1)]
                for _ in range(max_characters + 1)]

def generate_password(lower, upper, digit, special, words):
    password = ""
    for i in range(words):
        password += random.choice(eng_words)
        lower -= 3
    numbers = [lower, upper, digit, special]
    for i in range(lower + upper + digit + special):
        type = random.randint(0, 3)
        while numbers[type] == 0:
            type = random.randint(0, 3)
        numbers[type] -= 1
        if type == 0:
            password += random.choice(lowercases)
        elif type == 1:
            password += random.choice(uppercases)
        elif type == 2:
            password += random.choice(digits)
        elif type == 3:
            password += random.choice(special_characters)
    return password

def add_password_data(start_line, line_cap):
    count_tt()
    with open("./data/data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        with open("./data/rockyou.txt", 'r', encoding='latin-1') as file:
            lines = file.readlines()[start_line:]
            line_cnt = start_line - 1
            for line in lines:
                line_cnt += 1
                if line_cnt >= line_cap:
                    break 

                password = line.strip()
                leng = len(password)

                if (leng > max_characters or leng == 0):
                    continue

                lowercase_count, uppercase_count, digits_count, special_count, security_score = extract_features(password)

                if (lowercase_count + uppercase_count + digits_count + special_count) != leng:
                    continue

                words_count = count_english_words(password)

                if (array_5d[lowercase_count][uppercase_count][digits_count][special_count][words_count] > 0):
                    continue
                array_5d[lowercase_count][uppercase_count][digits_count][special_count][words_count] = 1

                analysis = zxcvbn(password)
                crack_time = float(analysis['crack_times_seconds']['offline_fast_hashing_1e10_per_second'])
                crack_time = crack_time * security_score * (0.99 ** words_count)

                new_row = [password, leng, lowercase_count, uppercase_count, digits_count, special_count, words_count, crack_time]

                writer.writerow(new_row)

def add_lack_sample_data(filename):
    count_tt()
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        for i in range(30, -1, -1):
            for j in range(30-i, -1, -1):
                for k in range(30-i-j, -1, -1):
                    for l in range(30-i-j-k, -1, -1):
                        for h in range(i//3, -1, -1):
                            if (i+j+k+l == 0 or array_5d[i][j][k][l][h] > 0):
                                continue
                            password = generate_password(i,j,k,l,h)
                            analysis = zxcvbn(password)
                            crack_time = float(analysis['crack_times_seconds']['offline_fast_hashing_1e10_per_second'])
                            *_, security_score = extract_features(password)
                            crack_time = crack_time * security_score * (0.99 ** h)
                            new_row = [password, i+j+k+l, i, j, k, l, h, crack_time]
                            writer.writerow(new_row)

def count_tt():
    with open("./data/data.csv", "r") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if (index == 0):
                continue
            try:
                array_5d[int(row[2])][int(row[3])][int(row[4])][int(row[5])][int(row[6])] = 1
            except:
                print("error", row)

if __name__ == "__main__":
    # add_password_data(0, 15000000)
    # add_lack_sample_data("./data/data.csv")

    for i in range(0, max_characters+1):
        num_len.append(0)
    with open("data/data.csv", "r") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if(index > 0):
                num_len[int(row[1])]+=1
    print(num_len)

    # for i in range(0, max_characters+1):
    #     num_len[i] = 0
    # with open("./data/rockyou.txt", "r", encoding='latin-1') as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         password = line.strip()
    #         if(len(password) > max_characters or len(password) == 0):
    #             continue
    #         num_len[len(password)] += 1
    # print(num_len)