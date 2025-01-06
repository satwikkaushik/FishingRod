import pandas, joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# loading dataset
df = pandas.read_csv("ml-model/datasets/legitimate_phishing_structured_dataset.csv")
df = df.drop(columns=["URL"], errors="ignore")
# print(df.head(5))

# splitting
X = df.drop(columns=["label"])
Y = df["label"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# training the model
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, Y_train)

# evaluating
Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)
print(f'Accuracy: {accuracy:.2f}')

# saving the model
joblib.dump(model, "./ml-model/LR_model.pkl")