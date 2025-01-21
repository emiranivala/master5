# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25662550"))
API_HASH = getenv("API_HASH", "3d2663ae1493ece93fab45f83b659acc")
BOT_TOKEN = getenv("BOT_TOKEN", "6852093006:AAFDFDu_AhIQZWGGfsQ73LgL6KuPcM6lf_k")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1900466126").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Ramzy:Ramzy@cluster0.od4yk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001811301225")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001811301225"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
