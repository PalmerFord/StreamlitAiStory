# Plamere waz here lmao

import streamlit as st
import random

def generate_story():
    # Random story stuff
    characters = ["Palmer", "Sawyer"]
    places = ["a Coca Cola factory", "Home Depot", "McDonalds", "the White House", "Calvin University", "Hope College"]
    antagonists = ["the IRS", "Joe Biden", "Taylor Swift", "the French"]

    # Generate a random bs story
    character = random.choice(characters)
    place = random.choice(places)
    antagonist = random.choice(antagonists)

    story = f"{character} went to {place} to do battle with {antagonist}."

    return story

# Streamlit app yaaay :D
def main():
    st.title("Story Generator")

    # Button to generate new story
    if st.button("Generate Story"):

        story = generate_story()

        st.write("Your Story:")
        st.write(story)

if __name__ == "__main__":
    main()
