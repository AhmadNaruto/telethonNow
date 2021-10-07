import re




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

@iqthon.on(admin_cmd(pattern="^\.tmsg (.*)")
async def iq(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(
            f"**Total ada** `{a.total}` **Chat Yang dikirim Oleh** {u} **di Grup Chat ini**"
        )
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=u)
    await event.edit(
        f"**Total ada `{a.total}` Chat Yang dikirim Oleh saya di Grup Chat ini**"
    )
