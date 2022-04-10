# from RAM-UBOT <@merhdni/>

import random

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import ram_cmd
from userbot import owner
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterMusic

@ram_cmd(pattern=r"ayg$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Silahkan menikmati [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await event.delete()
    except Exception:
        await event.edit("Kalo Gak bisa, Ya jangan nangis tod")

@ram_cmd(pattern=r"dcewe$")
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
            caption=f"Silahkan menikmati tot! [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await event.delete()
    except Exception:
        await event.edit("`Yah Kurang beruntung lu bang...`")


@ram_cmd(pattern=r"dcowo$")
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
            caption=f"Silahkan Menikmati [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await event.delete()
    except Exception:
        await event.edit("`Yah Kurang Beruntung lu neng...`")


@ram_cmd(pattern=r"alq$")
async def _(event):
    try:
        qurannya = [
            quran
            async for quran in event.client.iter_messages(
                "@kureenkeryam", filter=InputMessagesFilterMusic
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(qurannya),
            caption=f"Dengarkan Dengan Khusyu [{owner}](tg://user?id={aing.id})",
           reply_to=event.reply_to_msg_id)
        await event.delete()
    except Exception:
        await event.edit(f"`Kalo Ga bisa, Jangan nangis ya {owner}`")


@ram_cmd(pattern=r"sholawat$")
async def _(event):
    try:
        sholawatnya = [
            quran
            async for quran in event.client.iter_messages(
                "@pengagum_sholawat", filter=InputMessagesFilterMusic
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sholawatnya),
            caption=f"Dengerin tuh Sholawat Biar adem [{owner}](tg://user?id={aing.id})",
           reply_to=event.reply_to_msg_id)
        await event.delete()
    except Exception:
        await event.edit(f"`Kalo Gabisa Ya jangan nangis lah {owner}.`")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}ayg`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
        \n\n  •  **Syntax :** `{cmd}dcowo` or  `{cmd}dcewe`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
    "
    }
)
