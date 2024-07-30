import pandas as pd
from transformers import pipeline

# Load your CSV file
df = pd.read_csv("FileForModel.csv")

# Initialize the sentiment-analysis pipeline
sentiment_analysis = pipeline("sentiment-analysis")


# Function to label the title
def label_sentiment(title):
    result = sentiment_analysis(title)[0]
    return "positive" if result["label"] == "POSITIVE" else "negative"


# Apply the function to the 'title' column
df["label"] = df["message"].apply(label_sentiment)

# Save the labeled data to a new CSV file
df.to_csv("labeled_data.csv", index=False)
