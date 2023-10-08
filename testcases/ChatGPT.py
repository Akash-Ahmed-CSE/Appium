import openai
import pyttsx3
import time

# Set your OpenAI API key here
openai.api_key = "sk-D3yWrd8ZRNxmuoez8DFgT3B1bkFJ8ØXRdtvpM92eHQ5QkSØZ"

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to make ChatGPT respond
def get_gpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()


# Function to make ChatGPT talk
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Main conversation loop
if __name__ == "__main__":
    speak("Hello! I am ChatGPT. How can I assist you?")

    while True:
        user_input = input("You: ")
        prompt = f"You: {user_input}\nChatGPT:"

        response = get_gpt_response(prompt)
        print(f"ChatGPT: {response}")
        speak(response)

        if "goodbye" in user_input.lower():
            speak("Goodbye!")
            break
