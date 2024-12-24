import json
import random
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Sample intents data
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Prepare the dataset
# data = []
# for intent in intents:
#     for pattern in intent['patterns']:
#         data.append((pattern, intent['tag']))
data = []
for intent in intents:
    if 'patterns' in intent:  # Check if 'patterns' key exists
        for pattern in intent['patterns']:
            data.append((pattern, intent['tag']))
# Create a DataFrame
df = pd.DataFrame(data, columns=['Text', 'Intent'])

# Preprocess the text data
df['Processed_Text'] = df['Text'].str.lower()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Processed_Text'], df['Intent'], test_size=0.2, random_state=42)

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_tfidf = vectorizer.transform(X_test)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Print the classification report and confusion matrix
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Function to classify user input
def classify_intent(user_input):
    # Preprocess the user input
    user_input_tfidf = vectorizer.transform([user_input.lower()])
    
    # Predict the intent
    intent = model.predict(user_input_tfidf)
    return intent[0]

# Function to get a response based on the predicted intent
def get_response(intent_tag):
    for intent in intents:
        if intent['tag'] == intent_tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I don't understand."

# Streamlit app
st.title("NLP Chatbot")
st.write("Chat with the bot by typing your message below:")

user_message = st.text_input("You: ")

if st.button("Send"):
    if user_message.lower() in ["bye", "exit", "quit"]:
        st.write("Chatbot: Goodbye! Have a great day!")
    else:
        predicted_intent = classify_intent(user_message)
        response = get_response(predicted_intent)
        st.write(f"Chatbot: {response}")



        
#  pip install streamlit pandas scikit-learn numpy nltk spac
# y