from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# --------------------------------------------------
# 1. Create a small labeled text dataset
# --------------------------------------------------
texts = [
    "My package arrived three days late",
    "Where is my shipment",
    "The tracking number is not updating",
    "My order has not been delivered",
    "The courier delivered to the wrong address",
    "When will my package arrive",

    "I want to return this product",
    "Please give me my money back",
    "How can I request a refund",
    "I received the wrong item and want a refund",
    "Please cancel the order and refund me",
    "What is your return policy",

    "I was charged twice",
    "My payment did not go through",
    "The amount on my invoice is incorrect",
    "Why was my card declined",
    "There is an unexpected charge on my account",
    "I need a copy of my bill",
]

labels = [
    "delivery",
    "delivery",
    "delivery",
    "delivery",
    "delivery",
    "delivery",

    "refund",
    "refund",
    "refund",
    "refund",
    "refund",
    "refund",

    "billing",
    "billing",
    "billing",
    "billing",
    "billing",
    "billing",
]


# 2. Split data before fitting TF-IDF
X_train,X_test,y_train,y_test = train_test_split(texts,labels,test_size=0.33,random_state=42,stratify=labels)


# 3. Build text-classifier pipeline
model = Pipeline([
    ("tfidf",TfidfVectorizer(lowercase=True,ngram_range=(1,2))),
    ("classifier", LogisticRegression(max_iter=1000))
])

#4. Train the vectorizer and classifier
model.fit(X_train,y_train)

# --------------------------------------------------
# 5. Evaluate predictions on unseen test text
# --------------------------------------------------
predictions = model.predict(X_test)
print(f"\n Accuracy: {accuracy_score(y_true=y_test,y_pred=predictions)}")
print(f"\n Classification Report: {classification_report(y_true=y_test,y_pred=predictions,zero_division=0)}")
print(f"\n Confusion matrix: {confusion_matrix(y_true=y_test,y_pred=predictions,labels=["delivery","refund","billing"])}")

'''. --- OUTPUT --
 Accuracy: 0.6666666666666666

 Classification Report:  precision    recall  f1-score   support

     billing             1.00      1.00      1.00         2
    delivery             0.50      0.50      0.50         2
      refund             0.50      0.50      0.50         2

    accuracy                                 0.67         6
   macro avg             0.67      0.67      0.67         6
weighted avg             0.67      0.67      0.67         6


 Confusion matrix: [[1 1 0]
 [1 1 0]
 [0 0 2]]
'''


# --------------------------------------------------
# 6. Classify new support tickets
# --------------------------------------------------
new_tickets = [
    "The tracking page says my shipment is delayed",
    "Please return my payment",
    "My credit card was charged two times",
]

new_predictions = model.predict(new_tickets)
print("\nNew ticket predictions:")

for ticket, prediction in zip(new_tickets, new_predictions):
    print(f"{ticket} → {prediction}")

''' -- OUTPUT --

    New ticket predictions:
    The tracking page says my shipment is delayed → delivery
    Please return my payment → billing
    My credit card was charged two times → billing

'''

# --------------------------------------------------
# 7. Inspect individual test results
# --------------------------------------------------

print("\nIndividual test results:")

for text, actual, predicted in zip(X_test, y_test, predictions):
    status = "CORRECT" if actual == predicted else "ERROR"

    print(f"\n[{status}]")
    print(f"Text:      {text}")
    print(f"Actual:    {actual}")
    print(f"Predicted: {predicted}")

''' -- OUTPUT --

    Individual test results:

    [CORRECT]
    Text:      When will my package arrive
    Actual:    delivery
    Predicted: delivery

    [CORRECT]
    Text:      How can I request a refund
    Actual:    refund
    Predicted: refund

    [CORRECT]
    Text:      There is an unexpected charge on my account
    Actual:    billing
    Predicted: billing

    [ERROR]
    Text:      What is your return policy
    Actual:    refund
    Predicted: delivery

    [CORRECT]
    Text:      Why was my card declined
    Actual:    billing
    Predicted: billing

    [ERROR]
    Text:      The courier delivered to the wrong address
    Actual:    delivery
    Predicted: refund

'''