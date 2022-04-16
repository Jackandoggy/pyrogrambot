from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
import random

Alif=Client(
    "Pyrogram bot",
    bot_token="5138195964:AAFY2hPs9A5eZe5ncd0Ox1DF9zo25utA7_Q",
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
  InlineKeyboardButton("MY DEV", url="t.me/Alifmuhammed_tg"),
  InlineKeyboardButton("NEXT", callback_data="start")
  ]]


@Alif.on_message(filters.private & filters.command("start"))           
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"hey {message.from_user.mention}do [hi](https://t.me/CinemaChandagroup)",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg"),
            InlineKeyboardButton("alert", callback_data="alert")
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



@Alif.on_callback_query()
async def callback (bot, mmt : CallbackQuery):
    if mmt.data == "mm":  
        await mmt.message.edit(  
            text="hi bro"
        )
     
    elif mmt.data == "okbro":
        await mmt.message.edit(
            text="seen",
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("😃" , callback_data = "mm")
               ]]
           )
        )


    elif mmt.data == "close":
        await mmt.message.delete()



@Alif.on_callback_query()
async def callback_data (bots, msg : CallbackQuery):
    if msg.data ==  "alert":  
        await msg.answer("bye")














Alif.run()
