import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "hama")
ALIVE_NAME = getenv("ALIVE_NAME", "hama")
BOT_USERNAME = getenv("BOT_USERNAME", "DsssxnnBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Slt55")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "wtan778")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "soltansh1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8e3620165ec9b1e1569fe.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/slt99/alazizy")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/8e3620165ec9b1e1569fe.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/8e3620165ec9b1e1569fe.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/8e3620165ec9b1e1569fe.jpg")
