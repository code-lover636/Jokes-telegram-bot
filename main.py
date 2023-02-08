import telegram.ext
import requests

url = "https://joke110.p.rapidapi.com/random_joke"

headers = {
	"X-RapidAPI-Key": "15a2a9dc5bmsh020a3872b83c185p10621ejsnd08f0392c827",
	"X-RapidAPI-Host": "joke110.p.rapidapi.com"
}


apiKey = "6029344993:AAHNX0SaZ-KbL7ssrbNVdBpIIaygYuGGE1k"

def start(update, context):
    msg = """
    Hey! Are you bored?🥱
Wanna hear a joke?
Type /help to see what I can do.
    """
    update.message.reply_text(msg)
    
def help(update, context):
    msg = """
    Use the following commands to interact with me:
/start - Start the bot
/about - See information about the bot and creator
/joke - I will crack a joke
  
Are you lazy to type? You can also click the above links to send commands.
    """
    update.message.reply_text(msg)

def about(update, context):
    msg = """
    laughjokesbot makes you laugh.
This bot is made with Python Programming Language.
Creator & Owner: Aravind Ashokan
    """
    update.message.reply_text(msg)

def joke(update, context):
    response = requests.request("GET", url, headers=headers)
    if response: 
        update.message.reply_text(response.json()["setup"])
        update.message.reply_text(response.json()["punchline"])

    
updater = telegram.ext.Updater(apiKey, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("about", about))
disp.add_handler(telegram.ext.CommandHandler("joke", joke))


updater.start_polling()
updater.idle()
