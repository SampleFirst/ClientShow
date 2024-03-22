from pyrogram import Client, filters
import re
from info import AUTH_CHANNEL, SOURCE_USER


# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.group & filters.text & filters.incoming)
async def forward_message(client, message):
    content = message.text
    user = message.from_user.username 
    if user == SOURCE_USER:
        await client.send_message(
            chat_id=AUTH_CHANNEL, 
            text=message.text
        )

