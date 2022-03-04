# ©tofik_dn
# Minta tipis tipis

import random

from userbot import CMD_HELP
from userbot.events import register
from userbot import DEFAULTUSER
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(outgoing=True, pattern=r"^\.vbkp$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@randomasupanhe", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"YAHAHA SANGEAN, NIH ASUPANNYA JING [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Kurang beruntung ya, Padahal mau coli.")

@register(outgoing=True, pattern=r"^\.dcewe$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"CROTTTT!!! NIH VN DESAH CEWE [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`Yah Kurang beruntung lu bang...`")


@register(outgoing=True, pattern=r"^\.dcowo$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowo", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"CROTTTT!!! NIH VN DESAH COWO [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("`Yah Kurang Beruntung lu neng...`")

        
@register(outgoing=True, pattern=r"^\.ayg$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Ayang Aku 😘 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gada Yang Mau Sama Lo Karena Lo Dekil kaya baju partai bekasan🤭.")


CMD_HELP.update(
    {
        "asupan": "**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `.vbkp`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `.dcowo` `.dcewe`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
        \n\n  •  **Syntax :** `.ayg`\
        \n  •  **Function : **Untuk Mencari ayang buat cowok yang jomblo.\
    "
    }
)
