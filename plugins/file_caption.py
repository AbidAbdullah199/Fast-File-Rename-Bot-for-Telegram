from pyrogram import Client, filters 
from helper.database import AbidAbdullah199

@Client.on_message(filters.private & filters.command(['set_caption', "sc"]))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Sᴇɴᴅ Cᴀᴘᴛɪᴏɴs\n\nCᴀᴘᴛɪᴏɴ Vᴀʀɪᴀʙʟᴇs :- `/set_caption Fᴏʀ Fɪʟᴇ Nᴀᴍᴇ - : {filename} \n\nFɪʟᴇ Sɪᴢᴇ - : {filesize} \n\nDᴜʀᴀᴛɪᴏɴ - : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await AbidAbdullah199.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Sᴜᴄᴄᴇsғᴜʟʟʏ Aᴅᴅᴇᴅ**")
   
@Client.on_message(filters.private & filters.command(['del_caption', "dc"]))
async def delete_caption(client, message):
    caption = await AbidAbdullah199.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**Yᴏᴜ Dɪᴅɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ**")
    await AbidAbdullah199.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Is Dᴇʟᴇᴛᴇᴅ**")
                                       
@Client.on_message(filters.private & filters.command(['see_caption', 'view_caption', "vc"]))
async def see_caption(client, message):
    caption = await AbidAbdullah199.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Cᴀᴘᴛɪᴏɴ :**\n\n`{caption}`")
    else:
       await message.reply_text("**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Cᴀᴘᴛɪᴏɴ**")

