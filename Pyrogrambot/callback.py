from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client as Alif, filters



@Alif.on_callback_query()
async def callback (bot, mmt : CallbackQuery):
    if mmt.data == "hi":  
        await mmt.message.edit(  
            text="hi bro"
        )
     
    elif mmt.data == "help":


          reply1 = await mmt.message.edit("⬛")
          reply2 = await reply1.edit("⬛⬛")
          reply3 = await reply2.edit("⬛⬛⬛")
          await reply3.edit( 
            text="""Here my help menu
/id to get id
/video to get video
/sticker to get stickers
""",
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("hi" , callback_data = "hi")
               ]]
           )

     )
    elif mmt.data == "close":
        await mmt.message.delete()


    elif mmt.data == "khang":
        await mmt.answer("Please don't khang the code", show_alert=True)
