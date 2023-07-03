import random
import re
import nltk
from nltk.chat.util import Chat, reflections
import webbrowser
import pywhatkit

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello, how can I help you?"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. I am here to assist you."]
    ],
    [
        r"how are you?",
        ["I am doing well, thank you. How can I assist you today?"]
    ],
    [
        r"what can you do?",
        ["I can assist you with any questions or concerns you may have. Just ask!"]
    ],
    [
        r"quit",
        ["Thank you for chatting with me. Have a great day!"]
    ],
    [
        r"open google",
        ["Opening Google..."]
    ],
    [
        r"open youtube",
        ["Opening YouTube..."]
    ],
    [
        r"search (.*) on google",
        ["Searching for %1 on Google..."]
    ],
    [
        r"search (.*) on youtube",
        ["Searching for %1 on YouTube..."]
    ],
    [
        r"play (.*) ",
        ["playing for %1 on YouTube..."]
    ]
]

chatbot = Chat(pairs, reflections)

def google():
    webbrowser.open("https://www.google.com")

def youtube():
    webbrowser.open("https://www.youtube.com")

def search_on_google(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

def search_on_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(url)

def play_on_youtube(query):
    pywhatkit.playonyt(query)

def respond(user_input):
    if user_input.lower() == "open google":
        google()
    elif user_input.lower() == "open youtube":
        youtube()
    else:
        match = None
        for pattern, responses in pairs:
            match = re.match(pattern, user_input)
            if match:
                response = random.choice(responses)
                if "%1" in response:
                    response = response.replace("%1", match.group(1))
                if "google" in user_input:
                    search_on_google(match.group(1))
                elif "youtube" in user_input:
                    if "search" in user_input:
                        search_on_youtube(match.group(1))
                    elif "play" in user_input:
                        play_on_youtube(match.group(1))
                    else:
                        print(response)
                elif "play" in user_input:
                    play_on_youtube(match.group(1))
                else:
                    print(response)

while True:
    user_input = input("You: ")
    respond(user_input)
