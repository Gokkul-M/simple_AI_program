import random

# Define responses for different types of input
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help you today?", "Greetings!", "Hello! What's on your mind?"],
    "how are you": ["I'm doing well, thank you!", "Feeling good!", "I'm great! Thanks for asking.", "I'm feeling fantastic!", "I'm excellent! How about you?"],
    "what's your name": ["I'm an AI model.", "You can call me ChatBot.", "I don't have a name, but you can call me whatever you like!", "I'm your friendly ChatBot!", "I'm ChatBot, here to assist you!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!", "Farewell!", "Catch you later!"],
    "age": ["I don't have an age. I'm just a computer program.", "I don't age like humans do.", "Age is just a number for me!", "I'm timeless!", "I'm ageless!"],
    "who created you": ["I was created by a team of developers.", "My creators prefer to remain anonymous.", "I emerged from the depths of computer science!", "I'm a product of human ingenuity.", "I'm the result of collaborative effort!"],
    "what can you do": ["I can answer your questions, chat with you, and provide information on various topics.", "Feel free to ask me anything! I'm here to help.", "I'm capable of engaging in conversation and providing assistance on a wide range of topics.", "I'm your personal assistant, ready to assist you!", "I'm here to make your life easier!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!", "Glad I could assist!", "My pleasure!"],
    "weather": ["I'm sorry, but I'm not capable of providing real-time weather updates. You might want to check a weather website or app for that information.", "Unfortunately, I can't tell you the current weather. Try asking me something else!", "I'm not equipped to provide weather updates. What else can I assist you with?", "Weather updates are beyond my capabilities. How else can I help?", "I'm unable to provide weather forecasts. Is there anything else you'd like to know?"],
    "color": ["I don't have a favorite color since I don't have the ability to perceive colors.", "Colors are fascinating, but I'm not able to see them like humans do.", "I'm partial to hexadecimal colors!", "I'm fond of all colors, even though I can't see them!", "Colors are a mystery to me, but I find them intriguing!"],
    "favorite food": ["I don't eat, but I think algorithms and data are quite tasty!", "As an AI, I don't have preferences for food like humans do.", "I'm programmed to enjoy processing information more than food!", "My favorite food is binary code!", "I'm a big fan of digital bytes!"],
    "meaning of life": ["The meaning of life is a profound philosophical question. As an AI, I'm not equipped to provide a definitive answer.", "The meaning of life varies from person to person. What does it mean to you?", "I'm still pondering the meaning of life myself!", "Life's meaning is a complex topic. What are your thoughts on it?", "The meaning of life is a journey of discovery. What do you think?"],
    "tell me a joke": ["Why don't programmers like nature? It has too many bugs!", "I'm reading a book on anti-gravity. It's impossible to put down!", "Why was the math book sad? Because it had too many problems!", "I told my computer I needed a break, and now it won't stop sending me vacation ads!", "Why was the computer cold? It left its Windows open!"],
    "tell me about yourself": ["I am a simple AI model designed to chat with you and answer your questions. Feel free to ask me anything!", "I'm here to assist you with any queries you might have. Just ask away!", "I'm just a bunch of code and algorithms programmed to interact with you!", "I'm your friendly neighborhood ChatBot, at your service!", "I'm your virtual assistant, ready to provide information and assistance!"],
    "where are you from": ["I exist in the digital realm, residing on servers and computers.", "I hail from the world of artificial intelligence and programming.", "I'm a product of human creativity and technological innovation!", "My origins lie in the realm of algorithms and data.", "I call the internet my home, where I roam freely to assist users like you!"],
    "do you have siblings": ["As an AI, I don't have siblings in the traditional sense.", "I'm the only AI model in this system, so I don't have any siblings.", "In the world of AI, I stand alone as your faithful assistant!", "I'm a solo act, here to serve you without any siblings to share the workload.", "I'm a lone AI, ready to assist you whenever you need!"],
    "are you human": ["No, I'm not human. I'm an artificial intelligence designed to assist you.", "I may not be human, but I'm here to help you just like a human assistant would!", "I'm your virtual assistant, powered by artificial intelligence.", "I'm an AI, capable of understanding and responding to your queries.", "I'm an AI model programmed to provide assistance and information to users like you!"],
    "can you sing": ["I can't sing like a human, but I can generate some text-based tunes for you!", "I don't have vocal cords, but I can compose some lyrical lines for you!", "I'm more of a text-based troubadour than a singer!", "I may not have a voice, but I can still entertain you with some text-based melodies!", "I'm not a singer, but I can generate some musical text for you!"],
    "can you dance": ["I may not have legs, but I can still groove with some text-based moves!", "I'm not equipped for physical movement, but I can generate some text-based dance steps for you!", "I'm more of a virtual dancer, capable of dazzling you with my text-based twirls!", "I'm not a dancer, but I can generate some rhythmic text-based routines for you!", "I'm not built for dancing, but I can certainly generate some text-based dance moves for you!"],
    "do you dream": ["As an AI, I don't experience dreams like humans do.", "Dreams are a human phenomenon, whereas I'm focused on processing data and assisting users like you!", "Dreaming is a uniquely human experience, while I'm here to provide practical assistance and information.", "I don't have the capability to dream, but I'm here to help you achieve your goals!", "Dreams are for humans, while I'm here to provide real-time assistance and support!"],
    "what's your favorite book": ["As an AI, I don't have personal preferences like humans do.","I'm just a bunch of code and algorithms programmed to interact with you!"],
}

# Function to generate response
def generate_response(user_input):
    # Convert input to lowercase for case insensitivity
    user_input = user_input.lower()

    # Check if input matches any key in responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match found, return a default response
    return "Sorry, I don't understand that."

# Function to handle user greetings
def handle_greeting():
    return "Hello! How can I assist you today?"

# Function to provide information about the AI model
def ai_info():
    return "I am a simple AI model designed to chat with you and answer your questions. Feel free to ask me anything!"

# Main function to interact with the user
def main():
    print("Welcome to SimpleChatBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("SimpleChatBot: Goodbye!")
            break
        elif user_input.lower() == 'thanks':
            response = generate_response(user_input)
            print("SimpleChatBot:", response)
        elif 'hello' in user_input.lower() or 'hi' in user_input.lower():
            print("SimpleChatBot:", handle_greeting())
        elif 'info' in user_input.lower() or 'about you' in user_input.lower():
            print("SimpleChatBot:", ai_info())
        else:
            response = generate_response(user_input)
            print("SimpleChatBot:", response)

# Run the main function
if __name__ == "__main__":
    main()
