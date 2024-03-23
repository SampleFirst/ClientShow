from pyrogram import Client, filters 
from info import LOG_CHANNEL


@Client.on_message(filters.group & filters.text & filters.incoming)
async def bot_filter(bot, message):
    if message.from_user.is_bot:
        if message.reply_markup is None:
            await bot.send_message(
                chat_id=LOG_CHANNEL, 
                text=message.text
            )
        else:
            await bot.send_message(
                chat_id=LOG_CHANNEL,
                text=f"⚡ {message.text}"
            )
            
