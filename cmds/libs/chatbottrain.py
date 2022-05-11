from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from find_path import GetFileList
import spacy
import yaml


chatbot = ChatBot('Training Example')
trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train(
     "./conversation.yml"
)

#get all train data(.yml)
dir_list ,yml_list = GetFileList().FileList("chat_crops\\english")
for dirr in dir_list:
    print("chat_crops\\english\\" + dirr)
    dirData_list ,ymlData_list = GetFileList().FileList("chat_crops\\english\\" + dirr)
    for yml in ymlData_list:
        trainer.train("chat_crops\\english\\" + dirr + "\\" + yml)        

'''
trainer.train(
     "chat_crops\\english\\botprofile.yml"
)
'''

while True:
    i = input('>>> ').strip()
    if i != 'exit':
        print(chatbot.get_response(i))
    else:
        break   
