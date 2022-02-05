from pyrogram import Client, filters
from pyrogram.types import message, InlineKeyboardButton, InlineKeyboardMarkup 

Alif=Client(
    "Pyrogram bot",
    bot_token="5277391090:AAGu1AdEbl7-txB077OMIUuA--fYaiqIBW4",
    api_id="18714739",
    api_hash="7795554afe9b45d359f28c5455c0b1e1"
)

@Alif.on_message(filters.command("start"))           
async def start_message(bot, message):
    await message.reply_text(
        text="start✅",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg")
            ]]
            )
         )




Alif.run()
