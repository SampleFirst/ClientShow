from pyrogram import Client, filters

# Define the source group and target channel IDs
source_group_id = -1001932992146  # Replace with the source group ID
target_channel_id = -1001726137386  # Replace with the target channel ID

# Define the function to forward messages from bots in the source group to the target channel
@Client.on_message(filters.chat(source_group_id) & filters.text & filters.bot)
async def forward_bots(client, message):
    content = message.text
    try:
        await client.send_message(
            chat_id=target_channel_id, 
            text=content
        )
    except Exception as e:
        print(f"An error occurred while forwarding message: {e}")
