import time
from userbot import iqthon
from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "IQTHON"
IMOGTHON = "**ٍَ 🖤 ❬**"


@iqthon.on(admin_cmd(outgoing=True, pattern="المده$"))
@iqthon.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(iqt):
    if iqt.fwd_from:
        return
    iqtid = await reply_id(iqt)
    iqtupt = await get_readable_time((time.time() - StartTime))
    if iqt_IMG:
        iqt_c += f"**{IMOGTHON} المـسـتـخـدم :** {mention}:   ٍَ❭\n"
        iqt_c += f"**{IMOGTHON} مـدة الـتـشغـيـل :** `{iqtupt}`:   ٍَ❭"
        await iqt.client.send_file(iqt.chat_id, iqt_IMG, caption=iqt_c, reply_to=iqtid)
        await iqt.delete()
    else:
        await edit_or_reply(
            iqt,
            f"**{IMOGTHON} المـسـتـخـدم :** {mention}:   ٍَ❭\n"
            f"**{IMOGTHON} مـدة الـتـشغـيـل :** `{iqtupt}`:   ٍَ❭",
        )
