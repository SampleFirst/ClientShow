from pyrogram import Client, filters 
from info import LOG_CHANNEL 

@Client.on_message(filters.group)
async def forward_bots(client, message):
    if message.from_user.is_bot:
        await client.forward_messages(LOG_CHANNEL, message.chat.id, message.message_id)

