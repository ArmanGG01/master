# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from rams import CMD_HANDLER as cmd
from rams import CMD_HELP, DEVS
from rams.utils import edit_or_reply, ram_cmd as cuy
from rams.events import register as bro


@cuy(pattern="fgban(?: |$)(.*)")
@bro(pattern=r"^\.cgbn(?: |$)(.*)", sudo=True)
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    me = await event.client.get_me()
    mentions = f"**Warning!! User 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By** {me.first_name}\n"
    await edit_or_reply(event, "`Mengaktifkan global banned....✅`")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for _ in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        # make meself invulnerable cuz why not xD
        if idd in DEVS:
            await reply_message.reply(
                "`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 6969$ to my master__ [Heyworld](tg://user?id=1036951071) __to release your account__😏"
            )
        else:
            jnl = (
                f"**Global banned By** {me.first_name}\n\n"
                "**Frist Name: ** {}\n"
                "**User ID : ** `{}`\n"
            ).format(firstname, idd)
            if usname is None:
                jnl += "**Username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = f"**Reason: **{gbunm}"
                jnl += gbunr
            else:
                no_reason = "**Reason: **`Kang Tipu VCS`"
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            f"**Global Banned By** {me.first_name} \n**Reason:** `Anak Tolol` "
        )
        await event.reply(mention)
    await event.delete()


CMD_HELP.update(
    {
        "fakegban": f"**Plugin : **`fakegban`\
        \n\n  •  **Syntax :** `{cmd}fgban` <reply> <reason>\
        \n  •  **Function : **Untuk melakukan aksi Fake global banned , just for fun\
    "
    }
)
