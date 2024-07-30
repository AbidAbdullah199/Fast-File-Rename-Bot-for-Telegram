import os, time

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    

    # wes response configuration     
    PORT = int(os.environ.get("PORT", ""))
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} I'm Fast Telegram File Rename Bot Feel free to use me.

    ABOUT_TXT = """

<b>NAME</b> : {File Rename Fast}
<b>OWNER</b> : <a href=https://t.me/abidabdullah199>Click Here</a> 
<b>CHANNAL</b> : <a href=https://t.me/AnimeQuestX>Click Here</a>
<b>ONGOING ANIME</b> : <a href=https://t.me/OngoingAnimeQuest>Click Here</a>
<b>ANIME CHANNAL</b> : <a href=https://t.me/AnimeQuestX>Click Here</a>
<b>SUPPORT</b> : <a href=https://t.me/+r-x-wA4JT5gxZjVl>Click Here</a>
<b>GITHUB</b> : <a href=https://github.com/AbidAbdullah199>Click Here</a></b>     

"""

    HELP_TXT = """
<b><u>How To Set Thumbnail</u></b>
  
/start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
/del_thumb - Use This Command To Delete Your Old Thumbnail.
/view_thumb - Use This Command To View Your Current Thumbnail.

<b><u>How To Set Custom Caption</u></b>

/set_caption - Use This Command To Set A Custom Caption
/see_caption - Use This Command To View Your Custom Caption
/del_caption - Use This Command To Delete Your Custom Caption
Example - <code>/set_caption Name ➠ : {filename}

"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
┣⪼ 🥺 Join: @AnimeQuestX
╰━━━━━━━━━━━━━━━➣ </b>"""

    DONATE_TXT = """
<b>Donate Your Supports! ❤️</b>
"""