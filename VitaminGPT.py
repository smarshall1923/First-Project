# Import the required libraries

import os
import requests
import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from notion import get_pages
from openai_api import call_chat_completion
from ui import push_to_expander, display_table
from config import OPENAI_API_KEY, NOTION_TOKEN, DATABASE_ID
from google_sheets import get_google_sheet_data

get_google_sheet_data


# Create a simple Streamlit application
placeholder = st.empty()
placeholder.title("Steve's Vitamin List From Notion")
placeholder.write("Steve Marshall's List of Vitamins From Notion")

push_to_expander("This is a test", "Vitamin A", placeholder)
# Initialize session state for table data
if 'table_data' not in st.session_state:
    st.session_state.table_data = []


# Get the information from the Notion database
pages = get_pages()
columns = st.columns(3)  # Create three columns

for i, page in enumerate(pages):
    # Look through the dictionary
    # Check if the "Title" property exists and print its structure
    if "Title" in page["properties"]:
        if page["properties"]["Title"]:
            title_property = page["properties"]["Title"]
            if isinstance(title_property, dict):
                if "title" in title_property and "content" in title_property["title"][0]["text"]:
                    vitamin = title_property["title"][0]["text"]["content"]
                    # Get a one line overview from ChatGPT for each vitamin found
                    question = f"Give me a one line overview of the supplement called {vitamin}"
                    # Push the result to the table
                    answer = call_chat_completion(question)
                    col = columns[i % 3]  # Cycle through the columns
                    push_to_expander(answer, vitamin, col)


# Display the table
display_table(st.session_state.table_data)

