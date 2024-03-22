from pyrogram import Client, filters
import re

SOURCE_USER = "ekconverter9bot"
SOURCE_CHAT_ID = -1001932992146
TARGET_CHAT_IDS = [-1001726137386, -1001870457773]

# Function to check if a message contains any URLs
def contains_url(text):
    # Regular expression to match URLs
    url_regex = r"(https)"
    return re.search(url_regex, text) is not None


# Forward messages from the specific user if they contain URLs to the target chats
@Client.on_message(filters.group & filters.text & filters.incoming))
async def forward_message(client, message):
    if message.chat.id != SOURCE_CHAT_ID:
        content = message.text
        if contains_url(content):
            user = message.from_user.username 
            if user == SOURCE_USER:
                for chat_id in TARGET_CHAT_IDS:
                    await client.send_message(
                        chat_id=chat_id, 
                        text=message.text
                    )

