from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from YaeRobot import pbot as client


ANON = "https://telegra.ph/file/9e9e1112a16894e7998cf.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**Hey​ {message.from_user.mention()},\n\nI Am [Saber Sword](t.me/YaeRobot)**

**» My Devloper​ :** [U N K N O W N](tg://user?id=5531584953)
**» Python Version :** `{y()}`
**» Library Version :** `{o}` 
**» Telethon Version :** `{s}` 
**» Pyrogram Version :** `{z}`

**You Can Buy This Bot's Private Repo At The Buttons Below**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/XtheANonymous"), 
                    InlineKeyboardButton(
                        "Source", url="https://t.me/Xultim8")
                ]
            ]
        )
    )

__mod_name__ = "Repo/Source"
