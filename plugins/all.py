from pyrogram import Client, filters
from info import *

# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.group & filters.text & filters.incoming)
async def forward_message(bot, message):
    content = message.text
    user = message.from_user.mention
    if user == SOURCE_USER:
        if message.reply_markup is None:
            await bot.send_message(
                chat_id=AUTH_CHANNEL, 
                text=message.text
            )
        else:
            await bot.send_message(
                chat_id=AUTH_CHANNEL,
                text=f"⚡ {message.text}"
            )
    
