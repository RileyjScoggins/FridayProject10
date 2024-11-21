import sqlite3
import pandas as pd

# Path to your SQLite database
db_path = '/Users/rileyscoggins/Desktop/FridayProject10/feedback.db'

# Load data into a DataFrame
connection = sqlite3.connect(db_path)
feedback_df = pd.read_sql_query("SELECT * FROM feedback;", connection)
connection.close()

# Display the first few rows
print(feedback_df.head())


import openai
import os
from dotenv import load_dotenv
import pandas as pd

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function for sentiment analysis
def analyze_sentiment(review):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": f"Analyze the sentiment of this review: {review}. Categorize as Positive, Negative, or Neutral."}]
        )
        sentiment = response['choices'][0]['message']['content'].strip()
        return sentiment
    except Exception as e:
        return str(e)

# Apply the function to the DataFrame
feedback_df['sentiment'] = feedback_df['comment'].apply(analyze_sentiment)

# Save the results to an Excel file
output_file = "feedback_with_sentiment.xlsx"
feedback_df.to_excel(output_file, index=False)
print(f"Sentiment analysis completed! Results saved to {output_file}")

