import asyncio
from time import sleep

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

from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from userbot import iqthon
from . import *


BanTelethonAr = ChatBannedRights(
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

@iqthon.on(admin_cmd(pattern=r"تفليش ?(.*)"))
@iqthon.on(sudo_cmd(pattern=r"تفليش ?(.*)", allow_sudo=True))
async def _(event):
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result:
        return await eod(
            event, "انتضر هناك مشكله"
        )
    klanr = await eor(event, "**جاري الاستعداد لتفليش مجموعتك ..**")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BanTelethonAr)
                )
                success += 1
                await asyncio.sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await asyncio.sleep(0.5)
    await klanr.edit(
        "**تفليش مجموعتك اكتمل ...**"
    )
    await bot.send_message(
        Config.LOGGER_ID,
        f"**تفليش مجموعتك اكتمل ...** :  `{success}`  عدد من اصل  `{total}`  عضو ",
    )
