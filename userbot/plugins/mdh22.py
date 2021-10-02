import time
from userbot import iqthon


from . import StartTime, mention
from . import get_readable_time as grt

@iqthon.on(
    iqthon_cmd(
       pattern="مده", outgoing=True
    )
)
@iqthon.on(
    sudo_cmd(
       pattern="مده", allow_sudo=True
    )
)
async def tim(kon):
    timethon = await grt((time.time() - StartTime))
    await eor(
        kon, f"⌔∮ مستخدم البوت : \n  - {mention} \n⌔∮ مدة تشغيل البوت : \n  - {timethon}"
    )
