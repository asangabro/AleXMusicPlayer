from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵 i [AleXa OweNs](https://t.me/asanga_bot) Project..

I can play music in your group's voice call. Developed by [Asanga Udara](https://t.me/Ausanga_Udara).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "My Owner", url="https://t.me/Ausanga_Udara")
                  ],


                  [
                    InlineKeyboardButton(
                        "💬 Help", url="https://telegra.ph/AleXa-Group-Music-Player-Helper-05-26"
                    )
                   
                ],
                [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Asanga_Udara_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/Ausanga_Udara")
                ]
            ]
        )
   )


