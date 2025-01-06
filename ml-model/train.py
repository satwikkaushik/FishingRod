import pandas, joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# loading dataset
df = pandas.read_csv("./datasets/emails.csv")
print(df.head(5))

# vectorization
vectorizer = CountVectorizer(stop_words="english")

X = vectorizer.fit_transform(df["text"])
Y = df["spam"]  # 0-not spam, 1-spam

# splitting
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# training the model
model = LogisticRegression()
model.fit(X_train, Y_train)

print("Model trained")

# testing & evaluating
Y_predict = model.predict(X_test)

print("Accuracy:", accuracy_score(Y_test, Y_predict))
print("Classification Report:\n", classification_report(Y_test, Y_predict))
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_predict))

# saving model and vectorizer
joblib.dump(model, "LR_Spam_Detector.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model & Vectorizer saved")