import re

from userbot import iqthon


IQMOG = re.compile(
    "["
    "🔹"  
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
