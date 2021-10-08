import os

import moviepy.editor as m

from userbot import iqthon

@iqthon.on(admin_cmd(pattern="تخزين الصوت(?: |$)(.*)"))
async def iq(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("**قم برد على الصوت بشرط ان يكون الامتداد mp3 وليس بصمه**")
        return
    await event.edit("**جاري تخزين الصوت**")
    d = os.path.join("SQL/extras", "iq.mp3")
    await event.edit("**جارٍ التنزيل ... الملفات الكبيرة تستغرق وقتًا ..**")
    await event.client.download_media(ureply, d)
    await event.edit("**تم .. الآن قم بالرد على الفيديو الذي تريد إضافة هذا الصوت فيه بالأمر :** `.اضف الصوت`")

@iqthon.on(admin_cmd(pattern="اضف الصوت(?: |$)(.*)"))
async def iq(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("**قم بالرد على متحركه او فيديو الذي تريد إضافة الصوت فيه.**")
        return
    xx = await event.edit("**جاي اضافه الصوت**")
    ultt = await ureply.download_media()
    ls = os.listdir("SQL/extras")
    z = "iq.mp3"
    x = "SQL/extras/iq.mp3"
    if z not in ls:
        await event.edit("**قم بالرد أولاً بصوت بامتداد mp3 فقط**")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("L5.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="L5.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    os.remove("L5.mp4")
    os.remove(x)
    os.remove(ultt)
    await xx.delete()
