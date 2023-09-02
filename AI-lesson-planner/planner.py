import streamlit as st
import openai
import time

openai.api_key = "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"
st.title("Study scheduler using ai ")

age = st.number_input("Enter learner's age",min_value=6,max_value=80,step=1)

subject = st.text_area("Enter the subject")

topic = st.text_area("Enter the topic of your Subject")

complexity_levels = ["Beginner",'Intermediate','Advanced']
complexity = st.selectbox("Select the complexity", complexity_levels)

duration = ['1 week','15 days','10 days','20 days','1 month']
#duration = st.text_area("Enter the duration of study")
plan_duration = st.selectbox("Choose your duration", duration)

if st.button("Generate schedule"):
    prompt = f"You are tasked to produce an detailed schedule plan to study {subject} on the topic {topic} and to age {age} year old student and schedule should be designed for {plan_duration} and give details on each day topics display all needed content concisely in 4000 tokens"

    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        temperature = 0.7,
        n = 1,
        stop = None
    )
    time.sleep(20) 
    lesson_plan = response.choices[0].text.strip()
    st.subheader("Generated study schedule")

    st.write(lesson_plan)

