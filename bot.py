from plugins.cb_data import app as Client2
from config import *
import pyromod
import pyrogram.utils
import asyncio
from pyrogram import Client, idle

pyrogram.utils.MIN_CHAT_ID =-1001685382274
pyrogram.utils.MIN_CHANNEL_ID = -1001685382274
 
import asyncio

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():
    await app.start()
    print("Bot started")
    await idle()
    await app.stop()



if __name__ == "__main__":
    asyncio.run(main())














# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Back-Up Channel @JishuBotz
# Developer @JishuDeveloper
