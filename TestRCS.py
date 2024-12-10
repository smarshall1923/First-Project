
import streamlit as st
from streamlit_javascript import st_javascript

result = st_javascript("console.log('Hello from JavaScript!'); return 'This is a message from JavaScript';")

st.write(result)