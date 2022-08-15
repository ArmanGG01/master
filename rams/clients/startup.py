import sys

import telethon.utils

from rams import BOT_VER as version
from rams import (
    LOGS,
    LOOP,
    STRING_SESSION,
    ramblacklist,
    bot,
)


MSG_BLACKLIST = "MAKANYA JANGAN BELAGU BAE NGENTOD, rams {} LU UDAH DI MATIIN, LAPORKAN PADA @MERDHNI!!!!"


async def ram_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def ramulti():
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            LOOP.run_until_complete(ram_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if not STRING_SESSION:
        failed += 1
  
