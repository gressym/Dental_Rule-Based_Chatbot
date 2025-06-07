
import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Dental Clinic Chatbot", layout="centered")
st.title("🦷 Dental Clinic Chatbot")
st.markdown("Type your question or message below to chat with the bot.")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if user_input:
    response = get_response(user_input)
    st.session_state.history.append(("You", user_input))

    if response == "book_appointment":
        st.session_state.history.append(("Bot", "Sure, I can help you with that. Let's book your appointment!"))
        with st.form("booking_form"):
            name = st.text_input("Your Full Name")
            date = st.date_input("Preferred Date")
            time = st.time_input("Preferred Time")
            mobile = st.text_input("Mobile Number")
            submit = st.form_submit_button("Confirm Appointment")

            if submit:
                st.success(f"Appointment booked for {name} on {date} at {time}. We will confirm via {mobile}.")
                st.session_state.history.append(("Bot", f"Appointment booked for {name} on {date} at {time}."))
    else:
        st.session_state.history.append(("Bot", response))

# Show the conversation history
st.divider()
st.markdown("### 💬 Chat History")
for speaker, message in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧍‍♂️ {speaker}:** {message}")
    else:
        st.markdown(f"**🤖 {speaker}:** {message}")
