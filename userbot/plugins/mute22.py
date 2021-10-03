import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from userbot import iqthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from ..sql_helper.mute_sql import is_muted, mute, unmute
from . import BOTLOG, BOTLOG_CHATID, get_user_from_event

plugin_category = "admin"



@iqthon.iq_cmd(
    pattern="كتم(?:\s|$)([\s\S]*)",
    command=("كتم", plugin_category),
    info={
        "header": "iqthon",
        "description": "iqthon",
        "الأستـخدام": " {tr}iqthon",
    },
)
async def startgmute(event):
    "iqthon"
    if event.is_private:
        await event.edit("**⌔︙ جاري الكتم**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == iqthon.uid:
            return await edit_or_reply(
                event, "**⌔︙ لا يـمكنك كتم نـفسك**"
            )
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**⌔︙ غيـر قـادر عـلى جـلب مـعلومات الـشخص **"
        )
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            f"**⌔︙ تـم كـتم الـمستـخدم بـنجاح ✅**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ**\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**⌔︙ تـم كـتم الـمستـخدم بـنجاح ✅**",
            )
        else:
            await edit_or_reply(
                event,
                f"**⌔︙ تـم كـتم الـمستـخدم بـنجاح ✅**",
            )
    if BOTLOG:
        reply = await event.get_reply_message()
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⌔︙ الـمستخدم** {_format.mentionuser(user.first_name ,user.id)}\n **⌔︙ تـم كتمه بنـجاح**\n **⌔︙ الدردشـة** {event.chat.title}\n"
                f"**⌔︙ السـبب:** {reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**⌔︙ الـمستخدم** {_format.mentionuser(user.first_name ,user.id)} \n**⌔︙ تـم كتمه بنـجاح**",
            )
        if reply:
            await reply.forward_to(BOTLOG_CHATID)



@iqthon.iq_cmd(
    pattern="الغاء كتم(?:\s|$)([\s\S]*)",
    command=("الغاء كتم", plugin_category),
    info={
        "header": "iqthon.",
        "description": "iqthon ",
        "usage": "{tr}iqthon",
    },
)
async def endgmute(event):
    "iqthon"
    if event.is_private:
        await event.edit("**⌔︙ قـد تـحدث بعـض الأخـطاء**")
        await asyncio.sleep(2)
        userid = event.chat_id
        reason = event.pattern_match.group(1)
    else:
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == iqthon.uid:
            return await edit_or_reply(event, "**⌔︙ لا يـمكنك كتم نـفسك**")
        userid = user.id
    try:
        user = (await event.client(GetFullUserRequest(userid))).user
    except Exception:
        return await edit_or_reply(
            event, "**⌔︙ غيـࢪ قـادࢪ عـلى جـلب مـعلومات الـشخص **"
        )
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, f"**⌔︙ هـذا الـمستخدم لـيس مكـتوم**")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, f"**خـطأ **\n`{e}`")
    else:
        if reason:
            await edit_or_reply(
                event,
                f"**⌔︙ تـم الـغاء كـتم الـمستـخدم بـنجاح**",
            )
        else:
            await edit_or_reply(
                event,
                f"**⌔︙ تـم الـغاء كـتم الـمستـخدم بـنجاح**",
            )
    if BOTLOG:
        if reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**⌔︙ الـغاء الكـتم**\n"
                f"**⌔︙ الـمستخدم :* {_format.mentionuser(user.first_name ,user.id)} \n"
                f"**⌔︙ السبب :** `{reason}`",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                 "**⌔︙ الـغاء الكـتم**\n"
                f"**⌔︙ المستخدم :** {_format.mentionuser(user.first_name ,user.id)} \n",
            )





@iqthon.iq_cmd(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


