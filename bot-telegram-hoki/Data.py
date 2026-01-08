# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton,WebAppInfo


class Data:
    info = """
<b>
├ https://t.me/anyadevass - Anya Deva
├ https://t.me/Natasha_cantiq - Natasha Cantiq
├ https://t.me/brekeyle - Cakwe
</b>
    """
#     HELP = """
# <b> ❏ Perintah untuk Pengguna BOT
#  ├ /start - Mulai Bot
#  ├ /about - Tentang Bot ini
#  ├ /help - Bantuan Perintah Bot ini
#  ├ /ping - Untuk mengecek bot hidup 
 
#  ❏ Perintah Untuk Admin BOT
#  ├ /logs - Untuk melihat logs bot
#  ├ /setvar - Untuk mengatur var dengan command dibot
#  ├ /delvar - Untuk menghapus var dengan command dibot
#  ├ /getvar - Untuk melihat salah satu var dengan command dibot
#  ├ /users - Untuk melihat statistik pengguna bot
#  ├ /batch - Untuk membuat link lebih dari satu file
#  └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot</b>
# """
    HELP = """ 

"""

    close = [[InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")]]

    mbuttons = [
        [InlineKeyboardButton("⬅️ BACK", callback_data="back1"), InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]

    buttons = [
        [InlineKeyboardButton("🎰 INFO GACOR", url="https://t.me/+5_EzmCP-ysc5ZDc1"), InlineKeyboardButton("🎖 PROMO", url="https://yk69.top/YUK69")],
        [InlineKeyboardButton("💣 BOT INFO", callback_data="infb"), InlineKeyboardButton("❤️ OWNER", callback_data="ownDt")],
        [InlineKeyboardButton("📚 ABOUT ME", callback_data="about"), InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")],
        [InlineKeyboardButton("⬅️ BACK", callback_data="back")],
    ]


    startbtn = [
        [InlineKeyboardButton("🌍 DAFTAR YUK69",url="https://vip.livechatyuk69.net/register"), InlineKeyboardButton("🔒DOWNLOAD APK", web_app=WebAppInfo(url="https://drive.google.com/uc?export=download&id=1x83J4LIPd9COClmkE0Lp5D4tHOec9zN9"))],
        [InlineKeyboardButton("💣 INFO GACOR", url="https://t.me/infogacorhoki777"), InlineKeyboardButton("✅ KLAIM BONUS ", url="https://tawk.to/yuk69berkah")],
        [InlineKeyboardButton("📚 BOCORAN LIVE", url="https://es.rtpyk-69.autos"), InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat di akses melalui Link Khusus.</b>
"""
