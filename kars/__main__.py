""" rams start point """


import sys
import requests
from importlib import import_module

from pytgcalls import idle

from kars import BOT_VER, ramblacklist
from kars import LOGS, LOOP, bot
from kars.clients import ram_ubot_on, ramulti
from kars.modules import ALL_MODULES
from kars import call_py
try:
    for module_name in ALL_MODULES:
        imported_module = import_module("rams.modules." + module_name)
    client = karulti()
    total = 5 - client
    bot.start()
    call_py.start()
    user = bot.get_me()
    ramblacklist = requests.get(
        "https://raw.githubusercontent.com/ramadhani892/Ramblack/master/ramblacklist.json"
    ).json()
    if user.id in ramblacklist:
        LOGS.warning(
            "kars TIDAK DAPAT BERJALAN, KARNA LO KONTOL MAKE SEMEMA MENA, BOT LO DI MATIIN HEHEH, LAPORKAN KE @PakkPoll"        )
        sys.exit(1)
   # if 1826643972 not in DEVS:
      #  LOGS.warning(
       #     f"EOL\n✨ RAM - UBOT ✨ versi {BOT_VER}, © copyright by @merdhni"
       # )
       # sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOGS.info(f"Total Clients = {total} User")
LOGS.info(f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/ramsupportt")
LOGS.info(f"👑 KARMAN - UBOT 👑 v {BOT_VER} [DAH AKTIF KONTOL!]")
   

LOOP.run_until_complete(ram_ubot_on())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
