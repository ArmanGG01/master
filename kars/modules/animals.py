# Taken from
# https://github.com/AvinashReddy3108/PaperplaneRemix/blob/master/rams/plugins/memes.py

# TG-rams - A modular Telegram rams script for Python.
# Copyright (C) 2019 Kandarp <https://github.com/kandnub>
#
# TG-rams is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-rams is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-rams.  If not, see <https://www.gnu.org/licenses/>.

import requests

from rams import CMD_HANDLER as cmd
from rams import CMD_HELP
from rams.utils import edit_or_reply, ram_cmd as tod


@tod(pattern="dog$")
async def shibe(event):
    xx = await edit_or_reply(event, "`Nyari Mantan lu...`")
    response = requests.get("https://shibe.online/api/shibes").json()
    if not response:
        await event.edit("**Tidak bisa menemukan Anjing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0], reply_to=xx.reply_to_msg_id)
    await xx.delete()


@tod(pattern="cat$")
async def cats(event):
    xx = await edit_or_reply(event, "`Nyari kucing bentar...`")
    response = requests.get("https://shibe.online/api/cats").json()
    if not response:
        await event.edit("**Tidak bisa menemukan kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0], reply_to=xx.reply_to_msg_id)
    await xx.delete()

@tod(pattern="bird$")
async def bird(event):
    xx = await edit_or_reply(event, "`Nyari peler....`")
    response = requests.get("https://shibe.online/api/birds").json()
    if not response:
        await event.edit("**Tidak bisa menemukan kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0], reply_to=xx.reply_to_msg_id)
    await xx.delete()


CMD_HELP.update(
    {
        "animals": f"**Plugin : **`animals`\
        \n\n  •  **Syntax :** `{cmd}cat`\
        \n  •  **Function : **Untuk Mengirim gambar kucing secara random.\
        \n\n  •  **Syntax :** `{cmd}dog`\
        \n  •  **Function : **Untuk Mengirim gambar random dari anjing jenis Shiba.\
        \n\n  •  **Syntax :** `{cmd}bird`\
        \n  •  **Function : **Untuk Mengirim Gambar burung Secara random.\
    "
    }
)
