from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Gizli Sohbet"
        logger_text = f"""
**{MUSIC_BOT_NAME} ŞARKI KAYDEDİCİSİ**

**GRUP İSMİ:** {message.chat.title} [`{message.chat.id}`]
**İSTEYEN:** {message.from_user.mention}
**KULLANICI ADI:** @{message.from_user.username}
**ɪᴅ:** {message.from_user.id}
**ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

**çALAN PARÇA:** {message.text}

**ÇALAN KANAL:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
