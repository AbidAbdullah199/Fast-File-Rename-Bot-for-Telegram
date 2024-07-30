import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # fill up ids
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # extra
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    PORT = int(os.environ.get("PORT", ""))
    
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
        
    START_TXT = """Hᴇʟʟᴏ {} 
I ᴀᴍ Nɪᴄᴏ Rᴏʙɪɴ
I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇ Wɪᴛʜ Pᴀʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Mᴀᴋᴇ Oᴜᴛᴘᴜᴛ Wɪᴛʜ Yᴏᴜʀ Dᴇsɪʀᴇᴅ Fᴏʀᴍᴀᴛ Tʀʏ Tᴏ Usᴇ Mᴇ Oʀ Sᴇɴᴅ /ʜᴇʟᴘ Fᴏʀ Mᴏʀᴇ Assɪsᴛᴇɴᴛs.
"""
    
    FILE_NAME_TXT = """<b><u>robinrenamebot</u></b>

    
    ABOUT_TXT = f"""
<b>Channal :</b> <a href='https://t.me/AnimeQuestX'>Join Now</a>
<b>Hindi :</b> <a href='https://t.me/AnimeQuestHindi'>Join Now</a>
<b>Ongoing Channal :</b> <a href='https://t.me/OngoingAnimeQuest'>Join Now</a>
<b>Discussion Channal:</b> <a href='https://t.me/+r-x-wA4JT5gxZjVl'>Join Now</a>
<b>Oᴡɴᴇʀ :</b> <a href='https://t.me/abidabdullah199'>Monkey D Luffy</a>
"""

    
    THUMBNAIL_TXT = """<b><u>  Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ</u></b>
    
You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
/viewthumb - Use This Command To See Your Thumbnail
/delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>  Hᴏᴡ Tᴏ Sᴇᴛ Cᴀᴘᴛɪᴏɴ</u></b>
    
/set_caption - Use This Command To Set Your Caption
/see_caption - Use This Command To See Your Caption
/del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣ 🗃️ Sɪᴢᴇ: {1} | {2}
┣ ⏳️ Dᴏɴᴇ : {0}%
┣ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣ ⏰️ Eᴛᴀ: {4}
┣ 🥺 Join: @AnimeQuestX
╰━━━━━━━━━━━━━━━ </b>"""
    
    
    DONATE_TXT = """<b>Donate Me Your Support❤️</b>
    
 """
    
    HELP_TXT = """Inbox If You Have Business @abidabdullah199 """

