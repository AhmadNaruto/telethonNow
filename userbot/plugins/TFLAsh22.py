from asyncio import sleep

from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
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

from userbot import iqthon
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)
plugin_category = "admin"

KLANR_RIGHTS = ChatBannedRights(
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




@iqthon.iq_cmd(
    pattern="تفليش$",
    command=("تفليش", plugin_category),
    info={
        "header": "iqthon.",
        "description": "iqthon",
        "usage": [
            "{tr}iqthon",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(event):
    "iqthon"
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, event.client.uid)
    )
    if not result:
        return await edit_or_reply(
            event, "**⌔︙ ليس لديك صلاحيه حظر في هذا الدردشة**"
        )
    iqthonevent = await edit_or_reply(event, "**⌔︙جاري تفليش مجموعتك أنتظر قليلآ 🚮**")
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
                    EditBannedRequest(event.chat_id, user.id, KLANR_RIGHTS)
                )
                success += 15
                await sleep(0.2)  # for avoid any flood waits !!-> do not remove it
        except Exception as e:
            LOGS.info(str(e))
    await iqthonevent.edit(f"**⌔︙ تم بنجاح تفليش مجموعتك من {total} الاعضاء 🚮**")
