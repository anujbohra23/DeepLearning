from dotenv import load_dotenv
import streamlit as st
import sqlite3
import google.generativeai as genai
import os

# Load environment variables from .env file
load_dotenv()

# Configure the Google Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Loading gemini model and providing query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"{prompt} {question}")
    return response.text


# Function to execute SQL query
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows


# Prompt string to provide context to the model
prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.
    
    Example 1: "How many entries of records are present?"
    SQL command: SELECT COUNT(*) FROM STUDENT;
    
    Example 2: "Tell me all the students studying in Data Science class?"
    SQL command: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    
    Note: Ensure the SQL code does not have ``` at the beginning or end and does not contain the word 'SQL'.
"""

# Streamlit App setup
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input your question:", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    # Generate SQL query from English question
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query:")
    st.write(sql_query)

    # Execute the SQL query
    try:
        response = read_sql_query(sql_query, "student.db")
        st.subheader("Query Results:")
        for row in response:
            st.write(row)
    except Exception as e:
        st.write("Error executing SQL query:", e)
