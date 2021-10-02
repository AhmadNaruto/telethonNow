import time
from userbot import iqthon
from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "LEObot"
ICS_IMG = "https://telegra.ph/file/ca2467e77ffcd605cc54d.jpg"
ICSS_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝐒𝐎𝐔𝐑𝐂𝐄 𝐋𝐄𝐎 𓆪"
ICSEM = "**⌔∮**"


@iqthon.on(admin_cmd(outgoing=True, pattern="المده$"))
@iqthon.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(ics):
    if ics.fwd_from:
        return
    icsid = await reply_id(ics)
    icsupt = await get_readable_time((time.time() - StartTime))
    if ICS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"**{ICSEM} المستخدم :** {mention}\n"
        ics_c += f"**{ICSEM} مدة التشغيل :** `{icsupt}`"
        await ics.client.send_file(ics.chat_id, ICS_IMG, caption=ics_c, reply_to=icsid)
        await ics.delete()
    else:
        await edit_or_reply(
            ics,
            f"**{ICSS_TEXT}**\n\n"
            f"**{ICSEM} المستخدم :** {mention}\n"
            f"**{ICSEM} مدة التشغيل :** `{icsupt}`",
        )
