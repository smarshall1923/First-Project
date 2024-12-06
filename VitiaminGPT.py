# Import the required libraries

from dotenv import load_dotenv
load_dotenv()
import os
import openai
import requests

openai.api_key = "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"
NOTION_TOKEN = "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"
DATABASE_ID = "5d35421663fe448a87dc15cfd30a6c9b"
#DATABASE_ID = os.getenv("DATABASE_ID")

# Call OpenAI API
def CallChatCompletion(Question: str):
    chat_completion = openai.ChatCompletion.create(
        messages=[
            {
                "role": "user",
                "content": Question,
            }
        ],
        model="gpt-4o",
    )
    # Extract the content from the response
    return chat_completion.choices[0].message['content']

#DATABASESE_ID = os.getenv("DATABASE_ID")
#print(chat_completion.choices[0].message['content'])

# Notion Integration Setup
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

#Read thru the Notion Pages
def get_pages(num_pages=None):
    
    #If num_pages is None, get all pages, otherwise just the defined number.
    
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    new_var = num_pages is None
    get_all = new_var
    page_size = 100 if get_all else num_pages
    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    if 'results' not in data:
        raise KeyError("'results' key not found in the response data")
    results = data["results"]
    while data.get("has_more") and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])
    return results


# Get the information from the Notion database
pages = get_pages()
for page in pages:
    #Look thru the dictionary
    # Check if the "Title" property exists and print its structure
    if "Title" in page["properties"]:
        if page["properties"]["Title"]:
            title_property = page["properties"]["Title"]
            if isinstance(title_property, dict):
                if "title" in title_property and "content" in title_property["title"][0]["text"]:
                    content = title_property["title"][0]["text"]["content"]
                    #Get a one line overview from ChatGPT for each vitamin found
                    question = "Give me a one line overview of the suppliment called" + content
                    print(CallChatCompletion(question))




