from telethon.events import ChatAction
from kars import DEVS, DEVG, owner, bot
from kars.events import register
from kars.utils import get_user_from_event, ram_cmd

# thanks: liualvinas & vckyoubitch

@bot.on(ChatAction)
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from kars.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**Pengguna Gban Telah Bergabung** \n"
                            f"**Pengguna**: [{guser.id}](tg://user?id={guser.id})\n"
                            f"**Aksi**  : `Banned`"
                        )
                    except BaseException:
                        return


@ram_cmd(pattern="gbanb(?: |$)(.*)")
@register(pattern=r"^\.cgbanb(?: |$)(.*)", sudo=True)
async def gben(kars):
    dc = kars
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Ingin Mengaktifkan Perintah Global Banned!`")
    else:
        dark = await dc.edit("`Memproses Global Banned Pengguna Ini!!`")
    me = await kars.client.get_me()
    await dark.edit("`Global Banned Akan Segera Aktif!!`")
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    f"@{me.username}" if me.username else my_mention
    await kars.get_chat()
    a = b = 0
    if kars.is_private:
        user = kars.chat
        reason = kars.pattern_match.group(1)
    else:
        kars.chat.title
    try:
        user, reason = await get_user_from_event(kars)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "`MAAF BANGET MASSZEH 😔✋, LO GABISA GBAN DIA NGENTOT, ITU DEVELOPER GUA!!!`"
            )
        if user.id in DEVG:
            return await dark.edit("MAAF BANGET JING 🤪, LO GABISA GBAN ADMIN @obrolansuar")
        try:
            from kars.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await kars.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await kars.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit("`Global Banned Aktif ✅`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Mohon Balas Ke Pesan Pengguna`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**Kesalahan! Pengguna Ini Sudah Kena Perintah Global Banned.**"
            )
    except BaseException:
        pass
    return await dark.edit(
        f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **Perintah:** `{owner}`\n┣• **Pengguna:** [{user.first_name}](tg://user?id={user.id})\n┣• **Aksi:** `Global Banned`\n╰✠╼━━━━━━❖━━━━━━━✠")

@ram_cmd(pattern=r"ungbanb(?: |$)(.*)")
@register(pattern=r"^\.cungbanb(?: |$)(.*)", sudo=True)
async def gunben(kars):
    dc = kars
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`Membatalkan Perintah Global Banned Pengguna Ini`")
    else:
        dark = await dc.edit("`Membatalkan Perintah Global Banned`")
    me = await kars.client.get_me()
    await dark.edit(
        "`Memulai Membatalkan Perintah Global Banned, Jangan Songong Lagi Ya!!!`"
    )
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    f"@{me.username}" if me.username else my_mention
    await kars.get_chat()
    a = b = 0
    if kars.is_private:
        user = kars.chat
        reason = kars.pattern_match.group(1)
    else:
        kars.chat.title
    try:
        user, reason = await get_user_from_event(kars)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "**MAAF MASZEH, DIA GA BISA DI BLACKLIST KARNA DIA DEVELOPER GUA NGENTOT LO!!**"
            )
        try:
            from kars.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await kars.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await kars.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit("`Membatalkan Global Banned... Memproses... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Harap Balas Ke Pesan Pengguna`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit(
                "**Kesalahan! Pengguna Sedang Tidak Di Global Banned.**"
            )
    except BaseException:
        pass
    return await dark.edit(
        f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **Perintah:** `{owner}`\n┣• **Pengguna:** [{user.first_name}](tg://user?id={user.id})\n┣• **Aksi:** `Unglobal banned`\n╰✠╼━━━━━━❖━━━━━━━✠")
