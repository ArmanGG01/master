""" kars module for other small commands. """
from kars import CMD_HELP, ALIVE_NAME
from kars.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.rhelp` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[Arman](t.me/PakkPoll)"
        "\n\n[SUPPORT](https://t.me/obrolansuar)"
        "\n\n[CHANNEL](https://t.me/Karc0de)")


@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ArmanGG01/master/master/varshelper.txt)")


CMD_HELP.update({
    "karhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk RAM-UBOT.\
\n`.rvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
