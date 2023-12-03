import streamlit as st
import random

#replace with openai api
def generate_story():
    # Add your story elements or fetch them from a database/API
    characters = ["Alice", "Bob", "Charlie", "David"]
    places = ["a small village", "a big city", "a magical kingdom", "an ancient forest"]
    actions = ["discovered a hidden treasure", "saved the day", "embarked on a mysterious journey", "learned a valuable lesson"]

    # Generate a random story
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)

    story = f"{character} was in {place} and {action}."

    return story

# Streamlit app
def main():
    st.title("Story Generator")

    # Button to generate a new story
    if st.button("Generate Story"):

        #replace with openai api
        story = generate_story()

        st.write("Your Story:")
        st.write(story)

if __name__ == "__main__":
    main()
