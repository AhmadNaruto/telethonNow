import asyncio
from PIL import Image, ImageDraw, ImageFont
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import iqthon
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention




@iqthon.on(admin_cmd(pattern="بان وهمي(?: |$)(.*)"))
async def banohme(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"جاري حظر المستخدم {mention}\n"
    no_reason = "لايوجد سبب "
    await event.edit("**☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1226408155:
            await reply_message.reply("عذرا هذا مبرمج السورس")
        else:
            jnl = ("تم الحظر"
                   "[{}](tg://user?id={})"
                   f"` حظر المستخدم` {mention}\n\n"
                   "**الاسم: ** __{}__\n"
                   "**الايدي : ** `{}`\n"
                   ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**المعرف : ** لايمتلك معرف\n"
            elif usname != "None":
                jnl += "**المعرف** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**السبب: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = (
            f"حظر المستخدم {mention} ")
        await event.reply(mention)
    await event.delete()

    



@iqthon.on(admin_cmd(pattern="صنع هويه(?: |$)(.*)"))
async def hoah(event):
    replied_user = await event.get_reply_message()
    await event.client.download_profile_photo(
        replied_user.from_id, file="user.png", download_big=True
    )
    user_photo = Image.open("user.png")
    id_template = Image.open("userbot/resources/FrameID.png")
    user_photo = user_photo.resize((989, 1073))
    id_template.paste(user_photo, (1229, 573))
    position = (2473, 481)
    draw = ImageDraw.Draw(id_template)
    color = "rgb(23, 43, 226)"  # red color
    font = ImageFont.truetype("userbot/resources/fontx.ttf", size=200)
    draw.text(
        position,
        replied_user.sender.first_name.replace("\u2060", ""),
        fill=color,
        font=font,
    )
    id_template.save("user_id.png")
    await event.edit("`Membuat ID Card..`")
    await event.client.send_message(
        event.chat_id,
        "Generated User ID",
        reply_to=event.message.reply_to_msg_id,
        file="user_id.png",
        force_document=False,
        silent=True,
    )
    await event.delete()    
