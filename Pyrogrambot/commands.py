from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random


ALL_PIC = [
 "https://telegra.ph/file/a34f48501859a206568c1.jpg",
 "https://telegra.ph/file/d2e8841b6bca68760df39.jpg",
 "https://telegra.ph/file/0f618d79c4084b48140c2.jpg"
]


@Alif.on_message(filters.private & filters.command("start"))           
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"hey {message.from_user.mention}do [hi](https://t.me/CinemaChandagroup)",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg"),
            InlineKeyboardButton("alert", callback_data="hi"),
            InlineKeyboardButton("Help", callback_data="help")
            ],[
            InlineKeyboardButton("NEXT", callback_data="close")
            ]]
            )
         )


@Alif.on_message(filters.command("id"))
async def demo(bot, msege):
    text = f"""
First Name = {msege.from_user.first_name}
Last name = {msege.from_user.last_name}
User name = @{msege.from_user.username}
Id = <code>{msege.from_user.id}</code>
Mentoin = {msege.from_user.mention}"""
    await msege.reply_text(text=text)

@Alif.on_message(filters.command("sticker"))
async def ok(bot, ok):
    await ok.reply_sticker(
        sticker="CAACAgUAAxkBAAECBmxiGga9aXAaMGMLGsydNoQffbqNYwACJAADsx6IFZIHKachbCv9HgQ",
        reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton("hi", url="t.me/Alifmuhammed_tg")
        ]]
       )
    )

#video

@Alif.on_message(filters.command("video"))
async def da(bot, da):
    await da.reply_video(
    video="https://telegra.ph/file/3c5119738b90107900c08.mp4",
    caption="hi bro",
    reply_markup=InlineKeyboardMarkup( [[
    InlineKeyboardButton("hi", url="t.me/Alifmuhammed_tg")
    ]]
   )
  )
