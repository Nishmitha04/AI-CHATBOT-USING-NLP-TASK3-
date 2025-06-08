import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define some basic patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi :)"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by Python and NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm fine. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright", "Don't worry about it"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi, I'm your AI chatbot. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
