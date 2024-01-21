from nltk.chat.util import Chat, reflections

chatbot_responses = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you!",
     "I'm doing well, how about you?"]),
    (r"what is your name?", ["I'm a chatbot.", "You can call me ChatGPT."]),
    (r"bye|goodbye", ["Goodbye!", "Bye bye!", "Take care!"]),
    (r"(.*) your name(.*)", ["My name is ChatGPT."]),
    (r"(.*) help (.*)",
     ["I'm here to help. What do you need assistance with?"]),
    (r"(.*) your favorite (.*)",
     ["I don't have preferences. I'm just a machine."]),
    (r"what can you do(.*)",
     ["I can answer questions, provide information, and chat with you."]),
    (r"tell me a joke|jokes", [
     "Why did the Python programmer get denied a loan? Because he had no collateral!"]),
    (r"(.*) (movie|film) recommendation(.*)",
     ["I recommend watching 'The Matrix'."]),
    (r"(.*) (weather|temperature) in (.*)",
     ["I'm sorry, I don't have real-time weather information."]),
    (r"define (.*)",
     ["I'm sorry, I don't have a dictionary. You can use online dictionaries for definitions."]),
    (r"tell me about yourself|who are you", [
     "I am a chatbot designed to assist and chat with you."]),
    (r"how old are you", [
     "I don't have an age. I'm just a program running on a computer."]),
    (r"(.*) programming language do you like",
     ["I'm language-agnostic. I don't have preferences."]),
    (r"(.*) (book|books) recommend(.*)",
     ["I recommend 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams."]),
    (r"(.*) (song|music) recommend(.*)",
     ["I recommend 'Bohemian Rhapsody' by Queen."]),
    (r"(.*) (sports|sport) do you like",
     ["I don't have personal preferences, but I can provide information about sports."]),
    (r"(.*) (technology|tech) news",
     ["I don't have real-time news updates, but I recommend checking reliable news sources."]),
    (r"how can I learn programming", [
     "You can start by choosing a programming language, finding online resources, and practicing coding regularly."]),
    (r"(.*) thank you", ["You're welcome!", "Anytime!", "Happy to help!"]),
    (r"(.*) (love|like) you",
     ["Thank you, but I'm just a machine. Let's continue the conversation!"])
]


# Simple memory feature
user_inputs = []


def simple_chatbot():
    print("Hello! I'm a chatbot.My name is zara. You can start chatting with me. Type 'bye' to exit.")

    # Create a Chat instance
    chat = Chat(chatbot_responses, reflections)

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'bye':
            print("Zara: Goodbye! see you soon")
            break

        # Check for repeated inputs
        if user_input in user_inputs:
            print(
                "Zara: I think we already discussed that. Let's talk about something else.")
            continue

        user_inputs.append(user_input)

        # Get a response from the chatbot
        response = chat.respond(user_input)

        # Print the response
        print(f"Zara: {response}")


if __name__ == "__main__":
    simple_chatbot()
