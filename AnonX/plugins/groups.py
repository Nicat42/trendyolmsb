from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AnonX import app, Telegram
from AnonX.misc import SUDOERS
from AnonX.utils.database import get_served_chats


@app.on_message(filters.command(["groups", "chatlist"]) & SUDOERS)
async def serv_chats(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ʟɪsᴛ...")
    text = "<b>» ʟɪsᴛ ᴏғ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs :</b>\n\n"
    j = 0
    chats = []
    for chat in await get_served_chats():
        chats.append(int(chat["chat_id"]))

    for x in chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
            await asyncio.sleep(0.5)
        except FloodWait as fw:
            flood_time = int(fw.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except:
            continue

        await Telegram.send_split_text(message, text)
