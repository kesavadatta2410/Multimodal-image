import streamlit as st
from agent.agent import run_from_bytes
import json

# Page configuration
st.set_page_config(
    page_title="Multimodal Agent",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Multimodal Agent")

# Sidebar inputs
# Sidebar inputs
with st.sidebar:
    st.header("Input")

    with st.form("input_form"):
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp", "gif"])
        instruction = st.text_input("Question / instruction")
        context = st.text_area("Additional context (optional)")
        submit = st.form_submit_button("Run")

# Main area
if uploaded_file and instruction and submit:
    try:
        image_bytes = uploaded_file.read()
        result = run_from_bytes(
            image_bytes=image_bytes,
            filename=uploaded_file.name,
            instruction=instruction,
            context=context,
        )
        st.subheader("Result")
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Upload an image, enter a question, and click **Run** in the sidebar to see results.")
