import numpy as np
from base import extract_features, count_english_words
from joblib import load
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def predict_crack_time(password):
    model = load(f"predict_password/model_data/model{len(password)}.joblib")
    lowercase_count, uppercase_count, digits_count, special_count, security_score = extract_features(password)
    words_count = count_english_words(password)
    features = np.array([[lowercase_count, uppercase_count, digits_count, special_count, words_count]])
    predicted_crack_time = model.predict(features)
    
    time = predicted_crack_time[0]

    return str(time) + " giây"

def predict_crack_time_all(password):
    model = load(f"predict_password/model_data/model_all.joblib")
    lowercase_count, uppercase_count, digits_count, special_count, security_score = extract_features(password)
    words_count = count_english_words(password)
    features = np.array([[len(password), lowercase_count, uppercase_count, digits_count, special_count, words_count]])
    predicted_crack_time = model.predict(features)
    
    time = predicted_crack_time[0]

    return str(time) + " giây"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        password = sys.argv[1]
        type = sys.argv[2]
        if (type == "normal"):
            print(predict_crack_time(password))
        if (type == "all"):
            print(predict_crack_time_all(password))
    else:
        print("No password provided")
