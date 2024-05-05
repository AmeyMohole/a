from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        ["Chatbot: "+"Hello %1. How are you today?","Chatbot: "+"How may I help you?"]
    ],
    [
        r"(.*) name?",
        ["Chatbot: "+"I am a Chatbot. I don't have a particular name"]
    ],
    [
        r"How are you?",
        ["Chatbot: "+"I am fine.","Chatbot: "+"I am always happy to help"]
    ],
    [
        r"I am doing good",
        ["Chatbot: "+"Nice to hear that"]
    ],
    [
        r"Hi|Hello|Hey|hi|hello",
        ["Chatbot: "+"Hey there","Chatbot: "+"hello"]
    ],
    [
        r"(.*) created?",
        ["Chatbot: "+"I was made by a computer programmer"]
    ],
    [
        r"(.*) investments|money?",
        ["There are many options to invest money like mutual funds, regional banks, etc."]
    ],
    [
        r"(.*) stocks?",
        ["There are many companies to invest your money in."]
    ],
    [
        r"(.*) companies (.*) money?",
        ["Chatbot:" +"Amazon,Tesla"]
    ]
]

def chat():
    print("Hello I am a chatbot.Type 'quit' to exit")
    print("You:")
    obj = Chat(pairs,reflections)
    obj.converse()
chat()
