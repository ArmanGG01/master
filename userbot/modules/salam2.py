# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!
# YANG HAPUS KREDIT GUA TANDAIN REPO LO

from platform import uname
from userbot import CMD_HELP, BLACKLIST_CHAT, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, ram_cmd
from userbot.events import register

# ================= WELCOME ==================
#       HAYO YANG HAPUS KREDIT GUA JITAK
#                FROM RAM-UBOT
# ============================================

@ram_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**𝐀ssalamu'alaikum maszeh**")
    await event.delete()


@ram_cmd(pattern="gjm(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "GAK, JANGAN MAKSA YAH KONTOL!!")
    await event.delete()


@ram_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam kaum dajal...**")
    await event.delete()

@ram_cmd(pattern="gjn(?: |$)(.*)")
async def typewriter(event):
    await event.client.send_message(
        event.chat_id, "Ngomong apaan sih Gajelas Ngentottt")
    await event.delete()

@ram_cmd(pattern="yb(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Yabenarrrrrrr...**")
    await event.delete()


@ram_cmd(pattern="m(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
         event.chat_id, "**MEMEK NYA ANAK INIIIII....**")
    await event.delete()

@ram_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Apalo Kontolll....**")
    await event.delete()

@ram_cmd(pattern="gjb(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat.id, "**GAJELAS BABI....**")
    await event.delete()

@ram_cmd(pattern="gjk(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Gajelas Kontolll....**")
    await event.delete()

@ram_cmd(pattern="gbgn(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Ga banget, Ngentott!!!**")
    await event.delete()

@ram_cmd(pattern="gls(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**GAK, LO SANGEAN TOT!!!**")
    await event.delete()


@ram_cmd(pattern="bsl(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**BAU SAWI LO..!!**")
    await event.delete()


@ram_cmd(pattern="hoi(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Hai, Anak yatim!!**")
    await event.delete()


@ram_cmd(pattern="em(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Eh memek..!!!**")
    await event.delete()


@ram_cmd(pattern="eh(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "**EH NGENTOT...!**")
    await typew.delete()


@ram_cmd(pattern="ucp(?: |$)(.*)")
async def _(typeq):
    await typeq.client.send_message(
        typeq.chat_id, "**Lu siapa si ngentooootttt sokap bet sokap ajg!!!!**")
    await typeq.delete()  


@ram_cmd(pattern="hey(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "**Hey, Member Alay..😂**")
    await typew.delete()


@ram_cmd(pattern="loh(?: |$)(.*)")
async def _(typew):
     if typew.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            typew, f"**Dasar ngentot, Lo gabisa Nyoba disini anjing!!!**"
        )
    await typew.client.send_message(
        typew.chat_id, "**GC SAMPAH KAYA GINI, BUBARIN AJA PLIS!!🤣**")
    await typew.delete()
    
CMD_HELP.update({
    "ribut":
    ".p\
\nUsage:\
\n\n.l\
\nUsage:\
\n\n.gjm\
\nUsage:\
\n\n.gjn\
\nUsage:\
\n\n.gjb\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.gjk\
\nUsage:"
})

CMD_HELP.update({
    "war2":
    ".gbgn\
\nUsage:\
\n\n.bsl\
\nUsage:\
\n\n.hoi\
\nUsage:\
\n\n.eh\
\nUsage:\
\n\n.em\
\nUsage:\
\n\n.gls\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:\
\n\n.ucp\
\nUsage:\
\n\n.m\
\nUsage:\
\n\n.k\
\nUsage:"
})
