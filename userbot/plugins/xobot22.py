import re


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import iqthon


IQMOG = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental aliosamg
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)

def iqtfy(inputString: str) -> str:
    """قم بإزالة الرموز التعبيرية """
    return re.sub(IQMOG, "", inputString)


@iqthon.on(admin_cmd(pattern="اكس او(?: |$)(.*)"))
async def iq(SLQ):
    kn = SLQ.pattern_match.group(1)
    if not kn:
        if SLQ.is_reply:
            (await SLQ.get_reply_message()).message

            return
    LLL5L = await bot.inline_query("xobot", f"{(iqtfy(kn))}")
    await LLL5L[0].click(
        SLQ.chat_id,
        reply_to=SLQ.reply_to_msg_id,
        silent=True if SLQ.is_reply else False,
        hide_via=True,
    )

@iqthon.on(admin_cmd(pattern="همسه ?(.*)"
                   ))
async def iq(SLQ):
    if SLQ.fwd_from:
        return
    kkno = SLQ.pattern_match.group(1)
    donttag = "@whisperBot"
    if SLQ.reply_to_msg_id:
        await SLQ.get_reply_message()
    l5 = await bot.inline_query(donttag, kkno)
    await l5[0].click(SLQ.chat_id)
    await SLQ.delete()

@iqthon.on(admin_cmd(pattern="عدد رسائلي ?(.*)"
                   ))
async def iq(SLQ):
    k = await SLQ.get_reply_message()
    if k:
        a = await bot.get_messages(SLQ.chat_id, 0, from_user=k.sender_id)
        return await SLQ.edit(
            f"**مجموع** `{a.total}` **الرسائل** {thon} **هنا**"
        )
    thon = SLQ.pattern_match.group(1)
    if not thon:
        thon = "me"
    a = await bot.get_messages(SLQ.chat_id, 0, from_user=thon)
    await SLQ.edit(
        f"*مجموع `{a.total}` الرسائل هنا**"
    )
    
@iqthon.on(admin_cmd(pattern="فحص الحظر ?(.*)"
                   ))
async def iq(SLQ):
    await SLQ.edit("جاري الفحص")
    async with bot.conversation("@SpamBot") as l5:
        try:
            dontTag = l5.wait_SLQ(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await l5.send_message("/start")
            dontTag = await dontTag
            await bot.send_read_acknowledge(l5.chat_id)
        except YouBlockedUserError:
            await SLQ.edit("**قم بفك حظر @SpamBot للاكمال**")
            return
        await SLQ.edit(f"~ {dontTag.message.message}")    
