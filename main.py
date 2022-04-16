from pyrogram import Client
from Config import BOT_TOKEN, API_ID, API_HASH

Alif=Client(
    "Pyrogram bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="Pyrogrambot")
)


Alif.run()
