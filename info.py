import re
from os import environ
from Script import script
from dotenv import load_dotenv
load_dotenv()
from time import time

import re
import os
from os import environ
from pyrogram import enums
from Script import script

import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Log
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
login_channel = environ.get('LOGIN_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
LOGIN_CHANNEL = int(login_channel) if login_channel and id_pattern.search(login_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
chat_group = environ.get('CHAT_GROUP')
CHAT_GROUP = int(chat_group) if chat_group and id_pattern.search(chat_group) else None







# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
BOT_START_TIME = time()

PICS = (environ.get('PICS', 'https://telegra.ph/file/ac524f66eec140ec69db5.jpg https://telegra.ph/file/bd94ba94b8bd34793cc81.jpg https://telegra.ph/file/0fd19a01130a1dec30ee2.jpg https://telegra.ph/file/9e71045e92e89ecf0b1cd.jpg https://telegra.ph/file/f739b561482df0be0a644.jpg')).split()
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/f7f2a532fe4b990044507.mp4")
NOR_IMG = (environ.get('NOR_IMG', 'https://telegra.ph/file/8ab607a0ae37243d3e5eb.jpg https://telegra.ph/file/665820de1242714c1cb76.jpg https://telegra.ph/file/307a6c01601a8ef80b9bd.jpg https://telegra.ph/file/a416127d2fe5b6197da6c.jpg https://telegra.ph/file/ed9db200b03a691f303c8.jpg https://telegra.ph/file/4fe268a606d0d5f4a8d72.jpg https://telegra.ph/file/a7ea55f5e27e90f81a681.jpg https://telegra.ph/file/529d31175604a625fd1ae.jpg')).split()
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/732a9f89be5a9cd63289b.jpg")
CLOSE_IMG = (environ.get('CLOSE_IMG', 'https://telegra.ph/file/6e9dd701bac49632cf79a.jpg https://telegra.ph/file/998d2b84e1411ed5189e3.jpg https://telegra.ph/file/c199babd469011d07f139.jpg https://telegra.ph/file/31b6d3d2c70bbe52b5300.jpg https://telegra.ph/file/77744524fbb6305298d45.jpg https://telegra.ph/file/9d79d990674166a2a2364.jpg')).split()
SPELL_IMG = environ.get('SPELL_IMG',"https://telegra.ph/file/ab65e0a1b3e4bdf6d8d8f.jpg")
SP = (environ.get('SP', 'https://telegra.ph/file/db018384d5d139f3844ed.jpg https://telegra.ph/file/30c736c93b5ad5c328141.jpg https://telegra.ph/file/f1565e213ec1a45a27362.jpg https://telegra.ph/file/0c53da8c1598c63e50a6e.jpg https://telegra.ph/file/360d78cf3209429ca8e66.jpg')).split()
MELCOW_IMG = environ.get('MELCOW_IMG',"https://telegra.ph/file/ab65e0a1b3e4bdf6d8d8f.jpg")
MELCOW_VID = environ.get('MELCOW_VID',"")


# inline caption
INLINE_CAPTION = environ.get("INLINE_CAPTION", f"{script.INLINE_CAPTION}")


support_chat_id = environ.get('SUPPORT_CHAT_ID')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None


#VALUES
HRK_APP_NAME = environ.get('HRK_APP_NAME', 'mybots')
HRK_API = environ.get('HRK_API', '0')

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", False)
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'b4d510e7b1e56da54f43c9e27569ee0a281121db')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "False")), False)
S_GROUP = environ.get('S_GROUP',"https://t.me/nasrani_update")
BATCH_LINK = environ.get('BATCH_LINK',"https://t.me/nasrani_update")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://t.me/nasrani_update")
FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/bigmoviesworld")
MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
# FILE_CHANNEL = int(environ.get('FILE_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'DCENIMAS')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
BR_IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.BR_TEMPLATE_TXT}")

LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "tamil", "english", "hindi", "telugu", "kannada"]


# FILE_FORWARD = environ.get('FILE_FORWARD',"https://t.me/bigmoviesworld")
# MSG_ALRT = environ.get('MSG_ALRT', '𝑪𝑯𝑬𝑪𝑲 & 𝑻𝑹𝒀 𝑨𝑳𝑳 𝑴𝒀 𝑭𝑬𝑨𝑻𝑼𝑹𝑬𝑺')
# FILE_CHANNEL = int(environ.get('FILE_CHANNEL', -1001335744963))

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 180))
IMDB_DLT_TIME = int(environ.get('IMDB_DLT_TIME', 180))




# LOG_STR += (f"INLINE_CAPTION enabled with value {INLINE_CAPTION}, your files will be send along with this customized caption.\n" if INLINE_CAPTION else "No INLINE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
