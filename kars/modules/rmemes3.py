# CREDIT NGENTOT KONTOL ANJNG!

from time import sleep
from kars import CMD_HELP, bot
from kars import CMD_HANDLER as cmd
from kars.events import ram_cmd as boy
import asyncio


@bot.on(boy(pattern="hua$", outgoing=True))
async def _(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Aku di ghosting")
        sleep(1)
        await e.edit("ð­ð­ð­")
        sleep(1)
        await e.edit("Aku Sedihhh")
        sleep(1)
        await e.edit("Kenapa si")
        sleep(1)
        await e.edit("GAMPANG BGT NYAKITIN")
        sleep(1)
        await e.edit("HATI GUA BUKAN BUAT DI GHOSTING")
        sleep(1)
        await e.edit("TAI BANGET ASLI")
        sleep(1)
        await e.edit("PARAH SI")
        sleep(1)
        await e.edit("DEMI APASII")
        sleep(1)
        await e.edit("TWINGG")
        sleep(1)
        await e.edit("KONTOL")
        sleep(1)
        await e.edit("MEMEK")
        sleep(1)
        await e.edit("AKU DI GHOSTING")
        sleep(1)
        await e.edit("BANGSAT")
        sleep(1)
        await e.edit("ANJING")
        sleep(1)
        await e.edit("ð¡ð¡ð¡")
        sleep(1)
        await e.edit("ð¥´ð¥´ð¥´")
        sleep(1)
        await e.edit("ANJINGGGGà¼¼")
        sleep(1)
        await e.edit("TAIIII")
        sleep(1)
        await e.edit("AH ELAHH BABI")
        sleep(1)
        await e.edit("GAUSAH GANGGU")
        sleep(1)
        await e.edit("GUA STRESS")
        sleep(1)
        await e.edit("ð­ð­ð­ð­ð­ð­")
        sleep(1)
        await e.edit("ð¥´ð¥´ð¥´ð¥´")
        sleep(1)
        await e.edit("ADA YG MAU SAMA GUA?")
        sleep(1)
        await e.edit("PLISS GUA BUTUH")
        sleep(1)
        await e.edit("SESEORANG YG MAU NERIMA GUA")
        sleep(1)
        await e.edit("ðððð")
        sleep(1)
        await e.edit("MAU GAK JADI PACAR GUA??à¼¼")
        sleep(1)
        await e.edit("à¼¼ TAPI BOONG TOD!!à¼½")


@bot.on(boy(pattern="huh", outgoing=True))
async def _(event):
    await event.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n />â¤ï¸ *NIH GUA KASIH BUAT LU!!`")
    sleep(3)
    await event.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n/>ð  *E GAK DEH,UDH DI KSH GRATIS LU RUSAKIN`")
    sleep(2)
    await event.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\nð<\\  *KENTOD`")


@bot.on(boy(pattern=r"(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 103)
    input_str = event.pattern_match.group(1)
    if input_str == "story":
        await event.edit(input_str)
        animation_chars = [
            "`Cerita â¤ï¸ Cinta` ",
            "  ð             ð \n/ð\\         <ð\\ \n ð               /|",
            "  ð          ð³ \n/ð\\       /ð\\ \n  ð            /|",
            "  ð            ð \n/ð\\         <ð> \n  ð             /|",
            "  ð         âºï¸ \n/ð\\      /ð\\ \n  ð          /|",
            "  ð          ð \n/ð\\       /ð\\ \n  ð           /|",
            "  ð   ð \n /ð\\/ð\\ \n   ð   /|",
            " ð³  ð \n /|\\ /ð\\ \n /     / |",
            "ð    /ð°\\ \n<|\\      ð \n /ð    / |",
            "ð \n/(),âð® \n /\\         _/\\/|",
            "ð \n/\\_,__ð« \n  //    //       \\",
            "ð \n/\\_,ð¦_ð  \n  //         //        \\",
            "  ð­      âºï¸ \n  /|\\   /(ð¶)\\ \n  /!\\   / \\ ",
            "`TAMAT ð`"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(boy(pattern=r"(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 11)
    input_str = event.pattern_match.group(1)
    if input_str == "canda":
        await event.edit(input_str)
        animation_chars = [
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â   â    â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Kamu    â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â       â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Pasti   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__|â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Belum   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â          â¡\n  â â¢¿â£¯â â â (x)â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â    â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Mandi Wajib  â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __ â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â  â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Bwhaha  â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__| â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â   â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ GOBLOK   â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â ****â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(boy(pattern="nah(?: |$)(.*)", outgoing=True))
async def _(event):
    await event.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n />ð *Ini Buat Kamu`")
    sleep(2)
    await event.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\nð<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@bot.on(boy(pattern=r"(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 6)
    input_str = event.pattern_match.group(1)
    if input_str == "owner":
        await event.edit(input_str)
        animation_chars = [
            "**OWNER RAM-UBOT ADALAH MANUSIA TERGANTENG DI HATI PEMAKAI NYA, KENALAN DULU SAMA OWNER NYA YUK**"
            "**RAMADHANI NAMANYA,ORANG NYA BAIK**"
            "**TINGGAL NYA DI TANGERANG, BTW ORANG TANGERANG GANTENG GANTENG DAN THEBEST POKOK NYA AWWHHHH**"
            "**KALO MAU FORK REPONYA,IZIN DULU KE ORANG NYA YA GENGSSS**"
            "**POKOK NYA OWNER NYA THEBEST BANGET SERIUSSSSS**"
            "**UDAH POKOK NYA ITU AJA SIH,INTINYA OWNER NYA GANTENG DAN BAIK PARAH**"]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 6])

CMD_HELP.update({
    "memes5":
    f"`{cmd}nah` ; `{cmd}huh` ; `{cmd}owner`\
    \nUsage: cobain.\
    \n\n`{cmd}bunga` ; `{cmd}buah`\
    \nUsage: animasi.\
    \n\n`{cmd}waktu`\
    \nUsage: animasi."
})

CMD_HELP.update({
    "memes6":
    f"`{cmd}hua`\
    \nUsage: nangis.\
    \n\n`{cmd}cinta` ; `{cmd}canda`\
    \nUsage: liat sendiri"
})
