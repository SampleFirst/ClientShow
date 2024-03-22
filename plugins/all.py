from pyrogram import Client, filters
from info import AUTH_CHANNEL


# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.group & filters.text & filters.incoming)
async def forward_message(client, message):
    content = message.text
    await client.send_message(
        chat_id=AUTH_CHANNEL, 
        text=message.text
    )

