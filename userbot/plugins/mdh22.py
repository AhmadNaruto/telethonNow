import time
from userbot import iqthon
from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "IQTHON"
IMOGTHON = "**ٍَ 🖤 ❬**"

@iqthon.on(admin_cmd(outgoing=True, pattern="المده$"))
@iqthon.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(ics):
    if ics.fwd_from:
        return
    icsid = await reply_id(ics)
    icsupt = await get_readable_time((time.time() - StartTime))
    if ICS_IMG:
        ics_c += f"**{IMOGTHON} المستخدم :** {mention}\n"
        ics_c += f"**{IMOGTHON} مدة التشغيل :** `{icsupt}`"
        await ics.client.send_file(ics.chat_id, ICS_IMG, caption=ics_c, reply_to=icsid)
        await ics.delete()
    else:
        await edit_or_reply(
            ics,
            f"**{IMOGTHON} المستخدم :** {mention}\n"
            f"**{IMOGTHON} مدة التشغيل :** `{icsupt}`",
        )
