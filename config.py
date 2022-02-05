import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCnwRYowhgqMeAIDlfjSw0oduXvOKCKtSgUnsH3379Js4bnJalNaSAGAMttocWFjHzBz-g9G0wiTqkVRy3kb3BKktjV77EZ4Gj-2djwjhd0_jpkSKkGBl8QBZFLynhPt0pzV4_prO3c5_tvoY-fC8qTuhcrrzFRRqejxef-Jc1et3J1JLGvqQC0USRhNw68G9HUBOSDCe-G6jvFCbFDW1oIZsHbqg7IS0a0wzLmTYyj-QLcj1t5FJfpkD7MqOV9qL0ItJuBe-PK11TMlx-w8Qo_WpBK1sV81pbT1by5SHx4C8r-2kXXeaBZ488FM8A8PNie4PiykBHN8O3WOSIB-J-4AAAAAG5FPdUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5100828011:AAHLCCJH9B7moCnnM2yzehI3d_o431FdFxg")
BOT_NAME = getenv("BOT_NAME", "CNC Stream Bot")
API_ID = int(getenv("API_ID", "19718359"))
API_HASH = getenv("API_HASH", "03ee4693069d9cf8bc740c70631be024")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://hmm:astromanager@cluster0.jfstx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "dilshaner")
ALIVE_NAME = getenv("ALIVE_NAME", "CNC")
BOT_USERNAME = getenv("BOT_USERNAME", "CryptonitestreamBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "CNCstream")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "cryptonite_club")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CryptoNite_News")
SUDO_USERS = list(map(int, getenv("962844567 1450779437").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("https://github.com/CNCStream/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
