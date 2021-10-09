from asyncio import sleep
from datetime import datetime
from math import sqrt

from emoji import emojize
from telethon import functions
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import ChannelParticipantsAdmins, MessageActionChannelMigrateFrom
from userbot import iqthon



@iqthon.on(admin_cmd(pattern="userid(?: |$)(.*)"))
async def useridgetter(target):
    """For .userid command, returns the ID of the target user."""
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"**Name:** {name} \n**User ID:** `{user_id}`")



@iqthon.on(admin_cmd(pattern="chatid(?: |$)(.*)"))
async def chatidgetter(chat):
    """For .chatid, returns the ID of the chat you are in at that moment."""
    await chat.edit("Chat ID: `" + str(chat.chat_id) + "`")





regexNinja = False

@iqthon.on(admin_cmd(pattern="s(?: |$)(.*)"))
async def sedNinja(event):
    """For regex-ninja module, auto delete command starting with s/"""
    if regexNinja:
        await sleep(0.5)
        await event.delete()


@iqthon.on(admin_cmd(pattern="regexninja (on|off)(?: |$)(.*)"))
async def sedNinjaToggle(event):
    """Enables or disables the regex ninja module."""
    global regexNinja
    if event.pattern_match.group(1) == "on":
        regexNinja = True
        await event.edit("`Successfully enabled ninja mode for Regexbot.`")
        await sleep(1)
        await event.delete()
    elif event.pattern_match.group(1) == "off":
        regexNinja = False
        await event.edit("`Successfully disabled ninja mode for Regexbot.`")
        await sleep(1)
        await event.delete()
