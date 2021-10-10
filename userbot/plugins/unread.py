import asyncio

from ..sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from telethon import events

from userbot import iqthon


@iqthon.on(admin_cmd(pattern="unread(?: |$)(.*)"))
async def mark(bot):
    await asyncio.gather(
        bot.delete(),
        bot.send(
            functions.messages.MarkDialogUnread(
                peer=await iqthon.resolve_peer(message.chat.id), unread=True
            )
        ),
    )
