import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "predict_rating.joblib")
model = joblib.load(MODEL_PATH)

def predict_rating(text):
    return int(model.predict([text])[0])