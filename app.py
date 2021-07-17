import random
import re
from flask import Flask, request
import boto3
import telegram
from telebot.credentials import bot_token, bot_user_name, URL, aws_access_key_id, aws_secret_access_key
from time import sleep, time
from io import BytesIO 

def get_an_x(key: str) -> str:
  session = boto3.Session(aws_access_key_id="AKIAVI6P3SPVVXYIYE4D", aws_secret_access_key="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", region_name="ap-southeast-1")
  bucket = "noripetsu-bot"

  s3_client = session.client("s3")
  res = s3_client.list_objects(Bucket=bucket, Prefix="{}/".format(key), MaxKeys=1000)
  number_of_x = len(res["Contents"])
  pick = key + "/" +  str(random.randint(1,number_of_x-1)) + ".txt"

  f = BytesIO()
  s3_client.download_fileobj(bucket, pick,f)

  return f.getvalue().decode("utf-8")

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
   text = update.effective_message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       bot_welcome = """
       HELLO POK, WHY ARE YOU NOT DOING WORK?
       """
       bot.sendChatAction(chat_id=chat_id, action="typing")
       sleep(1.35)
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
        msg = get_an_x(key="fact")
        bot.sendChatAction(chat_id=chat_id, action="typing")
        sleep(1.5)
        bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=msg_id)
   elif text == "/story":
        msg = get_an_x(key="story")
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
        msg = get_an_x(key="joke")
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
