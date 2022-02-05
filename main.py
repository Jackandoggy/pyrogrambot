from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message 

Alif=Client(
    "Pyrogram bot",
    bot_token="5277391090:AAGL8d4ZkZKVPXZ9iCFN3wkFeYYfKhVq8-Q",
    api_id="18714739",
    api_hash="7795554afe9b45d359f28c5455c0b1e1"
)

@Alif.on_message(filters.command("start"))           
async def start_message(bot, message):
    await message.reply_text(
        text="start✅ https://t.me/UltroidSupport",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝗱𝗲𝘃", url="https://t.me/Alifmuhammed_tg")
            ]]
            )
         )




Alif.run()
