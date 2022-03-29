import asyncio
from pytgcalls.methods.groups import JoinGroupCall
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.exceptions import (
    NoActiveGroupCall,
    AlreadyJoinedError,
    NotInGroupCallError
)
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import call_py
from userbot.utils import edit_delete, edit_or_reply, ram_cmd

from userbot.utils.queues.queues import clear_queue

def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"



# credits by @vckyaz < vicky \>
# FROM GeezProjects < https://github.com/vckyou/GeezProjects \>
# ambil boleh apus credits jangan ya ka:)

@ram_cmd(pattern="joinvc(?: |$)(.*)")
async def join_(event):
    geezav = await edit_or_reply(event, f"**Processing**")
    if len(event.text.split()) > 1:
        chat = event.chat_id
        chats = event.pattern_match.group(1)
        try:
            chat = await event.client(GetFullUserRequest(chats))
        except AlreadyJoinedError as e:
            await call_py.leave_group_call(chat)
            clear_queue(chat)
            await asyncio.sleep(3)
            return await edit_delete(event, f"**ERROR:** `{e}`", 30)
        except (NodeJSNotInstalled, TooOldNodeJSVersion):
            return await edit_or_reply(event, "NodeJs is not installed or installed version is too old.")
    else:
        chat_id = event.chat_id
        chats = event.pattern_match.group(1)
        from_user = vcmention(event.sender)
    if not call_py.is_connected:
        await call_py.start()
    await call_py.join_group_call(
        chat_id,
        AudioPiped(
            'http://duramecho.com/Misc/SilentCd/Silence01s.mp3'
        ),
        chats,
        stream_type=StreamType().pulse_stream,
    )
    await geezav.edit(f"**{from_user} Berhasil Naik Ke VC Group!**")


@ram_cmd(pattern="leavevc(?: |$)(.*)")
async def leavevc(event):
    """ leave video chat """
    geezav = await edit_or_reply(event, "Processing")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if from_user:
        try:
            await call_py.leave_group_call(chat_id)
        except (NotInGroupCallError, NoActiveGroupCall):
            await edit_or_reply(event, f"{from_user} Tidak Berada Di VC Group.")
        await geezav.edit(f"**{from_user} Berhasil Turun Dari VC Group.**")

CMD_HELP.update(
    {
        "vcplugin": f"**Plugin : **`vcplugin`\
        \n\n  •  **Syntax :** `{cmd}play` <Judul Lagu/Link YT>\
        \n  •  **Function : **Untuk Memutar Lagu di voice chat group dengan akun kamu\
        \n\n  •  **Syntax :** `{cmd}vplay` <Judul Video/Link YT>\
        \n  •  **Function : **Untuk Memutar Video di voice chat group dengan akun kamu\
          "
    }
)
