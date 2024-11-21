import numpy as np
from base import extract_features
from joblib import load
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def predict_crack_time(password):
    model = load(f"predict_password/model_data/model{len(password)}.joblib")
    features = np.array([extract_features(password)])
    predicted_crack_time = model.predict(features)
    
    time = predicted_crack_time[0]

    if time < 60:
        return str(time) + " giây"

    time = int(time / 60)

    if time < 60:
        return str(time) + " phút"
    
    time = int(time / 60)

    if time < 24:
        return str(time) + " giờ"
    
    time = int(time / 24)

    if time < 365:
        return str(time) + " ngày"
    
    time = int(time / 365)

    suffix = " năm"

    while time >= 1e9:
        time = int(time / 1e9)
        suffix = " tỷ" + suffix

    if time >= 1e6:
        time = int(time / 1e6)
        suffix = " triệu" + suffix

    if time >= 1e3:
        time = int(time / 1e3)
        suffix = " nghìn" + suffix

    return str(time) + suffix

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(predict_crack_time(password))
    else:
        print("No password provided")
