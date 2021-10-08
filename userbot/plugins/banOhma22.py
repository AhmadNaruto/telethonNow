import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import iqthon
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
                   f"` جاري حظر المستخدم سيدي : {mention}\n\n"
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
            f"جاري حظر المستخدم سيدي : {mention} ")
        await event.reply(mention)
    await event.delete()

    
