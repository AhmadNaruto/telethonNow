import asyncio
import base64
import os
import shutil
import requests
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import AUTONAME, DEFAULT_BIO, edit_delete, iqthon, logging

plugin_category = "tools"

DEFAULTUSERBIO = DEFAULT_BIO or "تيست"
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)
autopic_path = os.path.join(os.getcwd(), "userbot", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "userbot", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "userbot", "photo_pfp.png")
digitalpfp = Config.DIGITAL_PIC
klanr = Config.TM_IQTHON or ""


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("صوره وقتي") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        kno = str(base64.b64decode("dXNlcmJvdC9oZWxwZXJzL3N0eWxlcy9kaWdpdGFsLnR0Zg=="))[2:36]
        fnt = ImageFont.truetype(kno, 65)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(280, 280, 280))
        img.save(autophoto_path)
        file = await iqthon.upload_file(autophoto_path)
        try:
            if i > 0:
                await iqthon(
                    functions.photos.DeletePhotosRequest(
                        await iqthon.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await iqthon(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("صوره وقتي") == "true"


async def autoname_loop():
    AUTONAMESTART = gvarstatus("اسم الوقت") == "true"
    while AUTONAMESTART:
        time.strftime("%d.%m.%Y")
        qI = time.strftime("%I:%M")
        go = requests.get(f"https://laksis3mk.000webhostapp.com/zl.php?text={qI}").json()['newText']
        name = f"{klanr} {go} "
        LOGS.info(name)
        try:
            await iqthon(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("اسم الوقت") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("وقت البايو") == "true"
    while AUTOBIOSTART:
        time.strftime("%d.%m.%Y")
        bi = time.strftime("%I:%M")
        ni = requests.get(f"https://laksis3mk.000webhostapp.com/zl.php?text={bi}").json()['newText']
        bio = f"{DEFAULTUSERBIO} {ni}"
        LOGS.info(bio)
        try:
            await iqthon(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("وقت البايو") == "true"


@iqthon.iq_cmd(
    pattern="الصورة الوقتية$",
    command=("الصورة الوقتية", plugin_category),
)
async def _(event):
    "To set random colour pic with time to profile pic"
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("صوره وقتي") is not None and gvarstatus("صوره وقتي") == "true":
        return await edit_delete(event, "**الصـورة الـوقتية شغـالة بالأصـل **")
    addgvar("صوره وقتي", True)
    await edit_delete(event, "**تم تفـعيل الصـورة الـوقتية بنجـاح **")
    await digitalpicloop()


@iqthon.iq_cmd(
    pattern="اسم وقتي$",
    command=("اسم وقتي", plugin_category),
)
async def _(event):
    "To set your display name along with time"
    if gvarstatus("اسم الوقت") is not None and gvarstatus("اسم الوقت") == "true":
        return await edit_delete(event, "**الاسـم الـوقتي شغـال بالأصـل **")
    addgvar("اسم الوقت", True)
    await edit_delete(event, "**تم تفـعيل الاسـم الـوقتي بنجـاح **")
    await autoname_loop()


@iqthon.iq_cmd(
    pattern="بايو وقتي$",
    command=("بايو وقتي", plugin_category),
)
async def _(event):
    "To update your bio along with time"
    if gvarstatus("وقت البايو") is not None and gvarstatus("وقت البايو") == "true":
        return await edit_delete(event, "**الـبايو الـوقتي شغـال بالأصـل **")
    addgvar("وقت البايو", True)
    await edit_delete(event, "**تم تفـعيل البـايو الـوقتي بنجـاح**")
    await autobio_loop()


@iqthon.iq_cmd(
    pattern="انهاء ([\s\S]*)",
    command=("انهاء", plugin_category),
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "الصورة الوقتية":
        if gvarstatus("صوره وقتي") is not None and gvarstatus("صوره وقتي") == "true":
            delgvar("صوره وقتي")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**تم ايقاف الصورة الوقتية بنـجاح **")
        return await edit_delete(event, "**لم يتم تفعيل الصورة الوقتية بالأصل **")
    if input_str == "اسم وقتي":
        if gvarstatus("اسم الوقت") is not None and gvarstatus("اسم الوقت") == "true":
            delgvar("اسم الوقت")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**تم ايقاف  الاسم الوقتي بنـجاح **")
        return await edit_delete(event, "**لم يتم تفعيل الاسم الوقتي بالأصل **")
    if input_str == "بايو وقتي":
        if gvarstatus("وقت البايو") is not None and gvarstatus("وقت البايو") == "true":
            delgvar("وقت البايو")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**  تم ايقاف البايو الوقـتي بنـجاح **")
        return await edit_delete(event, "**لم يتم تفعيل البايو الوقتي **")
    auto_iqthon = [
        "الصورة الوقتية",
        "اسم وقتي",
        "بايو وقتي",
    ]
    if input_str not in auto_iqthon:
        await edit_delete(
            event,
            f"عـذرا يجـب استـخدام الامـر بشـكل صحـيح ",
            parse_mode=_format.parse_pre,
        )


iqthon.loop.create_task(digitalpicloop())
iqthon.loop.create_task(autoname_loop())
iqthon.loop.create_task(autobio_loop())
