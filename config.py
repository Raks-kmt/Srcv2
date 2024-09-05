# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28526237"))
API_HASH = getenv("API_HASH", "936db76a74f9a52cfb2cea8a62e4c20e")
BOT_TOKEN = getenv("BOT_TOKEN", "7397842341:AAFIioQE_xJKcfoLVCMtUjf04_2ZT7SFpns")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6486192717").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://prisarax:WxuKANYzL5CPyY7d@cluster0.jxlwo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002204974717")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2204974717"))
