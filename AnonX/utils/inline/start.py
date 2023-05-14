from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴋᴏᴍᴜᴛʟᴀʀ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴋᴏᴍᴜᴛʟᴀʀ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❣ ᴅᴜʏᴜʀᴜ ❣", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 ʙᴏᴛ ꜱᴀʜɪʙɪ 🥀", user_id=OWNER
            )
        ],
     ]
    return buttons
