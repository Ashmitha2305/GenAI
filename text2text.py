iimport streamlit as st
import cohere

# Setup Cohere API key
COHERE_API_KEY = "IJrKNPVrXFiU7esQWNOYZOZ7CnjTCF7vFNmbO6tH"
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI
st.set_page_config(page_title="Text Summarizer with Cohere", layout="centered")
st.title("📝 Text Summarizer")
st.markdown("Enter a paragraph or long text and get a concise summary using Cohere's AI model.")

# Text input
text = st.text_area("Enter the text to summarize:", height=200)

# Parameters
length_option = st.selectbox("Select summary length", ["short", "medium", "long"])
format_option = st.selectbox("Select output format", ["paragraph", "bullets"])

# Submit button
if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = co.summarize(
                    text=text,
                    length=length_option,
                    format=format_option,
                    model='command-light'  # You can also try 'command-nightly'
                )
                st.success("Summary:")
                st.write(response.summary)
            except Exception as e:
                st.error(f"Error: {e}")mport streamlit as st
import openai

# Replace with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

st.title("Text Summarizer Chatbot 🤖")

with st.chat_message("user"):
    user_input = st.text_area("Enter the text you want to summarize:", height=200)

if st.button("Summarize"):
    if user_input:
        with st.spinner("Summarizing..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that summarizes text."},
                        {"role": "user", "content": f"Summarize the following text:\n\n{user_input}"}
                    ],
                    temperature=0.5,
                    max_tokens=150
                )
                summary = response["choices"][0]["message"]["content"]
                with st.chat_message("assistant"):
                    st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text.")
