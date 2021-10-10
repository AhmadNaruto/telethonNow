import random
import re
import time
from platform import python_version

from telethon import version
from telethon import Button, types, version
from telethon.errors import QueryIdInvalidError
from telethon.events import CallbackQuery, InlineQuery

from userbot import StartTime, iqthon
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention



@iqthon.on(admin_cmd(pattern="lists(?: |$)(.*)"))
async def order(event):
    reply_to_id = await reply_id(event)
    the_description = "Welcome to my list"
    IMG_list = gvarstatus("ALIVE_PIC")
    list1 = "test 1"
    list2 = "test2"
    list3 = "test3"
    alive_buttons = [
                [
                    Button.inline(
                        "TEXT", data=list1"
                    ),
                ],
                [
                    Button.inline(
                        text=f" التيليثون "
                    ),
                ],
                [
                    Button.inline(
                        text=f" الوقت"
                    ),
                ],
                [   
                    Button.url("رابط السورس", "https://github.com/klanrali/Telethon-Arab"
                    ),
                ],
                [   
                    Button.inline(
                        text=f" المالك "
                    ),
                ],
            ]
            await event.answer([
                builder.article(
                    title="Ialive", 
                    description="list MSG", 
                    text=the_description, 
                    thumb=InputWebDocument(url=IMG_list, size=42, mime_type="image/jpeg", attributes=[]) if IMG_list else None, 
                    buttons=alive_buttons, 
                    parse_mode="md"
                ),
            ])
                 
                    
                
           
