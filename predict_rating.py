from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import random
import stopwords

dataset = load_dataset("tblard/allocine", split="train")

def label_to_rating(label):
    return random.choice([1, 2]) if label == 0 else random.choice([4, 5])

texts = dataset["review"]
ratings = [label_to_rating(l) for l in dataset["label"]]

X_train, _, y_train, _ = train_test_split(texts, ratings, test_size=0.9, random_state=42)  # Réduire la taille de l'entraînement

stop_words_fr = stopwords.get_stopwords("fr")

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000, stop_words=stop_words_fr)),
    ("reg", LinearRegression()),  # Utilisation d'un modèle plus rapide
])

pipeline.fit(X_train, y_train)

joblib.dump(pipeline, "predict_rating.joblib")

print("Modèle entraîné et sauvegardé.")
