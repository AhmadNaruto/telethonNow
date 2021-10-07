import asyncio

from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message

from userbot import iqthon


@Iqthon.on_message(filters.command(["unread", "un"], ".") & filters.me)
async def mark_chat_unread(bot, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.send(
            functions.messages.MarkDialogUnread(
                peer=await Iqthon.resolve_peer(message.chat.id), unread=True
            )
        ),
    )

