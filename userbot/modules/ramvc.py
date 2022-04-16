from pytgcalls.exceptions import AlreadyJoinedError as memek
from pytgcalls.types.input_stream import (
    InputAudioStream as bego,
    InputStream as ngentot,
)
from pytgcalls import StreamType as kontol
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import GetGroupCallRequest as getvc

from userbot.events import register as ok
from userbot.utils import edit_delete, edit_or_reply, ram_cmd as tod
from userbot import call_py as sayang
from .ramcals import vcmention as toyik


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call

eor = edit_or_reply
ede = edit_delete

# credits by @vckyaz < vicky \>
# recode by @lahsiajg < starboy \>

@tod(pattern="jvc(?: |$)(.*)")
@ok(pattern=r"^\.cjvc(?: |$)(.*)", sudo=True)
async def join_(event):
    rambot = await eor(event, "**Hoiii, Aku datang...**")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await ede(rambot, f"**ERROR:** `{e}`", 5)
    else:
        chat_id = event.chat_id
        from_user = toyik(event.sender)
    if chat_id:
        file = "./userbot/resource/SEPI.mp3"
        try:
            await sayang.join_group_call(
                chat_id,
                ngentot(
                    bego(
                        file,
                    ),
                ),
                stream_type=kontol().local_stream,
            )
            await ede(rambot,
                f"⚝ **{from_user} Berhasil Join Ke Obrolan Suara**\n╚ **Chat ID:** `{chat_id}`", 3
            )
        except memek:
            return await ede(
                rambot, f"Maaf {from_user}, Lo udah di obrolan suara, dasar anjing lo.`", 10
            )
        except Exception:
            return await ede(rambot, f"**GA ADA OS DISINI KONTOL!!!**", 10)


@tod(pattern="lvc(?: |$)(.*)")
@ok(pattern=r"^\.clvc(?: |$)(.*)", sudo=True)
async def vc_end(event):
    rambot = await eor(event, "`Saatnya Turun...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await ede(rambot, f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
        toyik(event.sender)
    if chat_id:
        try:
            await sayang.leave_group_call(chat_id)
            await ede(
                rambot,
                f"⚝ **Berhasil Turun Obrolan Suara**\n╚ **Chat ID:** `{chat_id}`", 5
            )
        except Exception:
            return await ede(rambot, f"**LO LAGI GA DI OS KONTOL!!!!**", 10)
