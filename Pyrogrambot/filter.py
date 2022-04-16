from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@Client.on_message(filters.regex("hi") | filters.regex("Hi")                  
async def regex(bot, msg):
    await msg.reply_text(
        text="hi",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg"),
            InlineKeyboardButton("alert", callback_data="hi"),
            InlineKeyboardButton("Help", callback_data="help")
            ],[
            InlineKeyboardButton("NEXT", callback_data="close")
            ]]
            )
         )
