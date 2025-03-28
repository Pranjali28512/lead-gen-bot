import google.generativeai as genai

# Set up your API key
genai.configure(api_key="AIzaSyC-X1gMRJo2LHY6KnJAO2jc-EbVaIBnsbM")

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel('models/gemini-1.5-pro')  # Gemini Pro model
        response = model.generate_content(prompt)
        return response.text  # Get the AI's reply
    except Exception as e:
        return f"Error: {e}"

# Chatbot Interaction
print("Welcome to the AI Lead Generation Bot!")
name = input("What's your name? ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")

print(f"Thank you, {name}! Your details have been saved. We'll contact you soon.")

while True:
    user_input = input("Ask me anything about our services (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = ask_gemini(user_input)
    print("Bot:", response)