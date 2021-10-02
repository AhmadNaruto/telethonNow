import time
from userbot import iqthon
from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "IQTHONbot"
IQ_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/17f2ad9df0b5aeed779d1.mp4"
IQTS_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬  :"
IQTEM = "**⌔∮**"


@iqthon.on(admin_cmd(outgoing=True, pattern="المده$"))
@iqthon.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(IQT):
    if IQT.fwd_from:
        return
    IQTid = await reply_id(IQT)
    IQTupt = await get_readable_time((time.time() - StartTime))
    if IQT_IMG:
        IQT_c = f"**{IQTS_TEXT}**\n"
        IQT_c += f"**{IQTEM} المستخدم :** {mention}\n"
        IQT_c += f"**{IQTEM} مدة التشغيل :** `{IQTupt}`"
        await IQT.client.send_file(IQT.chat_id, IQT_IMG, caption=IQT_c, reply_to=IQTid)
        await IQT.delete()
    else:
        await edit_or_reply(
            IQT,
            f"**{IQTS_TEXT}**\n\n"
            f"**{IQTEM} المستخدم :** {mention}\n"
            f"**{IQTEM} مدة التشغيل :** `{IQTupt}`",
        )
