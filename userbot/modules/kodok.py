# Yang Hapus Besok Mati Aminnn
# Port By @Vckyouuu
# Piki mintaa yaaa
# Mks sm sm
# Rama ganteng mks sm sm


from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError

from userbot import CMD_HELP, rambot, bot
from userbot import CMD_HANDLER as cmd
from userbot.utils import ram_cmd

@ram_cmd(pattern=r"prg")
async def honkasays(event):
    await event.edit(f"`Sabar {rambot}, sedang memuat...`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit(f"`{rambot}, Beri sesuatu teks contoh {cmd}prg test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit(f"`{rambot} Saya tidak bisa menggunakan hal-hal sebaris di sini...`")
    except ChatSendStickersForbiddenError:
        await event.edit("Maaf {rambot}, saya tidak bisa mengirim stiker ke sini !!")


CMD_HELP.update({"prog": f"`{cmd}prg`\
    \nPenjelasan: {cmd}prg <kata kata>. Biar bisa lihat kodok bentuk badut"})
