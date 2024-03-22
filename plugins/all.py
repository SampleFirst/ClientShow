from pyrogram import Client, filters
import re

SOURCE_USER_ID = 6317295439
SOURCE_CHAT_ID = -1001932992146
TARGET_CHAT_ID = [-1001726137386, -1001870457773]

# Function to check if a message contains any URLs
def contains_url(text):
    # Regular expression to match URLs
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.search(url_regex, text) is not None


# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.chat(SOURCE_CHAT_ID) & filters.user(SOURCE_USER_ID) & ~filters.forwarded)
async def forward_message(client, message):
    if message.text and contains_url(message.text):
        for chat_id in TARGET_CHAT_ID:
            await client.send_message(
                chat_id=chat_id, 
                text=message.text
            )

