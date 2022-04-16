from pyrogram import Client, filters



@Client.on_message(filters.regex("hi") | filter.regex("Hi"))                     
async def regex(bot, msg):
    await msg.reply_text("""
Hi bro
""")
