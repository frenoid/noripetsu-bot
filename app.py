import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name,URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

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
       bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/love":
       msg = """
       hughug
       """
       bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/kisskiss":
        msg = """
        lovelove
        """
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/fact":
        msg = """
        Did you the the arc d'triomphe is a copy of the arc in Rome?
        """
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/story":
        msg = """
        Once upon a time, a girl got onto a bus and fell asleep. Normnorm went to the toilet and she got kidnapped. End of story. 
        """
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/hughug":
        msg = """
        kisskiss
        """
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/joke":
        msg = """
        What do you call a group of puns? Answer: A punnet of puns. HAHAHA!
        """
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
