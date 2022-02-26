from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import random

Alif=Client(
    "Pyrogram bot",
    bot_token="5257455119:AAHHq3lOpT6j0JcM8EMpI6w8l-uR2OrKNLM",
    api_id="17863381",
    api_hash="793044f52346c11ab8cb792325dfbc5d"
)


ALL_PIC = [
 "https://telegra.ph/file/a34f48501859a206568c1.jpg",
 "https://telegra.ph/file/d2e8841b6bca68760df39.jpg",
 "https://telegra.ph/file/0f618d79c4084b48140c2.jpg"
]

INFO_MESSAGE = """
Bye {} I am not alive 😢 
So Please Request Again 
"""

INFO_BUTTON = [[
  InlineKeyboardButton("MY DEV", url="t.me/Alifmuhammed_tg")
  ]]


@Alif.on_message(filters.private & filters.command("start"))           
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"hey {message.from_user.mention}",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg")
            ]]
            )
         )

@Alif.on_message(filters.command("info"))           
async def start_message(bot, message):
    await message.reply_text(
         text=INFO_MESSAGE.format(message.from_user.mention),
         Reply_markup=InlineKeyboardMarkup(INFO_BUTTON)
    )



@Alif.on_message(filters.command("start"))
async def demo(bot, msege):
    text = f"""
First Name = {msege.from_user.first_name}
Last name = {msege.from_user.last_name}
User name = @{msege.from_user.username}
Id = {msege.from_user.id}
Mentoin = {message.from_user.mention}"""
    await msege.reply_text(text=text)









Alif.run()
