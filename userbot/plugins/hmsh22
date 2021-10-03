from . import reply_id as rd


@iqthon.on(
    iqthon_cmd(pattern="همسه ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    hms = event.pattern_match.group(1)
    knox = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(knox, hms) 
    await tap[0].click(event.chat_id)
    await event.delete()
