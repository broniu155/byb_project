# Importing libraries
import numpy as np
import pandas as pd

# Importing visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Importing scikit-learn
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score
from sklearn.utils import shuffle

# Load the dataset
data = pd.read_csv("Iris.csv")

# Fit the LabelEncoder
le = LabelEncoder()
data['Species_label'] = le.fit_transform(data['Species'])

# Create the binary classification
data['Species_label'] = data['Species_label'].apply(lambda x: 0 if x == 0 else 1)

# Shuffle the dataset
data = shuffle(data, random_state=42)

# Splitting the dataset into features and target
# Independent variable
X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
# Dependent variable
y = data['Species_label']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predicting the test set results
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Generate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Calculate precision and recall
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_rep)

print('Confusion Matrix:')
print(conf_matrix)

print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')

# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Non-Iris setosa', 'Iris-setosa'], yticklabels=['Non-Iris setosa', 'Iris-setosa'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
