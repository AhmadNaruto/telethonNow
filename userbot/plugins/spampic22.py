import time
import threading

from re import sub
from telethon import events

from asyncio import wait, sleep

from userbot import iqthon


@iqthon.on(admin_cmd(pattern="سبام صور (?: |$)(.*)"))
async def spamfoto(e):
    arr = extract_args_arr(e)
    if len(arr) < 2 or not arr[0].isdigit():
        await e.edit("هناك خطا")
        return
    await e.delete()
    counter = int(arr[0])
    link = arr[1]
    for i in range(0, counter):
        await e.client.send_file(e.chat_id, link)
