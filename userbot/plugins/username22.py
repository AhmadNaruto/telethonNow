from math import sqrt

from telethon import functions


from userbot import iqthon



@iqthon.on(admin_cmd(pattern="userid(?: |$)(.*)"))
async def useridgetter(target):
    """For .userid command, returns the ID of the target user."""
    message = await target.get_reply_message()
    if message:
        if not message.forward:
            user_id = message.sender.id
            if message.sender.username:
                name = "@" + message.sender.username
            else:
                name = "**" + message.sender.first_name + "**"
        else:
            user_id = message.forward.sender.id
            if message.forward.sender.username:
                name = "@" + message.forward.sender.username
            else:
                name = "*" + message.forward.sender.first_name + "*"
        await target.edit(f"**المعرف :** {name}")
