# from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton as IKB
from pyrogram.types import InlineKeyboardMarkup as IKM


class ButtonMaker:
    def __init__(self):
        self.__button = []
        self.__header_button = []
        self.__footer_button = []

    def ubutton(self, key, link, position=None):
        if not position:
            self.__button.append(IKB(text=key, url=link))
        elif position == "header":
            self.__header_button.append(IKB(text=key, url=link))
        elif position == "footer":
            self.__footer_button.append(IKB(text=key, url=link))

    def ibutton(self, key, data, position=None):
        if not position:
            self.__button.append(IKB(text=key, callback_data=data))
        elif position == "header":
            self.__header_button.append(IKB(text=key, callback_data=data))
        elif position == "footer":
            self.__footer_button.append(IKB(text=key, callback_data=data))

    def build_menu(self, b_cols=1, h_cols=8, f_cols=8):
        menu = [self.__button[i : i + b_cols] for i in range(0, len(self.__button), b_cols)]
        if self.__header_button:
            h_cnt = len(self.__header_button)
            if h_cnt > h_cols:
                header_buttons = [self.__header_button[i : i + h_cols] for i in range(0, len(self.__header_button), h_cols)]
                menu = header_buttons + menu
            else:
                menu.insert(0, self.__header_button)
        if self.__footer_button:
            if len(self.__footer_button) > f_cols:
                [menu.append(self.__footer_button[i : i + f_cols]) for i in range(0, len(self.__footer_button), f_cols)]
            else:
                menu.append(self.__footer_button)
        return IKM(menu)


# def start_button(client):
#     if not FORCE_SUB_CHANNEL[0] and not FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         buttons.ibutton("🔍 INFO", "help")
#         buttons.ibutton("❌ TUTUP", "close")
#         buttons.ibutton("▶️ PLAY", "aplay", position="footer")
#         return buttons.build_menu(1)
        
#     if not FORCE_SUB_CHANNEL[0] and FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         gno = 0
#         for g in client.ilink_gc:
#             gno += 1
#             buttons.ubutton(f"🔵 Join Group {gno}", g)
#         buttons.ibutton("🔍 INFO", "help", position="footer")
#         buttons.ibutton("❌ TUTUP", "close", position="footer")
#         buttons.ibutton("▶️ PLAY", "aplay")
#         return buttons.build_menu(2)
        
#     if FORCE_SUB_CHANNEL[0] and not FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         cno = 0
#         for c in client.ilink_ch:
#             cno += 1
#             buttons.ubutton(f"🔵 Join Channel {cno}", c)
#         buttons.ibutton("🔍 INFO", "help", position="footer")
#         buttons.ibutton("❌ TUTUP", "close", position="footer")
#         buttons.ibutton("▶️ PLAY", "aplay")
#         return buttons.build_menu(2)
        
#     if FORCE_SUB_CHANNEL[0] and FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         cno = gno = 0
#         for c in client.ilink_ch:
#             cno += 1
#             buttons.ubutton(f"🔵 Join beb!", c)
#         for g in client.ilink_gc:
#             gno += 1
#             buttons.ubutton(f"🔵 Join beb!", g)
#         buttons.ibutton("🔍 INFO", "help", position="footer")
#         buttons.ibutton("❌ TUTUP", "close", position="footer")
#         buttons.ibutton("▶️ PLAY", "aplay")
#         return buttons.build_menu(2)


# def fsub_button(client, message):
#     if not FORCE_SUB_CHANNEL[0] and FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         gno = 0
#         for g in client.ilink_gc:
#             gno += 1
#             buttons.ubutton(f"🔵 Join Group {gno}", g)
#         try:
#             buttons.ibutton("❗️COBA LAGI❗️", "colag", position="footer")
#         except IndexError:
#             pass
#         return buttons.build_menu(2)
        
#     if FORCE_SUB_CHANNEL[0] and not FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         cno = 0
#         for c in client.ilink_ch:
#             cno += 1
#             buttons.ubutton(f"🔵 Join Channel {cno}", c)
#         try:
#             buttons.ibutton("❗️COBA LAGI❗️", "colag", position="footer")
#         except IndexError:
#             pass
#         return buttons.build_menu(2)
        
#     if FORCE_SUB_CHANNEL[0] and FORCE_SUB_GROUP[0]:
#         buttons = ButtonMaker()
#         cno = gno = 0
#         for c in client.ilink_ch:
#             cno += 1
#             buttons.ubutton(f"🔵 Join Channel {cno}", c)
#         for g in client.ilink_gc:
#             gno += 1
#             buttons.ubutton(f"🔵 Join Group {gno}", g)
#         try:
#             buttons.ibutton("❗️COBA LAGI❗️", "colag", position="footer")
#         except IndexError:
#             pass
#         return buttons.build_menu(2)
