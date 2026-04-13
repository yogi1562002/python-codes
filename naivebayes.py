import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("data.csv")
le = LabelEncoder()
for column in data.columns:
    data[column] = le.fit_transform(data[column])
X = data.iloc[:, :-1]  
y = data.iloc[:, -1]   
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Predictions:", y_pred)
print("Actual:", y_test.values)
print("Accuracy:", accuracy * 100, "%")
