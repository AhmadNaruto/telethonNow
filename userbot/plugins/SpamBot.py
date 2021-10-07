import os
from asyncio import sleep

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import iqthon




@iqthon.on(admin_cmd(pattern="فحص الحظر ?(.*)")
async def spam(SLQ):
    await event.edit("`Processing...`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Mohon Unblock @SpamBot dan coba lagi**")
            return
        await event.edit(f"~ {response.message.message}")

