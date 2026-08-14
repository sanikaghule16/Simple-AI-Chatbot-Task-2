print("FQA Chatbot")
print("Enter Bye To Exit.\n")
while True:
    user = input("You: ").lower()
    if user == "hi":
        print("Bot: Hello , How can i help you?")
    elif user == "what is python?":
        print("Bot: Python is a Programming Language")
    elif user == "what is ai?":
        print("Bot: AI is an Artificial Intelligence")
    elif user == "bye":
        print("Bot: Bye Have a Good Day!!")
        break
    else:
        print("Bot: Sorry,I don't understand your question")
