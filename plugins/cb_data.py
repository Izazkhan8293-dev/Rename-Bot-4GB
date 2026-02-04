from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.progress import progress_for_pyrogram
from config import *
import os
import asyncio
import time

# ----------- Session-Based Client -----------
app = Client(
    name="my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins=dict(root="plugins")
)

# ----------- /start Command -----------
@app.on_message(filters.private & filters.command("start"))
async def start(bot: Client, message: Message):
    await message.reply_text(
        text="👋 Hello! I am your Rename Bot using session.\n\nSend me a file to rename.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Channel", url="https://t.me/JishuBotz")]]
        ),
    )

# ----------- Cancel Callback -----------
@app.on_callback_query(filters.regex("cancel"))
async def cancel(bot: Client, update):
    await update.message.edit("❌ Operation Cancelled!")

# ----------- /rename Handler -----------
@app.on_message(filters.private & filters.document)
async def rename_file(bot: Client, message: Message):
    # Ask user for new file name
    m = await message.reply_text("✏️ Send me the new file name (with extension):")

    # Wait for user's reply
    try:
        response = await bot.listen(message.chat.id, timeout=60)  # wait 60 seconds
    except asyncio.TimeoutError:
        return await m.edit("⏰ Timeout! You took too long to send the new name.")

    new_file_name = response.text.strip()
    await m.edit("⚡ Downloading file...")

    # Download file
    start_time = time.time()
    file_path = await bot.download_media(
        message,
        file_name=new_file_name,
        progress=progress_for_pyrogram,
        progress_args=("Downloading...", m, start_time)
    )

    # Send back renamed file
    await m.edit("⚡ Uploading file...")
    await bot.send_document(
        chat_id=message.chat.id,
        document=file_path,
        caption=f"✅ Renamed to `{new_file_name}`",
        progress=progress_for_pyrogram,
        progress_args=("Uploading...", m, start_time)
    )

    # Clean up
    try:
        os.remove(file_path)
    except:
        pass

    await m.delete()
