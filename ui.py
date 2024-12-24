import streamlit as st

def push_to_expander(answer: str, vitamin: str, col):
    with col.expander(f"More Info On {vitamin}"):
        st.write(answer)

def display_table(data):
    df = pd.DataFrame(data)
    st.markdown(
        """
        <style>
        .dataframe th, .dataframe td {
            padding: 10px;
            text-align: left;
        }
        .dataframe td:nth-child(1) {
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.dataframe(df, width=1500, height=400)


"""
# Function to push the answer and vitamin to the table
def PushToTable(answer: str, vitamin: str):
    # Append new row to the table data
    st.session_state.table_data.append({"Vitamin": vitamin, "Answer": answer})
"""


# Function to create an xpandable section and show a message inside it
def PushToCard(answer: str, vitamin: str, unique_id: int):
    # Use st.markdown to inject custom CSS for the card
    st.markdown(
        """
        <style>
        .custom-card {
            width: 500px;  /* Adjust the width as needed */
            height: 300px; /* Adjust the height as needed */
            padding: 20px; /* Optional: Add padding for better spacing */
            border: 1px solid #ccc; /* Optional: Add a border */
            border-radius: 10px; /* Optional: Add rounded corners */
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Optional: Add a shadow */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Apply the custom CSS class to the card
    with ui.card(content=answer, key=f"{vitamin}-{unique_id}"):
        ui.card.__init__(vitamin)
        ui.textarea(answer)
        ui.button("More Info On " + vitamin)
