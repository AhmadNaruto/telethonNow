from userbot import iqthon

@iqthon.on(admin_cmd(pattern="جلب الصورة"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("**⌔︙ يجـب عـليك الـرد عـلى صـورة ذاتيـة الـتدمير**")
    kno = await event.get_reply_message()
    pic = await kno.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
**⌔︙ تـم جـلب الصـورة بنجـاح ✅
- CH: @IQTHON**
  """,
    )
    await event.delete()
