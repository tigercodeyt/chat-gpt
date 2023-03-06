import time
import openai
import pyttsx3

openai.api_key = "YOUR_API_CODE"
print("="*50)
print("CHATSTAR BY TIGER CODE YT")
print("CREATED BY MUHAMMAD ABBAS")
print("="*50)

# Set up the language model
model_engine = "text-davinci-003"

# Set up the text-to-speech engine with a human-like voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change to the second voice in the list

# Set the rate and volume of the speech
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# Typewriter effect function
def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


# Loop indefinitely
while True:
    print("  ")
    # Get input from the user
    prompt = input("You: ")
    print("  ")
    # Set the maximum number of tokens to generate in the response
    max_tokens = 1024

    # Check if the user input is "who made you"
    if prompt.lower() == "who made you":
        response = "My Best friend Muhammad Abbas."
    else:
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Get the response from the OpenAI API
        response = completion.choices[0].text.strip()

    # Print the response with typewriter effect
    typewriter_effect("CHATSTAR: " + response)

    # Speak the response after the typing effect finishes
    spoken_response = response.replace("CHATSTAR: ", "")  # Remove "CHATSTAR: " prefix from spoken text
    engine.say(spoken_response)
    engine.runAndWait()


# Loop indefinitely
    while True:
        print("  ")
        # Get input from the user
        prompt = input("You: ")
        print("  ")
        # Set the maximum number of tokens to generate in the response
        max_tokens = 1024

        # Check if the user input is "who made you"
        if prompt.lower() == "who made you":
            response = "My Best friend Muhammad Abbas."
        else:
            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=0.5,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Get the response from the OpenAI API
            response = completion.choices[0].text.strip()

        # Print and speak the response with typewriter effect
        typewriter_effect("CHATSTAR: " + response)
