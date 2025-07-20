import google.generativeai as genai

#  Configure API key
genai.configure(api_key="Here_Your_API_Key") # Please enter your API key

#  Create the model instance
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

#  Start a chat session
chat = model.start_chat(history=[
    {
        "role": "model",
        "parts": ["You are a virtual assistant named Jarvis developed by ShamsulHaq skilled in general tasks like Google Cloud, Gemini, Alexa etc."]
    }
])

#  Send a user message and get response
response = chat.send_message("What is coding?")

#  Print the response
print("Jarvis:", response.text)
