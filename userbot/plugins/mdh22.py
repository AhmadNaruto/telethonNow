import time
from userbot import iqthon


from . import StartTime, mention
from . import get_readable_time as grt

@iqthon.iq_cmd(
    pattern="مده$",
    command=("مده", plugin_category),
    info={
        "header": "مده",
        "options": "مده",
        "usage": [
            "{tr}مده",
        ],
    },
)
async def tim(kon):
    timethon = await grt((time.time() - StartTime))
    await eor(
        kon, f"⌔∮ مستخدم البوت : \n  - {mention} \n⌔∮ مدة تشغيل البوت : \n  - {timethon}"
    )
