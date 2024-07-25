import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import AbidAbdullah199
from config import Config, Txt  
  

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await AbidAbdullah199.add_user(client, message)                
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton('○ Aɴɪᴍᴇ Cʜᴀɴɴᴀʟ', url='https://t.me/AnimeQuestX'),
        InlineKeyboardButton('○ Aɴɪᴍᴇ Hɪɴᴅɪ', url='https://t.me/AnimeQuestHindi')],
        [InlineKeyboardButton('○ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('○ Hᴇʟᴘ', callback_data='help')],
        [InlineKeyboardButton("○ Oᴡɴᴇʀ", url='https://t.me/abidabdullah199')]
    ])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton('○ Aɴɪᴍᴇ Cʜᴀɴɴᴀʟ', url='https://t.me/AnimeQuestX'),
                InlineKeyboardButton('○ Aɴɪᴍᴇ Cʜᴀɴɴᴀʟ Hɪɴᴅɪ', url='https://t.me/AnimeQuestHindi')],
                [InlineKeyboardButton('○ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('○ Hᴇʟᴘ', callback_data='help')],
                [InlineKeyboardButton("○ Oᴡɴᴇʀ", url='https://t.me/abidabdullah199')]
            ])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Mᴀɪɴ Cʜᴀɴɴᴀʟ", url="https://t.me/AnimeQuestX")],
                [InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")]
            ])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Mᴀɪɴ Cʜᴀɴɴᴀʟ", url="https://t.me/AnimeQuestX")],
                [InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")]
            ])            
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()





@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
	text = Txt.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("FAQ",url = "https://t.me/abidabdullah199"), 
        			InlineKeyboardButton("Cʟᴏsᴇ",callback_data = "close") ]])
	await message.reply_text(text = text,reply_markup = keybord)


