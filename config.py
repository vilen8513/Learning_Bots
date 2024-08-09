import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("27766763"))
API_HASH = getenv("6663825288")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7303487163:AAEd2BRXoG1p9LbK5tcUINBObkXXmx1frHo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://vilen8513:vilen8513@cluster0.rhynj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002231236503", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6663825288))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("https://t.me/Heeramandi_GC", "https://t.me/FallenAssociation")
SUPPORT_CHAT = getenv("https://t.me/Heeramandi_GC", "https://t.me/DevilsHeavenMF")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQGnr-sAScQYaES6XCLerXc4jZ4K0F-drgBixpMbZ6qgdbSTWRRTrcENFabhMDH_piV4MuRE2X_azvE4uzg3wtOWqV5iHHvotWzXAwypVS6XicKCY5cGGhsrZw5dvL-_WsBfYITFHBfb4ZOTKKciE6LMEdWAhP7KHkC-ajlkXdDKtpzITyt6EJsG1PTUn86uZWJOtqIFZTVHqzxLn3zAzMW-rTzurTP9mhNcVOx-LYipFnXbZXt-AfTE2awpe-A-JBXQ7J-nRsGL461RM6GElRgXNhqykjLrlax4JH_EViCHHpnR4cxLaIqAQ1PxmXIMpXNXZ7WwRz0lfp_8cpBMzYFkWNZhaQAAAAGNMeeIAA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
STATS_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
STREAM_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/5659f7cb281dfefe6db1d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
