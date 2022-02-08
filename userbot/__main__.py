# Copyright (C) 2019 The Raphielscape Company LLC.
# 
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from sys import argv
from telethon.tl.functions.channels import InviteToChannelRequest

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import BOTLOG_CHATID, BOT_USERNAME, BOT_VER, LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info(f"🔥RAM-UBOT🔥 ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN KONTOLL NGENTOT MEMEK ANJING BABI!!!]")

async def ram_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🔥 **PocongUserbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{branch}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@GeezSupport"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
    try:
        await bot(JoinChannelRequest("@GeezProjectt"))
    except BaseException:
        pass

bot.loop.run_until_complete(ram_userbot_on())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
