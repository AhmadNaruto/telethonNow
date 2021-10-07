import os
from asyncio import sleep

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import iqthon
from userbot.utils import edit_delete, edit_or_reply



@iqthon.on(admin_cmd(pattern="فحص الحظر ?(.*)")
async def spamtaste(SQL):
    await SQL.edit("جاري الفحص")
    async with bot.conversation("@SpamBot") as l5:
        try:
            donttag = l5.wait_SQL(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await l5.send_message("/start")
            donttag = await donttag
            await bot.send_read_acknowledge(l5.chat_id)
        except YouBlockedUserError:
            await SQL.edit("**فك الحظر @SpamBot **")
            return
        await SQL.edit(f"~ {donttag.message.message}")
