import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from userbot import iqthon
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch

plugin_category = "utils"
LOGS = logging.getLogger(__name__)


async def fetch_info(replied_user, event):
    """Get details from the User object."""
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(
            user_id=replied_user.user.id, offset=42, max_id=0, limit=80
        )
    )
    replied_user_profile_photos_count = "`لم يقم المستخدم بتعيين صورة الملف الشخصي`"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    last_name = replied_user.user.last_name
    try:
        dc_id, location = get_input_location(replied_user.profile_photo)
    except Exception:
        dc_id = "`تعذر جلب معرف DC`"
    common_chat = replied_user.common_chats_count
    username = replied_user.user.username
    user_bio = replied_user.about
    is_bot = replied_user.user.bot
    restricted = replied_user.user.restricted
    verified = replied_user.user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("`هذا المستخدم ليس له اسم`")
    )
    last_name = last_name.replace("\u2060", "") if last_name else (" ")
    username = "@{}".format(username) if username else ("`هذا الشخص لايوجد لديه معرف`")
    user_bio = "`هذا الشخص لايوجد لديه نــبــذة`" if not user_bio else user_bio
    caption = "<b>• ⚜️ | مــعــلــومــات الــمــســتــخــدم :</b>\n"
    caption += f"<b>• ⚜️ | الاســم  :  </b> {first_name} {last_name}\n"
    caption += f"<b>• ⚜️ | الــمــ؏ــࢪف  : </b> {username}\n"
    caption += f"<b>• ⚜️ | الايــدي  :  </b> <code>{user_id}</code>\n"
    caption += f"<b>• ⚜️ | ؏ــدد صــوࢪڪ  : </b> {replied_user_profile_photos_count}\n"
    caption += f"<b>• ⚜️ | الــنــبــذة  : </b>  <code>{user_bio}</code>\n"
    caption += f"<b>• ⚜️ | الــمــجــمــو؏ــات الـمـشـتـࢪكـة  : </b> {common_chat}\n"
    caption += f"<b>• ⚜️ | رابــط مــبـاشـࢪ لــہ الـحـسـابہ  :  </b> \n"
    caption += f'• ⚜️ | <a href="tg://user?id={user_id}">{first_name}</a> \n'
    return photo, caption





@iqthon.iq_cmd(
    pattern="ايدي(?:\s|$)([\s\S]*)",
    command=("ايدي", plugin_category),
    info={
        "header": "Gets info of an user.",
        "description": "User compelete details.",
        "usage": "{tr}whois <username/userid/reply>",
    },
)
async def who(event):
    "Gets info of an user"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user, reason = await get_user_from_event(event)
    if not replied_user:
        return
    cat = await edit_or_reply(event, "**• ⚜️ | جـاري جـلب ايـدي المسـتخدم  🆔**")
    replied_user = await event.client(GetFullUserRequest(replied_user.id))
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(cat, "**• ⚜️ | تعذر جلب معلومات هذا المستخدم.**")
    message_id_to_reply = await reply_id(event)
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await cat.delete()
    except TypeError:
        await cat.edit(caption, parse_mode="html")


@iqthon.iq_cmd(
    pattern="رابط الحساب(?:\s|$)([\s\S]*)",
    command=("رابط الحساب", plugin_category),
    info={
        "header": "Generates a link to the user's PM .",
        "usage": "{tr}link <username/userid/reply>",
    },
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"• ⚜️ | [{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"• ⚜️ | [{tag}](tg://user?id={user.id})")
