import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL
from time import sleep, time

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   print(request.get_json(force=True))
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.effective_message.chat.id
   msg_id = update.effective_message.message_id

   time_mod_10 = int(time()) % 10

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       HELLO POK, WHY ARE YOU NOT DOING WORK?
       """
       # send the welcoming message
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)
   elif text == "/money":
       msg = """
       NO
       """
       bot.sendChatAction(chat_id=chat_id, action="typing")
       sleep(1.25)
       bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/love":
       msg = """
       hughug
       """
       bot.sendChatAction(chat_id=chat_id, action="typing")
       sleep(1.5)
       bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/kisskiss":
        msg = """
        lovelove
        """
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/fact":
        if time_mod_10 == 0:
            msg = """
            Did you know the arc d'triomphe is a copy of the arc in Rome?
            """
        elif time_mod_10 == 1:
            msg = """
            Did you know it's cheaper to buy a book of 10 metro tickets then each one individually? 
            """
        elif time_mod_10 == 2:
            msg = """
            Did you know Pyramides has tons of terrific Korean restos nearby?
            """
        elif time_mod_10 == 3:
            msg = """
            Did you know you shouldn't propose to a girl if she's standing in front of a rubbish bin?
            """
        elif time_mod_10 == 4:
            msg = """
            Did you know Carrefour prices are lower outside of the city centre?
            """
        elif time_mod_10 == 5:
            msg = """
            The quickest way to a girl heart is to bang nails into her wall
            """
        elif time_mod_10 == 6:
            msg = """
            You can get a tarte aux fraises and tartes au citron at a bargain at Monoprix
            """
        elif time_mod_10 == 7:
            msg = """
            Don't cross the skiis going downhill or you're gonna have bad time
            """
        elif time_mod_10 == 8:
            msg = """
            Helsinki airport sells fantastic hotdogs. The secret is in the garnish.
            """
        elif time_mod_10 == 9:
            msg = """
            Place d'Italie is now Chinatown.
            """
        else:
            msg = """
            Did you know Ryanair baggage bins can be outsmarted by zipping up the expandable section?
            """
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/story":
        if time_mod_10 == 0:
            msg = """
            Once upon a time, a girl got onto a bus and fell asleep. Normnorm went to the toilet and she got kidnapped. End of story. 
            """
        elif time_mod_10 == 1:
            msg = """
            Once upon a time, a girl took a train to Colmar cuz all her roomies were jerks. She ate a deliciously sweet broccoli and didn't finish her onion soup. End of story
            """
        elif time_mod_10 == 2:
            msg = """
            Once upon a time, a girl had korean bbq, and she had it the next week and the week after. Her bf then died from kimchi poisoning. End of story.
            """
        elif time_mod_10 == 3:
            msg = """
            Once upon a time, a girl went to Poland to stay in a sketchy apartment. She exchanged contacts with stranges and took pictures of architecture. End of story.
            """
        elif time_mod_10 == 4:
            msg = """
            Once upon a time, a girl had a boyfriend who scored 100 points at arcade basketball. Then she met one who could tell her fun facts and changed boyfriends. End of story.
            """
        elif time_mod_10 == 5:
            msg = """
            Once upon a time, a girl went to Paris but spoke no French. Then she learnt un hotdog svp and went clubbing at Montparnasse with Daisy. End of story.
            """
        elif time_mod_10 == 6:
            msg = """
            Once upon a time, a girl lived in the topmost apartment in Paris. Her roomies kept leaving cups on top of her wardrobe. In return she fed them cough medicine. End of story.
            """
        elif time_mod_10 == 7:
            msg = """
            Once upon a time, a girl put a bag of rice into a rice cooker and flew to Paris. Her roomies ate all of her rice and made her cook marmite chicken. End of story.
            """
        elif time_mod_10 == 8:
            msg = """
            Once upon a time, a girl went walking in Florence by herself because her roomies wanted to stay in. She took the most beautiful photos and sat at a cafe. End of story.
            """
        elif time_mod_10 == 9:
            msg = """
            Once upon a time, a girl stayed at St. Kilda and wanted to visit relatives in the city. She walked 40 min to the city centre and enjoyed roast duck at Chinatown. They had season parking. End of story.
            """
        else:
            msg = """
            Once upon a time, a girl landed in Paris and thought Kah Wee is Normnorm despite the fact that Normnorm looks like Jungkook. End of story.
            """
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/hughug":
        msg = """
        kisskiss
        """
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/joke":
        msg = """
        What do you call a group of puns? Answer: A punnet of puns. HAHAHA!
        """
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   else:
       try:
           # clear the message we got from any non alphabets
           text = re.sub(r"\W", "_", text)
           # create the api link for the avatar based on http://avatars.adorable.io/
           url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
           # reply with a photo to the name the user sent,
           # note that you can send photos by url and telegram will fetch it for you
           bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
           bot.sendChatAction(chat_id=chat_id, action="typing")
           sleep(2)
           bot.sendMessage(chat_id=chat_id, text="STOP PLAYING WITH A BOT AND WORK", reply_to_message_id=msg_id)
       except Exception:
           # if things went wrong
           bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
  return '.'

if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
