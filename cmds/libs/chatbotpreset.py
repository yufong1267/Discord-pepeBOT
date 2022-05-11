from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
 
#creating a new chatbot
chatbot = ChatBot('Edureka')
trainer = ListTrainer(chatbot)
trainer.train([ 'hi, can I help you find a course', 'sure I would love to find you a course', 'your course have been selected'])
trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])

trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])
#getting a response from the chatbot
response = chatbot.get_response("hello")
print(response)