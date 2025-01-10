import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# fine-tuned model
model_path = r"C:\Users\Satchal Patil\DATASCIPRAC\DSP4codesnipp\t5_finetuned\checkpoint-3775"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

# Define a function for inference
def generate_code(query):
    query = query.lower()
    input_text = "generate code: " + query
    input_ids = tokenizer.encode(input_text, max_length=128, truncation=True, padding="max_length", return_tensors="pt")
    outputs = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit app
st.set_page_config(
    page_title="Code Generation App",
    page_icon="🤖",
    layout="centered",
)

st.title("🚀 Code Generation Using Fine-Tuned T5 Model")
st.markdown(
    """
    Enter a description of the code you'd like to generate, and let the model do the rest!
    """
)

# Input field 
with st.form("code_generation_form"):
    query = st.text_area(
        "Enter your query to generate code:",
        placeholder="e.g., How to write a list comprehension in Python?",
        height=100,
    )
    submit_button = st.form_submit_button("Generate Code")

# Display generated code
if submit_button:
    if query.strip():
        with st.spinner("Generating code... Please wait"):
            code = generate_code(query.strip())
        st.subheader("📝 Generated Code:")
        st.code(code, language="python")

        # Copy functionality
        st.button("📋 Copy Code", on_click=st.write, args=("Generated Code Copied!",))
        st.text("Copy the code manually if the button is not supported.")
    else:
        st.warning("⚠️ Please enter a query to generate code.")
