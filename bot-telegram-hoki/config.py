import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from requests import get
from distutils.util import strtobool

ENV_URL = os.environ.get("ENV_URL", "")
if ENV_URL:
    try:
        res = get(ENV_URL)
        if res.status_code == 200:
            with open("config.env", "wb+") as f:
                f.write(res.content)
        else:
            logging.error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        logging.error(f"ENV_URL: {e}")

load_dotenv("config.env")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
# db_channel = int(os.environ.get("CHANNEL_ID", ""))
# CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER = os.environ.get("OWNER", "")

# FORCE_SUB_CHANNEL = [int(a) for a in os.environ.get("FORCE_SUB_CHANNEL", 0).split()]
# FORCE_SUB_GROUP = [int(a) for a in os.environ.get("FORCE_SUB_GROUP", 0).split()]

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "100"))

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)


# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
# DISABLE_CHANNEL_BUTTON = bool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", 0).split()]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

logging.basicConfig(
    format="[%(levelname)s] - [%(asctime)s - %(name)s - %(message)s] -> [%(module)s:%(lineno)d]",
    handlers=[
        RotatingFileHandler("log.txt", mode="w+", maxBytes=5242880, backupCount=1),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.ERROR)
LOGGER = logging.getLogger("tgfs")

PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello kak {first} ^^\n\nSelamat datang di Hoki777.\n\nNikmati sensasi bermain dengan permainan paling lengkap terfavorit bagi para bettor dari salah satu situs terbaik di Asia Tenggara.\n\n\nUntuk daftar dan dapat info terbaru atau klaim promo bisa menggunakan tombol dibawah ini. Salam Jackpot Mania ^^.</b>",
)

