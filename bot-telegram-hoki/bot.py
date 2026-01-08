import asyncio
from pyrogram import Client, filters, idle  # 👈 idle ditambahkan di sini!
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait

from config import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
    OWNER,
    ADMINS,
)

class Bot(Client):
    def __init__(self):
        bot_id = int(TG_BOT_TOKEN.split(":", 1)[0])
        super().__init__(
            name=f"tgfs_{bot_id}",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER.info(f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——")
        except FloodWait as f:
            self.LOGGER.info(f"Kena FloodWait jir: {f.value}s")
            await asyncio.sleep(f.value)
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
        except Exception as a:
            raise ValueError(a)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot stopped.")

    def run(self):
        """Jalankan bot secara async"""
        try:
            self.loop.run_until_complete(self.start())
            idle()  # 👈 ini bukan self.idle(), tapi fungsi idle() dari pyrogram
        except KeyboardInterrupt:
            self.LOGGER.info("Bot dihentikan oleh user.")
        finally:
            self.loop.run_until_complete(self.stop())