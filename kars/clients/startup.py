import sys

import telethon.utils

from rams import BOT_VER as version
from rams import (
    LOGS,
    LOOP,
    RAM2,
    RAM3,
    RAM4,
    RAM5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
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

    if STRING_2:
        try:
            RAM2.start()
            LOOP.run_until_complete(ram_client(RAM2))
            user = RAM2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_3:
        try:
            RAM3.start()
            LOOP.run_until_complete(ram_client(RAM3))
            user = RAM3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_4:
        try:
            RAM4.start()
            LOOP.run_until_complete(ram_client(RAM4))
            user = RAM4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if STRING_5:
        try:
            RAM5.start()
            LOOP.run_until_complete(ram_client(RAM5))
            user = RAM5.get_me()
            name = User.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in ramblacklist:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(f"{e}")

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
