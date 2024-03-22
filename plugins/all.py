from pyrogram import Client, filters
import re

# Define the user ID of the specific user whose messages you want to forward
specific_user_id = "6317295439"

# Define the target chats where you want to forward the messages
target_chats = ["-1001726137386", "-1001870457773"]

# Function to check if a message contains any URLs
def contains_url(text):
    # Regular expression to match URLs
    url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.search(url_regex, text) is not None

# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.user(specific_user_id) & ~filters.forwarded)
async def forward_message(client, message):
    if contains_url(message.text):
        for chat_id in target_chats:
            await client.forward_messages(
                chat_id=chat_id, 
                from_chat_id=message.chat.id, 
                message_ids=message.message_id
            )

