import random
import json
from zxcvbn import zxcvbn
from base import extract_features, max_characters

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_characters = "~!@#$%^&*()_-=+\\/|?.<>,;:"
all_characters = lowercase + uppercase + digits + special_characters

def generate_password(length):
    return ''.join(random.choice(all_characters) for _ in range(length))

def generate_password_data(num_samples):
    data = []
    for length in range(1, max_characters + 1):
        for i in range(num_samples * length):
            password = generate_password(length)
            
            analysis = zxcvbn(password)
            crack_time = analysis['crack_times_seconds']['offline_fast_hashing_1e10_per_second']

            *_, security_score = extract_features(password)

            crack_time = float(crack_time) * security_score

            data.append({
                "password": password,
                "crack_time": crack_time
            })
    return data

def save_data_to_json(filename, num_samples):
    data = generate_password_data(num_samples)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Dữ liệu đã được lưu vào {filename}")
    
if __name__ == "__main__":
    save_data_to_json("data.json", 1000)
