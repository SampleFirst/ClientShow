from pyrogram import Client
from pyrogram.types import Message


def auto_forward_buttons(client: Client, message: Message, source_chat: str, target_chats: list):
    if message.chat.id == source_chat and message.reply_markup:
        for chat_id in target_chats:
            client.forward_messages(chat_id=chat_id, from_chat_id=message.chat.id, message_ids=message.message_id)


@Client.on_message()
def handle_message(client, message):
    auto_forward_buttons(client, message, "-1001932992146", ["-1001726137386", "-1001870457773"])


