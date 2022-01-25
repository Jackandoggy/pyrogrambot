form pyrogram import Client, filters 

Alif=Client(
    "Pyrogram bot",
    bot_token="5277391090:AAGu1AdEbl7-txB077OMIUuA--fYaiqIBW4",
    api_id="18714739",
    api_hash="7795554afe9b45d359f28c5455c0b1e1"
)



@Alif.on_massage(filters.command("start")) 
async def start_message(bot, message):
    wait message.reply_text("hi")  










Alif.run()
