from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client as Alif, filters



@Alif.on_callback_query()
async def callback (bot, mmt : CallbackQuery):
    if mmt.data == "mm":  
        await mmt.message.edit(  
            text="hi bro"
        )
     
    elif mmt.data == "help":
        reply1 = await mmt.message.edit("○○○")
        reply2 = await reply1.edit("●○○")
        reply3 = await reply2.edit("●●○")
        await reply3.edit("●●●")
            text="""Here my help menu
/id to get id
/video to get video
/sticker to get stickers
""",
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("😃" , callback_data = "mm")
               ]]
           )
        )


    elif mmt.data == "close":
        await mmt.message.delete()


    elif mmt.data == "hi":
        await mmt.answer("𝖸𝗈𝗎 𝖺𝗋𝖾 𝗂𝗇 𝗆𝗒 𝗌𝖾𝖼𝗈𝗇𝖽 𝗉𝖺𝗀𝖾.", show_alert=True)
