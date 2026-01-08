# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton,WebAppInfo


class Data:
    info = """
<b>
├ https://t.me/bukananyadevass - KAISAR LANGIT
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
        [InlineKeyboardButton("FB OFC", url="https://hk777.top/FACEBOOKGRUPHOKI777"), InlineKeyboardButton("TELE OFC", url="https://hk777.top/TELEGRAMGRUPHOKI777")],
        [InlineKeyboardButton("WA OFC", url="https://wa.me/6282312622550"), InlineKeyboardButton("INFO GACOR", url="t.me/infogacorhoki777")],
        [InlineKeyboardButton("⭐️ APK HOKI777 ⭐️", web_app=WebAppInfo(url="https://hk777.top/HOKI777"))],
        [InlineKeyboardButton("⭐️ LOGIN HOKI777 ⭐️", url="t.me/infogacorhoki777")],
        [InlineKeyboardButton("TELE CREATOR", url="https://hk777.top/TELE-CREATOR-HOKI777"), InlineKeyboardButton("WA CREATOR", url="https://hk777.top/CREATOR-HOKI777")],
        [InlineKeyboardButton("LIVECHAT", url="https://secure.livechatinc.com/licence/19408592/v2/open_chat.cgi"), InlineKeyboardButton("RTP LIVE", url="https://hk777.top/RTP-Hoki777")],
        [InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]


    startbtn = [
        [InlineKeyboardButton("FB OFC", url="https://hk777.top/FACEBOOKGRUPHOKI777"), InlineKeyboardButton("TELE OFC", url="https://hk777.top/TELEGRAMGRUPHOKI777")],
        [InlineKeyboardButton("WA OFC", url="https://wa.me/6282312622550"), InlineKeyboardButton("INFO GACOR", url="t.me/infogacorhoki777")],
        [InlineKeyboardButton("⭐️ APK HOKI777 ⭐️", web_app=WebAppInfo(url="https://hk777.top/HOKI777"))],
        [InlineKeyboardButton("⭐️ LOGIN HOKI777 ⭐️", url="t.me/infogacorhoki777")],
        [InlineKeyboardButton("TELE CREATOR", url="https://hk777.top/TELE-CREATOR-HOKI777"), InlineKeyboardButton("WA CREATOR", url="https://hk777.top/CREATOR-HOKI777")],
        [InlineKeyboardButton("LIVECHAT", url="https://secure.livechatinc.com/licence/19408592/v2/open_chat.cgi"), InlineKeyboardButton("RTP LIVE", url="https://hk777.top/RTP-Hoki777")],
        [InlineKeyboardButton("❌ ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat di akses melalui Link Khusus.</b>
"""


