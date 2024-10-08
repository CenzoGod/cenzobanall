#  Copyright (c) 2023 @AM_YTBOTT - AMBOT
# Telegram Ban All Bot 
# Creator - AMBOT

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


logging.basicConfig(level=logging.INFO)

print("𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜.....")

Riz = TelegramClient('Riz', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f" **Wʜᴏ ᴅᴀʀᴇs sᴜᴍᴍᴏɴ ᴛʜᴇ Rᴇᴀᴘᴇʀ? Sᴘᴇᴀᴋ ʏᴏᴜʀ ᴘᴜʀᴘᴏsᴇ, ᴏʀ ғᴀᴄᴇ ᴛʜᴇ ᴄᴏɴsᴇǫᴜᴇɴᴄᴇs…** \n\n `{ms}` ms")


@Riz.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝙐𝙨𝙚 𝙏𝙝𝙞𝙨 𝘾𝙢𝙙 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥."
         await event.reply(Reply)
     else:
         await event.delete()
         RiZ = await event.get_chat()
         RiZoeLop = await event.client.get_me()
         admin = RiZ.admin_rights
         creator = RiZ.creator
         if not admin and not creator:
              return await event.reply("𝙄 𝘿𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝘽𝙖𝙣 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙍𝙞𝙜𝙝𝙩𝙨 !!")
         RiZoeL = await Riz.send_message(event.chat_id, "**Vᴇʀɪʟʏ, ᴛʜᴇ ɪᴍᴘᴀᴄᴛ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ғᴀʟʟᴇɴ ᴜᴘᴏɴ ʏᴏᴜ. Lᴇᴛ ɴᴏᴛʜɪɴɢ ʙᴜᴛ sɪʟᴇɴᴄᴇ ʀᴇᴍᴀɪɴ....**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         kimk = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
                if user.id not in admins_id:
                    await event.client.kick_participant(event.chat_id, user.id)
                    kimk += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
         await RiZoeL.edit(f"**Tʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ ʀɪᴛᴇ. Aʟʟ ᴜsᴇʀs ʜᴀᴠᴇ ʙᴇᴇɴ ᴄᴀsᴛ ɪɴᴛᴏ ᴛʜᴇ ᴅᴀʀᴋ. Tʜᴇ ᴄʜᴀᴍʙᴇʀ ɪs ᴇᴍᴘᴛʏ, ᴀɴᴅ ᴛʜᴇ sʜᴀᴅᴏᴡs ʀᴇɪɢɴ ᴜɴᴄʜᴀʟʟᴇɴɢᴇᴅ. Wʜᴏ ᴅᴀʀᴇs ᴅᴇғʏ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ?! \n\n Kicked Users:** `{kimk}` \n **From total users:** `{all}`")
    

@Riz.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f" Use This Cmd in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         RiZ = await event.get_chat()
         RiZoeLop = await event.client.get_me()
         admin = RiZ.admin_rights
         creator = RiZ.creator
         if not admin and not creator:
              return await event.reply("𝙄 𝘿𝙤𝙣'𝙩 𝙝𝙖𝙫𝙚 𝘽𝙖𝙣 𝙋𝙚𝙧𝙢𝙞𝙨𝙨𝙞𝙤𝙣 𝙍𝙞𝙜𝙝𝙩𝙨 !!")
         RiZoeL = await Riz.send_message(event.chat_id, " **Vᴇʀɪʟʏ, ᴛʜᴇ ɪᴍᴘᴀᴄᴛ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ғᴀʟʟᴇɴ ᴜᴘᴏɴ ʏᴏᴜ. Lᴇᴛ ɴᴏᴛʜɪɴɢ ʙᴜᴛ sɪʟᴇɴᴄᴇ ʀᴇᴍᴀɪɴ....**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                   print(str(e))
                   await asyncio.sleep(0.1)
         await RiZoeL.edit(f"**Tʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ ʀɪᴛᴇ. Aʟʟ ᴜsᴇʀs ʜᴀᴠᴇ ʙᴇᴇɴ ᴄᴀsᴛ ɪɴᴛᴏ ᴛʜᴇ ᴅᴀʀᴋ. Tʜᴇ ᴄʜᴀᴍʙᴇʀ ɪs ᴇᴍᴘᴛʏ, ᴀɴᴅ ᴛʜᴇ sʜᴀᴅᴏᴡs ʀᴇɪɢɴ ᴜɴᴄʜᴀʟʟᴇɴɢᴇᴅ. Wʜᴏ ᴅᴀʀᴇs ᴅᴇғʏ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ?!** \n\nBanned Users:** `{bann}` \n **From Total Users:** `{all}`")

    
@Riz.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
   if event.sender_id in SUDO_USERS:
     if not event.is_group:
         Reply = f"𝙈𝙮 𝙎𝙪𝙙𝙤 𝙐𝙨𝙚𝙧  !! 𝙐𝙨𝙚 𝙏𝙝𝙞𝙨 𝘾𝙢𝙙 𝙞𝙣 𝙂𝙧𝙤𝙪𝙥."
         await event.reply(Reply)
     else:
         msg = await event.reply("𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜 𝙋𝙖𝙧𝙩𝙞𝙘𝙞𝙥𝙖𝙣𝙩 𝙇𝙞𝙨𝙩𝙨...")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleeping for {ex.seconds} seconds")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))


@Riz.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in SUDO_USERS:
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = rizoel[0]
            bc = int(bc)
            text = "Tʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪᴛs ᴍɪssɪᴏɴ. ᴡᴇ ᴀʟʟ ᴀʟᴏɴᴇ ᴡɪᴛʜ ᴛʜᴇ sʜᴀᴅᴏᴡs ᴀs ɪ ʟᴇᴀᴠᴇ ᴛʜɪs ʀᴇᴀʟᴍ. ʙᴇ ᴀᴡᴀʀᴇ: ᴛʜᴇ sᴜʀɢᴇ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ'ꜱ ʟᴇᴀᴠɪɴɢ ʜᴀs ʙᴇᴇɴ ɴᴏᴛᴇᴅ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Tʜᴇ Rᴇᴀᴘᴇʀ ʜᴀs ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪᴛs ᴍɪssɪᴏɴ. ᴡᴇ ᴀʟʟ ᴀʟᴏɴᴇ ᴡɪᴛʜ ᴛʜᴇ sʜᴀᴅᴏᴡs ᴀs ɪ ʟᴇᴀᴠᴇ ᴛʜɪs ʀᴇᴀʟᴍ. ʙᴇ ᴀᴡᴀʀᴇ: ᴛʜᴇ sᴜʀɢᴇ ᴏғ ᴛʜᴇ Rᴇᴀᴘᴇʀ'ꜱ ʟᴇᴀᴠɪɴɢ ʜᴀs ʙᴇᴇɴ ɴᴏᴛᴇᴅ...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("𝙎𝙪𝙘𝙘𝙚𝙨𝙛𝙪𝙡𝙡𝙮 𝙇𝙚𝙛𝙩")
            except Exception as e:
                await event.edit(str(e))   
          

@Riz.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Restarting__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Riz.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("Your Ban All AMBot Deployed Successfully ✅")

Riz.run_until_disconnected()
