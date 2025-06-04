import requests
import pyttsx3

# Set API Key
API_KEY = "your_gemini_api_key"  # Replace with your actual key
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Function to interact with Gemini AI API
def get_ai_response(user_input):
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [{"text": user_input}]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 503:
            return "Error 503: The model is overloaded. Please try again later."
        elif response.status_code != 200:
            return f"Error {response.status_code}: {response.json().get('error', {}).get('message', 'Unknown error')}"

        response_json = response.json()

        if "candidates" in response_json and response_json["candidates"]:
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: No valid response received. Check API request format."

    except requests.exceptions.RequestException as e:
        return f"Request Error: {str(e)}"

# Function to convert chatbot response to speech (Offline)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Interactive Chat Loop (Text Input + Speech Output)
print("💬 CodeX AI Chatbot - Type 'exit' to quit\n")
while True:
    user_input = input("You: ")  # Text input only

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    print("🤖 Thinking...\n")

    ai_response = get_ai_response(user_input)
    print(f"🦾 CodeX: {ai_response}\n")

    speak(ai_response)  # Convert AI response to speech

