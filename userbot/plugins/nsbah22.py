import random

from iqthon.klanr.resources.Contact import *
from userbot import iqthon

from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event

plugin_category = "utils"


@iqthon.iq_cmd(
    pattern="نسبة الحب(?:\s|$)([\s\S]*)",
    command=("نسبة الحب", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    iqth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    iqt = random.choice(kno)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{iqth}](tg://user?id={user.id}) هـي {iqt} 😔🖤"
    )


@iqthon.iq_cmd(
    pattern="نسبة الانوثة(?:\s|$)([\s\S]*)",
    command=("نسبة الانوثة", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    iqth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    iqt = random.choice(arb)
    await edit_or_reply(
        mention, f"⌯︙نسبة الانوثة لـ [{iqth}](tg://user?id={user.id}) هـي {iqt} 🥵🖤"
    )


@iqthon.iq_cmd(
    pattern="نسبة الغباء(?:\s|$)([\s\S]*)",
    command=("نسبة الغباء", plugin_category),
)
async def permalink(mention):
    """Generates a link to the user's PM with a custom text."""
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    iqth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    iqt = random.choice(arb)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{iqth}](tg://user?id={user.id}) هـي {iqt} 😂💔"
    )
