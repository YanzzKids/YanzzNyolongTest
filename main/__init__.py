#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27621449
API_HASH = "b1118d4dd11827478807d36b317db4be"
BOT_TOKEN = "5407885401:AAFILdkfTWHZZ1TeJT63gp_4V42if5JvzhY"
SESSION = "BQDFEbC_NhWKlqD6tn7tMuCqI6jCGK2RTGvH_C2etFkdB1jPGIdirZHTZi-2ni5P4AYkuwfrPoA5Zg070_2KsdBYdrZMUMGF9Je583cR1vbNSbAugQbJI9eqzGirjZJNc5pflRM_8U26ngYi6uJ_dGe1DWD8LETUXvYQZZN8iuYGvArNJTgc4qPS0eycIjuCXRoroLkmSFKNope5oMHOiwI9NhrrtEH06wqNdf4dw64X3aQbMrLhrPrDqytN2GKwnqzPq5QvYN3bqy-A7RPs5Ey6SV4RIPIM1l_jHUl4xSNXFcR49rHxiF3U0UytCx-HT2b38QFwMQp7BprvjgLhjlCLVbgQA"
FORCESUB = "YanzzUcull"
AUTH = 1438138105

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
