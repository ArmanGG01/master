import logging

from userbot import BOT_USERNAME
from userbot.events import register
from  userbot.utils import ram_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@ram_cmd(pattern="rhelp")
async def _(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@ram-userbot")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`The bot doesn't work! Please set the Bot Token and Username correctly. The module has been stopped..`"
            )
    except Exception:
        return await event.edit(
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
        )
