chat_bot = "Chatbot: Hello, I am your chatbot"
print(chat_bot)

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello"]:
        print("Chatbot: Hello! How are you?")
    elif user == "how are you":
        print("Chatbot: I am fine. What about you?")
    elif user == "i am fine":
        print("Chatbot: Nice to hear that!")
    elif user == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot: Sorry, I only understand hi, hello, how are you, i am fine, bye")
