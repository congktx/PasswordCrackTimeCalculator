import csv
from base import max_characters
from joblib import dump
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV

X_train = [[] for _ in range(max_characters + 1)]
y_train = [[] for _ in range(max_characters + 1)]
XX = []
yy = []

def get_data(filename):
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

            data_row = []
            for i in range(1,7):
                data_row.append(int(row[i]))
            XX.append(data_row)

            yy.append(float(row[7]))

    print(XX[0])
    print(yy[0])

def train_models(filename):
    params = {
            "Decision Tree": {
                "criterion": [
                    "squared_error",
                    "friedman_mse",
                    "absolute_error",
                    "poisson",
                ],
                "splitter": ["best", "random"],
                "max_features": ["sqrt", "log2"],
            },
        }
    
    # model = DecisionTreeRegressor()
    # para = params["Decision Tree"]

    # gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=1)
    # gs.fit(XX, yy)

    # model.set_params(**gs.best_params_)
    # model.fit(XX, yy)

    # dump(model, f"./model_data/model_all.joblib")
    # print(f"Mô hình đã được lưu vào file model_data/model_all.joblib")
    
    # for i in range(1, max_characters + 1):
    #     print(f"Training model {i}...")

    #     model = DecisionTreeRegressor()
    #     para = params["Decision Tree"]

    #     gs = GridSearchCV(model, para, cv=3, n_jobs=-1, verbose=1)
    #     gs.fit(X_train[i], y_train[i])

    #     model.set_params(**gs.best_params_)
    #     model.fit(X_train[i], y_train[i])

    #     dump(model, f"./model_data/model{i}.joblib")
    #     print(f"Mô hình thứ {i} đã được lưu vào file model_data/model{i}.joblib")

if __name__ == "__main__":
    train_models("./data/data.csv")
