import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KK_Updates")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH","")
BOT_USERNAME = getenv("BOT_USERNAME", "")
SUPPORT = getenv("SUPPORT", "kk_kovilakam")
OWNER_ID = int(getenv("OWNER_ID", "5423253221"))




