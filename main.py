from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
import random

Alif=Client(
    "Pyrogram bot",
    bot_token="5138195964:AAFY2hPs9A5eZe5ncd0Ox1DF9zo25utA7_Q",
    api_id="17863381",
    api_hash="793044f52346c11ab8cb792325dfbc5d",
    plugins=dict(root="Pyrogrambot")
)


Alif.run()
