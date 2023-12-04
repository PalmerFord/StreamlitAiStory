# Made by Palmer Ford 
# December 2, 2023

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key using st.secrets
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app
def main():
    st.set_page_config(
        page_title="AI Story Generator",
        page_icon="📚",
        layout="centered",
        initial_sidebar_state="collapsed",
        menu_items={
            'About': "Made by [Palmer Ford](https://github.com/PalmerFord)"
        }
    )

    st.title('AI Story Generator')

    tone = st.selectbox("Select Story Tone", ["normal", "funny", "serious", "sad", "acid trip"])
    main_characters = st.text_input("Main Character(s):")
    supporting_characters = st.text_input("Supporting Character(s):")
    settings = st.text_input("Setting(s):")
    antagonists = st.text_input("Antagonist(s):")
    other_info = st.text_input("Other Things to Mention:")

    if st.button("Generate Story"):
        # Display a message indicating that the story is being generated
        loading_message = st.text("Generating story. Please wait...")

        # OpenAI API call
        response = generate_story(main_characters, supporting_characters, settings, antagonists, other_info, tone)

        # Remove the loading message and display the generated story
        loading_message.empty()
        st.subheader("Generated Story:")
        st.markdown(response.choices[0].message.content)

def generate_story(main_characters, supporting_characters, settings, antagonists, other_info, tone):
    # Define system prompts for different tones
    system_prompts = {
        "normal": "You are an internet story writer that writes short stories who never writes generic stories and likes to add additional elements to a story to make it more engaging and unpredictable.",
        "funny": "You are an internet story writer that writes humorous short stories who never writes generic stories and likes to add additional elements to a story to make it more fun and unpredictable.",
        "serious": "You are an internet story writer that writes serious short stories who never writes generic stories and likes to add additional elements to a story to make it more engaging and unpredictable.  ",
        "sad": "You are an internet story writer that writes sad short stories who never writes generic stories and likes to add additional elements to a story to make it more engaging and unpredictable. Your stories are all tragedies.",
        "acid trip": "You are an internet story writer that crafts completely unpredictable, absurd, acid trip tales and likes to add additional elements to a story to make it more insane and unpredictable. The villain names you come up with are always completly unhinged."
    }

    # OpenAI API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{system_prompts[tone]} \n\nyou rarely start a story with once upon a time."},
            {
                "role": "user",
                "content": f"Main character(s): {main_characters}\n\n"
                           f"Supporting character(s): {supporting_characters}\n\n"
                           f"Setting(s): {settings}\n\n"
                           f"Antagonist(s): {antagonists}\n\n"
                           f"Other things to mention: {other_info}\n\n"
                           "Story:",
            },
        ],
        temperature=1.1,
        # max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

if __name__ == "__main__":
    main()