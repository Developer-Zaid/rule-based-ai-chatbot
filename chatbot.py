from datetime import datetime

INTENTS = {
    ("hello", "hi", "hey", "good morning", "good evening"):
        "Hello! Nice to meet you.",

    ("how are you",):
        "I'm doing great. Thanks for asking!",

    ("name", "who are you"):
        "I am DecodeBot, a rule-based AI chatbot.",

    ("help",):
        (
            "Available commands:\n"
            "- hello / hi / hey\n"
            "- how are you\n"
            "- name\n"
            "- date\n"
            "- time\n"
            "- thanks\n"
            "- bye"
        ),

    ("thanks", "thank you"):
        "You're welcome!"
}


def get_response(user_input):
    if user_input == "date":
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    if user_input == "time":
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    for keywords, response in INTENTS.items():
        if user_input in keywords:
            return response

    return "Sorry, I don't understand that command."


def main():
    print("=" * 50)
    print("🤖 DecodeBot")
    print("A Rule-Based AI Chatbot")
    print("Type 'help' to see commands.")
    print("Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ["bye", "exit", "quit"]:
            print("DecodeBot: Goodbye! Have a great day.")
            break

        print(f"DecodeBot: {get_response(user_input)}")


if __name__ == "__main__":
    main()
