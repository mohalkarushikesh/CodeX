# CodeX AI Chatbot

CodeX AI Chatbot is a simple interactive chatbot that communicates with the Gemini AI API to generate responses based on user input. It also features offline speech synthesis using `pyttsx3` for text-to-speech conversion.

## Features
- **AI-Powered Responses**: Interacts with the Gemini AI API to generate intelligent replies.
- **Offline Speech Synthesis**: Uses `pyttsx3` to convert chatbot responses into spoken words.
- **Interactive Chat Loop**: Users can engage in real-time conversations with the chatbot.
- **Error Handling**: Provides informative error messages when API requests fail.

## Requirements
Before running the chatbot, ensure you have the following dependencies installed:

```bash
pip install requests pyttsx3
```

## Setup Instructions
1. Clone or download the project.
2. Install the required Python packages using the command above.
3. Replace `"your_gemini_api_key"` with your actual Gemini API key.

## Usage
Run the script using:

```bash
python chatbot.py
```

Then, enter your messages and receive AI-generated responses. Type `'exit'` to end the chat.

## Error Handling
- The chatbot gracefully handles API errors and displays appropriate messages.
- If the AI service is overloaded (`Error 503`), users are encouraged to retry later.
- Any unexpected connection issues will be reported to ensure smooth debugging.

## Notes
- The chatbot currently supports text-based input/output.
- Future improvements may include enhancements like GUI integration or additional speech features.


