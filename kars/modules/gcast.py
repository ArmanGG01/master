import asyncio
import os

import heroku3
from requests import get
from telethon.errors import FloodWaitError

from rams import BLACKLIST_GCAST
from rams import CMD_HANDLER as cmd
from rams import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME
from rams.utils import edit_delete, edit_or_reply, ram_cmd as star
from rams.events import register as mek
while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/ramadhani892/Ramblack/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001692751821, -1001459812644]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""


@star(pattern="gcast(?: |$)(.*)")
@mek(pattern="^\.cgcast(?: |$)(.*)", sudo=True)
async def gcast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**KALO MALAS TYPING YA MINIMAL REPLY LAH NGENTOD**")
    kk = await edit_or_reply(event, "`Limit jangan Salahin Gua tot, Lagi gua kirim ni....`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@star(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**KALO MALAS TYPING YA MINIMAL REPLY YA NGENTOT**")
    kk = await edit_or_reply(event, "`Limit jangan salahin gua tot, Lagi gua kirim ni....`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{er}` **chat**"
    )


@star(pattern="blchat$")
async def sudo(event):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            event,
            f"🌟 **Blacklist GCAST:** `Enabled`\n\n✅ **Blacklist Group:**\n» {list}\n\nKetik `{cmd}addbl` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_delete(event, "🌟 **Blacklist GCAST:** `Disabled`")


@star(pattern="addbl(?:\\s|$)([\\s\\S]*)")
async def add(event):
    xxnx = await edit_or_reply(event, "`Sedang Memproses...`")
    var = "BLACKLIST_GCAST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{gc}` **ke daftar blacklist gcast.**\n\nSabar Ya ngentot, Gua lagi Restart dulu."
    )
    heroku_Config[var] = blacklistgrup


@star(pattern="delbl(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xxx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari daftar blacklist gcast.**\n\nSabar ngentot, Gua restart dulu bentar."
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await edit_delete(
            xxx, "**Grup ini tidak ada dalam daftar blacklist gcast.**", 10
        )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  •  **Syntax :** `{cmd}blchat`\
        \n  •  **Function : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n  •  **Syntax :** `{cmd}addbl`\
        \n  •  **Function : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  •  **Syntax :** `{cmd}delbl`\
        \n  •  **Function : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  •  **Note : **Ketik perintah** `{cmd}addbl` **dan** `{cmd}delbl` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
