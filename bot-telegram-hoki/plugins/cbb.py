from bot import Bot
from config import OWNER
from Data import Data
from pyrogram import filters
from pyrogram.errors import MessageNotModified, MessageIdInvalid
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message
from random import choice
from time import gmtime, strftime, time
from config import START_MSG

import os


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass