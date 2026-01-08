import asyncio
from datetime import datetime
from time import time
from bot import Bot

from config import (
    ADMINS,
    CUSTOM_CAPTION,
    FORCE_MSG,
    PROTECT_CONTENT,
    START_MSG,
    LOGGER,
)
from database.sql import add_user, delete_user, full_userbase, query_msg
from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from pyrogram.types import Message, InlineKeyboardMarkup
from helper_func import decode, get_messages
from Data import Data


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60**2 * 24),
    ("hour", 60**2),
    ("min", 60),
    ("sec", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)

from pyrogram import Client

@Client.on_message(filters.command("start"))
async def not_joined(client: Client, message: Message):
    try:
        await message.reply(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f"@{message.from_user.username}" if message.from_user.username else None,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(Data.startbtn),
            quote=True,
            disable_web_page_preview=True,
        )
    except:
        pass