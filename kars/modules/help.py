# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" rams help command """

from rams import CMD_HANDLER as cmd
from rams import CMD_HELP, EMOJI_HELP, bot
from rams.utils import edit_delete, edit_or_reply, ram_cmd

modules = CMD_HELP


@ram_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """For help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"𝘔𝘢𝘢𝘧 𝘔𝘰𝘥𝘶𝘭𝘦 `{args}` 𝘛𝘪𝘥𝘢𝘬 𝘋𝘢𝘱𝘢𝘵 𝘋𝘪𝘵𝘦𝘮𝘶𝘬𝘢𝘯!!")
    else:
        user = await bot.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{EMOJI_HELP}\t\t\t"
        await edit_or_reply(
            event,
            f"{EMOJI_HELP}   {string}"
            f"\n\nSupport @RAM_UBOT\n"
        )
        await event.reply(
            f"╭┄──────┈┄┈──────┄\n"
            f"│ ▸ **Daftar Perintah RAM-UBOT :**\n"
            f"│ ▸ **Jumlah** `{len(modules)}` **Modules**\n"
            f"│ ▸ **Owner:** [{user.first_name}](tg://user?id={user.id})\n"
            f"├┄─────┈┄┈─────┄\n"
            f"│ **Contoh Ketik** `{cmd}help ping`\n"
            f"│ **Untuk Melihat Informasi Module**\n"
            f"╰┄──────┈┈──────┄"
        )
