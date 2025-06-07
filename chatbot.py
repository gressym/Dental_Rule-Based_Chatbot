# A simple rule-based chatbot for a dental clinic

import os
import pandas as pd
from datetime import datetime

def save_appointment_to_excel(name, date, time, mobile, filename="appointments.xlsx"):
    """
    Save the appointment details to an Excel file.
    Creates the file if it doesn't exist, appends if it does.
    """
    new_entry = pd.DataFrame([{
        "Name": name,
        "Date": str(date),
        "Time": str(time),
        "Mobile": mobile,
        "Booked At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])

    if os.path.exists(filename):
        try:
            existing = pd.read_excel(filename)
            updated = pd.concat([existing, new_entry], ignore_index=True)
        except Exception:
            updated = new_entry  # fallback if corrupted
    else:
        updated = new_entry

    updated.to_excel(filename, index=False)


def get_response(user_input):
    """
    This function takes a user's question as input and returns a response based on keywords.
    """
    user_input = user_input.lower()
    
    # Greeting keywords
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! Welcome to the Dental Clinic. How can I assist you today?"

    # FAQ Keywords and Responses
    faq = {
        ("hours","schedule", "working","duration","open", "timing"): "Our clinic is open from 9 AM to 6 PM, Monday to Saturday.",
        ("location", "address", "where", "find", "direction"): "We are located at 123 Dental Street, Smileville.",
        ("insurance", "accept", "plan"): "Yes, we accept most major dental insurance plans. Please call us for more details.",
        ("book", "appointment"): "book_appointment",
        ("services", "offer", "provide"): "We offer a range of services including dental cleanings, fillings, root canals, and cosmetic dentistry.",
        ("emergency", "urgent"): "Yes, we offer emergency dental services. Please call us immediately at (123) 456-7890.",
        ("cost", "price", "fee", "much"): "The cost of our services varies. For a price estimate, please schedule a consultation with one of our dentists.",
        ("payment", "pay"): "We accept cash, credit/debit cards, and insurance. Payment is due at the time of service.",
        ("dentist", "doctor"): "We have a team of experienced and caring dentists. You can learn more about them on our website's 'About Us' page."
    }

    # Calculate a score for each possible response
    best_response = ""
    max_score = 0

    for keywords, response in faq.items():
        score = sum(word in user_input for word in keywords)
        if score > max_score:
            max_score = score
            best_response = response

    
    if max_score > 0:
        return best_response

    return "Sorry, I don't know that yet. Please try asking another question or rephrasing your current one."

def book_appointment():
    """
    Handles the multi-step appointment booking conversation.
    """
    print("Sure, I can help you with that. What is your full name?")
    name = input("> ")

    print(f"Thank you, {name}. What is your preferred date for the appointment?")
    date = input("> ")

    print("And what time would you prefer?")
    time = input("> ")

    print("Lastly, can I have your mobile number?")
    mobile = input("> ")

    print(f"Thank you! Your appointment is scheduled for {date} at {time}. We will send you a confirmation message shortly.")
    save_appointment_to_excel(name, date, time, mobile)

def main():
    """
    Main function 
    """
    print("Welcome to the Dental Clinic Chatbot! Ask me a question or type 'quit' to exit.")

    while True:
        user_question = input("> ")
        if user_question.lower() in ["quit", "exit", "bye", "goodbye"]:
            print("Thank you for visiting. Have a great day!")
            break
        
        response = get_response(user_question)

        if response == "book_appointment":
            book_appointment()
        else:
            print(response)

if __name__ == "__main__":
    main()
