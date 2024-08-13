# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# personal_bot.py


class PersonalBot:
    def __init__(self):
        # Define some predefined responses
        # auto capitalize
        # Normalize the question to lower case for consistent matching
        self.responses = {
            "what is your favorite color": "I don't have eyes, but I think blue is nice!",
            "what is the meaning of life": "The meaning of life is to find your own purpose and enjoy the journey!",
            "are you single": "I don't love",
            "hey": "hey too i'm beast an AI assistant ready to help",
            "hi": "hi too i'm beast an AI assistant ready to help",
            "what is your name?": "I'm your friendly personal bot!",
            "how are you?": "I'm good, and thanks for asking! 😊",
            "what can you do": "I can answer your questions and keep you entertained!",
            "hello": "Hi there! How can I help you today?",
            "how are you": "I'm just a bot, but I'm here and ready to assist you!",
            "what is your name": "I'm your friendly personal bot. You can call me Beast😎💪!",
            "help": "Sure! You can ask me about my features or anything else you need help with.",
            "thank you": "You're welcome! If you need anything else, just let me know.",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, question):
        # Normalize the question to lower case for consistent matching
        question = question.lower()
        # Return a predefined response if it exists
        return self.responses.get(question, "Sorry, I don't understand that question.")


def main():
    bot = PersonalBot()
    print("Welcome! i'm beast an AI assistant ready to help")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Bot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
