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

def deEmojify(inputString: str) -> str:
    """قم بإزالة الرموز التعبيرية """
    return re.sub(IQMOG, "", inputString)


@iqthon.on(admin_cmd(pattern="اكس او(?: |$)(.*)"))
async def nope(doit):
    kn = doit.pattern_match.group(1)
    if not kn:
        if doit.is_reply:
            (await doit.get_reply_message()).message

            return
    LLL5L = await bot.inline_query("xobot", f"{(deEmojify(kn))}")
    await LLL5L[0].click(
        doit.chat_id,
        reply_to=doit.reply_to_msg_id,
        silent=True if doit.is_reply else False,
        hide_via=True,
    )

@iqthon.on(admin_cmd(pattern="همسه ?(.*)"
                   ))
async def hmsh(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()
