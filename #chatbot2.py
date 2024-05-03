#chatbot2
import nltk
from nltk.chat.util import Chat,reflections
pairs=[
    ['hello|hii|hey',['hello','hi there','hey']]
,['how are you',["i am good,thanks","i am doing well."]]
,['what is your name',['i am chatbot','call me a bot']],]
def chatbot():
    print("hello! how can i help you today?")
    chat=Chat(pairs,reflections)
    chat.converse()
if __name__=="--main--":
    chatbot()
    