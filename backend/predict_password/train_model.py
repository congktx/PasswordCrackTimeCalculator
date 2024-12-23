import json
import numpy as np
from base import extract_features, max_characters
from joblib import dump
import csv
from sklearn.tree import DecisionTreeRegressor


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

    model = DecisionTreeRegressor()
    model.fit(X, y)

    dump(model, model_file)
    print(f"Mô hình đã được lưu vào file {model_file}")

def train_models(filename):
    X_train = [[] for _ in range(max_characters + 1)]
    y_train = [[] for _ in range(max_characters + 1)]

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):

            if (index == 0):
                continue

            leng = int(row[1])

            data_row = []
            for i in range(2,7):
                data_row.append(int(row[i]))
            X_train[leng].append(data_row)

            y_train[leng].append(float(row[7]))


    for i in range(max_characters):
        model = DecisionTreeRegressor()
        model.fit(X_train[i], y_train[i])

        dump(model, f"./model_data/model{i+1}.joblib")
        print(f"Mô hình thứ {i+1} đã được lưu vào file model_data/model{i+1}.joblib")

if __name__ == "__main__":
    train_models("./data/data.csv")
