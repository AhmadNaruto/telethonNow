import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "iqthonbot"
iqthon_IMG = "https://telegra.ph/file/ca2467e77ffcd605cc54d.jpg"
iqthonS_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝐒𝐎𝐔𝐑𝐂𝐄 𓆪"
iqthonEM = "**⌔︙**"


@iqthon.on(admin_cmd(outgoing=True, pattern="المده$"))
@iqthon.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(iqthon):
    if iqthon.fwd_from:
        return
    iqthonid = await reply_id(iqthon)
    iqthonupt = await get_readable_time((time.time() - StartTime))
    if iqthon_IMG:
        iqthon_c = f"**{iqthonS_TEXT}**\n"
        iqthon_c += f"**{iqthonEM} المستخدم :** {mention}\n"
        iqthon_c += f"**{iqthonEM} مدة التشغيل :** `{iqthonupt}`"
        await iqthon.client.send_file(iqthon.chat_id, iqthon_IMG, caption=iqthon_c, reply_to=iqthonid)
        await iqthon.delete()
    else:
        await edit_or_reply(
            iqthon,
            f"**{iqthonS_TEXT}**\n\n"
            f"**{iqthonEM} المستخدم :** {mention}\n"
            f"**{iqthonEM} مدة التشغيل :** `{iqthonupt}`",
        )
