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
