

#  Dental_RuleBased_Chatbot

A simple **rule-based chatbot** built using **Python** and **Streamlit** that helps users interact with a virtual dental assistant. It answers frequently asked questions and assists with appointment bookings.

---

## 📌 Project Structure

```
dental_clinic_chatbot/
├── chatbot.py          # Core chatbot logic (rule-based)
├── frontend.py         # Streamlit UI interface for the chatbot
├── README.md           # Project overview and instructions
```

---

## 💬 Features

- Greets users and responds to common dental clinic queries.
- Handles unknown questions with a polite default response.
- Supports appointment booking via a conversational form.
- Simple, keyword-based rule engine — no machine learning.
- Cleanly structured with clear function separation for logic and UI.

---

## 🛠️ Technologies Used

- **Python**: Core programming logic
- **Streamlit**: Interactive UI for web interface
- **Basic NLP**: Keyword-based response matching

---

## 🚀 How to Run the Project

### 🧑‍💻 Prerequisites:
- Python 
- Pip (Python package manager)

### 📦 Step 1: Install Dependencies

```bash
pip install streamlit
```

### ▶️ Step 2: Run the Chatbot UI

```bash
streamlit run app.py
```

### ✅ Frequent Questions can be like this !
- Start chatting by entering your queries.
- Try questions like:
  - "What are your working hours?"
  - "Where is your clinic located?"
  - "Do you accept insurance?"
  - "Book appointment"

---

## 📂 Logic Overview

### `chatbot.py`:
- Contains the chatbot logic via `get_response(user_input)`
- Uses `if-else` and keyword matching to answer questions
- Includes a `book_appointment()` function for handling multi-step inputs

### `frontend.py`:
- Streamlit UI to interface with the chatbot
- Uses forms to take structured input for appointments
- Maintains chat history using `st.session_state`

---

## 🌱 Future Improvements

- ✅ Add user authentication for recurring patients  
- 🤖 Integrate ML-based intent classification (e.g., spaCy or HuggingFace)  
- 📞 Real-time calendar integration with Google Calendar API  
- 📊 Admin dashboard for viewing appointment stats  
- 💬 Add voice input and text-to-speech for accessibility

---


Created as a part of an internship technical task.  
