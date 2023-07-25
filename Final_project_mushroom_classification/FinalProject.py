# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

# Read the data
data = pd.read_csv("mushrooms.csv")

# Visualize the data
print(data.head())

# Find the number of samples per class
class_counts = data['class'].value_counts()
print(class_counts)

# Create features and labels
X = data.loc[:, ['cap-shape', 'cap-color', 'ring-number', 'ring-type']]
y = data['class']

# Convert string values to integers using Label Encoding
encoder = LabelEncoder()
for col in X.columns:
    X[col] = encoder.fit_transform(X[col])
y = encoder.fit_transform(y)

# Print the final X and y
print(X.head())
print(y)

# Split the data into train and test sets with 70-30 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating and training models
logistic_model = LogisticRegression()
ridge_model = RidgeClassifier()
decision_tree_model = DecisionTreeClassifier()
naive_bayes_model = GaussianNB()
neural_network_model = MLPClassifier()

# Train the models
logistic_model.fit(X_train, y_train)
ridge_model.fit(X_train, y_train)
decision_tree_model.fit(X_train, y_train)
naive_bayes_model.fit(X_train, y_train)
neural_network_model.fit(X_train, y_train)

# Make predictions using the test dataset
logistic_predictions = logistic_model.predict(X_test)
ridge_predictions = ridge_model.predict(X_test)
decision_tree_predictions = decision_tree_model.predict(X_test)
naive_bayes_predictions = naive_bayes_model.predict(X_test)
neural_network_predictions = neural_network_model.predict(X_test)

# Comparing the performances
print("Classification Report for Logistic Regression model:")
print(classification_report(y_test, logistic_predictions))

print("Classification Report for Ridge Regression model:")
print(classification_report(y_test, ridge_predictions))

print("Classification Report for Decision Tree model:")
print(classification_report(y_test, decision_tree_predictions))

print("Classification Report for Naive Bayes model:")
print(classification_report(y_test, naive_bayes_predictions))

print("Classification Report for Neural Network model:")
print(classification_report(y_test, neural_network_predictions))

# Evaluation with Random Forest
random_forest_model = RandomForestClassifier()
random_forest_model.fit(X_train, y_train)
random_forest_predictions = random_forest_model.predict(X_test)

print("Classification Report for Random Forest model:")
print(classification_report(y_test, random_forest_predictions))


import seaborn as sns
from sklearn.metrics import confusion_matrix

# Helper function to plot confusion matrix as a heatmap
def plot_confusion_matrix(y_true, y_pred, labels, title):
    cm = confusion_matrix(y_true, y_pred)
    ax = plt.subplot()
    sns.heatmap(cm, annot=True, ax=ax, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    ax.set_title(title)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    plt.show()

# Plot confusion matrix for Logistic Regression model
plot_confusion_matrix(y_test, logistic_predictions, labels=["edible", "poisonous"], title="Logistic Regression Confusion Matrix")

# Plot confusion matrix for Ridge Regression model
plot_confusion_matrix(y_test, ridge_predictions, labels=["edible", "poisonous"], title="Ridge Regression Confusion Matrix")

# Plot confusion matrix for Decision Tree model
plot_confusion_matrix(y_test, decision_tree_predictions, labels=["edible", "poisonous"], title="Decision Tree Confusion Matrix")

# Plot confusion matrix for Naive Bayes model
plot_confusion_matrix(y_test, naive_bayes_predictions, labels=["edible", "poisonous"], title="Naive Bayes Confusion Matrix")

# Plot confusion matrix for Neural Network model
plot_confusion_matrix(y_test, neural_network_predictions, labels=["edible", "poisonous"], title="Neural Network Confusion Matrix")

# Plot confusion matrix for Random Forest model
plot_confusion_matrix(y_test, random_forest_predictions, labels=["edible", "poisonous"], title="Random Forest Confusion Matrix")
