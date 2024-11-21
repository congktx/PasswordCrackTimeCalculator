from sklearn.linear_model import LinearRegression
import json
import numpy as np
from base import extract_features, max_characters
from joblib import dump

def load_and_process_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    features = []
    labels = []
    for entry in data:
        if "password" not in entry or "crack_time" not in entry:
            raise ValueError("Dữ liệu đầu vào thiếu trường 'password' hoặc 'crack_time'.")
        
        features.append(extract_features(entry["password"]))
        labels.append(entry["crack_time"])

    return np.array(features), np.array(labels)

def train_model(data_file, model_file):
    X, y = load_and_process_data(data_file)

    model = LinearRegression()
    model.fit(X, y)

    dump(model, model_file)
    print(f"Mô hình đã được lưu vào file {model_file}")

def train_models(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    features = [[] for _ in range(max_characters + 1)]
    labels = [[] for _ in range(max_characters + 1)]

    for entry in data:
        if "password" not in entry or "crack_time" not in entry:
            raise ValueError("Dữ liệu đầu vào thiếu trường 'password' hoặc 'crack_time'.")
        password = entry["password"]
        features[len(password)].append(extract_features(password))
        labels[len(password)].append(entry["crack_time"])

    for i in range(max_characters):
        X = np.array(features[i + 1])
        y = np.array(labels[i + 1])
        model = LinearRegression()
        model.fit(X, y)

        dump(model, f"model_data/model{i+1}.joblib")
        print(f"Mô hình thứ {i+1} đã được lưu vào file model_data/model{i+1}.joblib")

if __name__ == "__main__":
    train_models("data.json")
