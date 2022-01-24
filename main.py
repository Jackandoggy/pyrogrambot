form pyrogram import Client, filters 





Alif=Client(
    "Pyrogram bot",
    bot_token="bot token",
    api_id="api id",
    api_hash="api hash"
)



@Alif.on_massage(filters.command("start")) 
async def start_message(bot
