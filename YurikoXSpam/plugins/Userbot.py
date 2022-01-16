# Yuriko X Spam - Spam Userbots
# © 2021 - 2022 - TheYuriko

import os
import sys
from YurikoXSpam import Yur, Yur2, Yur3, Yuri4, Yur5 , Yur6, Yur7, Yur8, Yur9, Yur10, Yur11, Yur12, Yur13, Yur14, Yur15, Yur16, Yur17, Yur18, Yur19, Yur20, Yur21, Yur22, Yur23, Yur24, Yur25, Yur26, Yur27, Yur28, Yur29, Yur30, Yur31, Yur32, Yur33, Yur34, Yur35, Yur36, Yur37, Yur38, Yur39, Yur40, SUDO_USERS
from YurikoXSpam import ALIVE_PIC, yurikoversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from time import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Yur.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@yur7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yuri2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yuri4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Yur40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop = f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\nϟ үυяιкσ x sραм ϟ︎ `{ms}` ᴍs"                   
        await fuk.edit(pingop)


# ALIVE

YURI_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/5f119690b8ad57b0cae94.jpg"


yuriko = "✧ үυяιкσ x sραм 𝗛𝗲𝗿𝗲 ✧\n\n"

yuriko += f"┏━━━━━━━━━━━━━━━━━━━\n"

yuriko += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

yuriko += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

yuriko += f"┣➣ **YurikoXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{yurikoversion}`\n"
    
yuriko += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/YURIKOXSPAMGOD)\n"

yuriko += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/YURIKOXSPAM)\n"

yuriko += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

yuriko += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/XRAJVEER09OP/YurikoXSpam) 🖤"            
                                    
@Yur.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  YURI_PIC,
                                  caption=yuriko)
   
   
# help

HELP_PIC = "https://telegra.ph/file/5f119690b8ad57b0cae94.jpg"

YurikoX = "🔥 үυяιкσ x sραм 🔥\n\n"
 
YurikoX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ үυяιкσ x sραм__\n\n"

YurikoX += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

YurikoX += f" `.ping` - `.alive` - `.setname` - `.setbio` - `.inviteall` - .`restart` - `.update` - `.stats` - `.addsudo` \n\n"
 
YurikoX += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

YurikoX += f" `.join` - `.pjoin` - `.leave`\n\n"
 
YurikoX += f" ↧ 𝚂𝙿𝙰𝙼 / 𝚁𝙰𝙸𝙳 𝙲𝙼𝙳𝚂 ↧\n\n"

YurikoX += f" `.raid` - `.replyraid` - `.dreplyraid` - `.delayraid` \n\n `.spam` - `.bigspam` - `.delayspam` - `.abuse` \n\n"

YurikoX += f" 𝙳𝙼 / 𝙴𝚌𝚑𝚘 𝙲𝚖𝚍𝚜 \n\n"

YurikoX += f" `.dm` - `.dmraid` - `.dmspam` \n\n `.addecho` - `.rmecho` \n\n"

YurikoX += f"All Cmds Uploaded : [•HERE•](https://t.me/Resourcez/4) \n\n"
 
YurikoX += f"© @YurikoXSpam | @YurikoXSpamgod\n"


@Yur.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Yur.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=YurikoX)                                                         


@Yur.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@yur7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yuri2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yuri4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Yur40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂\n\n ....Please Wait Until үυяιкσ x sραм Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Yur.disconnect()
        except Exception:
            pass
        try:
            await Yur2.disconnect()
        except Exception:
            pass
        try:
            await Yur3.disconnect()
        except Exception:
            pass
        try:
            await Yur4.disconnect()
        except Exception:
            pass
        try:
            await Yur5.disconnect()
        except Exception:
            pass
        try:
            await Yur6.disconnect()
        except Exception:
            pass
        try:
            await Yur7.disconnect()
        except Exception:
            pass
        try:
            await Yur8.disconnect()
        except Exception:
            pass
        try:
            await Yur9.disconnect()
        except Exception:
            pass
        try:
            await Yur10.disconnect()
        except Exception:
            pass
        try:
            await Yur11.disconnect()
        except Exception:
            pass
        try:
            await Yur12.disconnect()
        except Exception:
            pass
        try:
            await Yur13.disconnect()
        except Exception:
            pass
        try:
            await Yur14.disconnect()
        except Exception:
            pass
        try:
            await Yur15.disconnect()
        except Exception:
            pass
        try:
            await Yur16.disconnect()
        except Exception:
            pass
        try:
            await Yur17.disconnect()
        except Exception:
            pass
        try:
            await Yur18.disconnect()
        except Exception:
            pass
        try:
            await Yur19.disconnect()
        except Exception:
            pass
        try:
            await Yur20.disconnect()
        except Exception:
            pass
        try:
            await Yur21.disconnect()
        except Exception:
            pass
        try:
            await Yur22.disconnect()
        except Exception:
            pass
        try:
            await Yur23.disconnect()
        except Exception:
            pass
        try:
            await Yur24.disconnect()
        except Exception:
            pass
        try:
            await Yur25.disconnect()
        except Exception:
            pass
        try:
            await Yur26.disconnect()
        except Exception:
            pass
        try:
            await Yur27.disconnect()
        except Exception:
            pass
        try:
            await Yur28.disconnect()
        except Exception:
            pass
        try:
            await Yur29.disconnect()
        except Exception:
            pass
        try:
            await Yur30.disconnect()
        except Exception:
            pass
        try:
            await Yur31.disconnect()
        except Exception:
            pass
        try:
            await Yur32.disconnect()
        except Exception:
            pass
        try:
            await Yur33.disconnect()
        except Exception:
            pass
        try:
            await Yur34.disconnect()
        except Exception:
            pass
        try:
            await Yur35.disconnect()
        except Exception:
            pass
        try:
            await Yur36.disconnect()
        except Exception:
            pass
        try:
            await Yur37.disconnect()
        except Exception:
            pass
        try:
            await Yur38.disconnect()
        except Exception:
            pass
        try:
            await Yur39.disconnect()
        except Exception:
            pass
        try:
            await Yur40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
