import json
import os
import re
import shutil
import time
from asyncio import get_event_loop, sleep
from glob import glob
from re import findall
from urllib.error import HTTPError
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from emoji import get_emoji_regexp
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from requests import get
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo
from urbandict import define
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtube_search import YoutubeSearch
from userbot import iqthon
from userbot.utils.FastTelethon import upload_file



def get_video_thumb(file, output=None, width=320):
    output = file + ".jpg"
    metadata = extractMetadata(createParser(file))
    cmd = [
        "ffmpeg",
        "-i",
        file,
        "-ss",
        str(int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)),
        # '-filter:v', 'scale={}:-1'.format(width),
        "-vframes",
        "1",
        output,
    ]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    p.communicate()
    if not p.returncode and os.path.lexists(file):
        return output


def sortthings(contents, path):
    catsort = []
    contents.sort()
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isfile(catpath):
            catsort.append(file)
    for file in contents:
        catpath = os.path.join(path, file)
        if os.path.isdir(catpath):
            catsort.append(file)
    return catsort




@register(outgoing=True, pattern=r"^\.imdb (.*)")
async def imdb(e):
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = get("https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all")
        soup = BeautifulSoup(page.content, "lxml")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = get(mov_link)
        soup = BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "poster"):
            poster = soup.find("div", "poster").img["src"]
        else:
            poster = ""
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        mov_credits = soup.findAll("div", "credit_summary_item")
        if len(mov_credits) == 1:
            director = mov_credits[0].a.text
            writer = "Not available"
            stars = "Not available"
        elif len(mov_credits) > 2:
            director = mov_credits[0].a.text
            writer = mov_credits[1].a.text
            actors = []
            for x in mov_credits[2].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            director = mov_credits[0].a.text
            writer = "Not available"
            actors = []
            for x in mov_credits[1].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "Not available"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "Not available"
        await e.edit(
            "<a href=" + poster + ">&#8203;</a>"
            "<b>Title : </b><code>"
            + mov_title
            + "</code>\n<code>"
            + mov_details
            + "</code>\n<b>Rating : </b><code>"
            + mov_rating
            + "</code>\n<b>Country : </b><code>"
            + mov_country[0]
            + "</code>\n<b>Language : </b><code>"
            + mov_language[0]
            + "</code>\n<b>Director : </b><code>"
            + director
            + "</code>\n<b>Writer : </b><code>"
            + writer
            + "</code>\n<b>Stars : </b><code>"
            + stars
            + "</code>\n<b>IMDB Url : </b>"
            + mov_link
            + "\n<b>Story Line : </b>"
            + story_line,
            link_preview=True,
            parse_mode="HTML",
        )
    except IndexError:
        await e.edit("Plox enter **Valid movie name** kthx")




@register(outgoing=True, pattern=r"^\.yt (\d*) *(.*)")
async def yt_search(event):
    """For .yt command, do a YouTube search from Telegram."""

    if event.pattern_match.group(1) != "":
        counter = int(event.pattern_match.group(1))
        if counter > 10:
            counter = int(10)
        if counter <= 0:
            counter = int(1)
    else:
        counter = int(3)

    query = event.pattern_match.group(2)

    if not query:
        return await event.edit("`Enter a query to search.`")
    await event.edit("`Processing...`")

    try:
        results = json.loads(YoutubeSearch(query, max_results=counter).to_json())
    except KeyError:
        return await event.edit(
            "`Youtube Search gone retard.\nCan't search this query!`"
        )

    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n"

    for i in results["videos"]:
        try:
            title = i["title"]
            link = "https://youtube.com" + i["url_suffix"]
            channel = i["channel"]
            duration = i["duration"]
            views = i["views"]
            output += f"[{title}]({link})\nChannel: `{channel}`\nDuration: {duration} | {views}\n\n"
        except IndexError:
            break

    await event.edit(output, link_preview=False)


@register(outgoing=True, pattern=r".rip(audio|video( \d{0,4})?) (.*)")
async def download_video(v_url):
    """For .rip command, download media from YouTube and many other sites."""
    dl_type = v_url.pattern_match.group(1).lower()
    reso = v_url.pattern_match.group(2)
    reso = reso.strip() if reso else None
    url = v_url.pattern_match.group(3)

    await v_url.edit("`Preparing to download...`")
    s_time = time.time()
    video = False
    audio = False

    if "audio" in dl_type:
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": os.path.join(
                TEMP_DOWNLOAD_DIRECTORY, str(s_time), "%(title)s.%(ext)s"
            ),
            "quiet": True,
            "logtostderr": False,
        }
        audio = True

    elif "video" in dl_type:
        quality = (
            f"bestvideo[height<={reso}]+bestaudio/best[height<={reso}]"
            if reso
            else "bestvideo+bestaudio/best"
        )
        opts = {
            "format": quality,
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "outtmpl": os.path.join(
                TEMP_DOWNLOAD_DIRECTORY, str(s_time), "%(title)s.%(ext)s"
            ),
            "logtostderr": False,
            "quiet": True,
        }
        video = True

    try:
        await v_url.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await v_url.edit(f"`{str(DE)}`")
    except ContentTooShortError:
        return await v_url.edit("`The download content was too short.`")
    except GeoRestrictedError:
        return await v_url.edit(
            "`Video is not available from your geographic location "
            "due to geographic restrictions imposed by a website.`"
        )
    except MaxDownloadsReached:
        return await v_url.edit("`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await v_url.edit("`There was an error during post processing.`")
    except UnavailableVideoError:
        return await v_url.edit("`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await v_url.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await v_url.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await v_url.edit(f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    if audio:
        await v_url.edit(
            f"`Preparing to upload song:`\n**{rip_data.get('title')}**"
            f"\nby **{rip_data.get('uploader')}**"
        )
        f_name = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*.mp3"))[0]
        with open(f_name, "rb") as f:
            result = await upload_file(
                client=v_url.client,
                file=f,
                name=f_name,
                progress_callback=lambda d, t: get_event_loop().create_task(
                    progress(
                        d, t, v_url, c_time, "Uploading..", f"{rip_data['title']}.mp3"
                    )
                ),
            )

        thumb_image = [
            x
            for x in glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))
            if not x.endswith(".mp3")
        ][0]
        metadata = extractMetadata(createParser(f_name))
        duration = 0
        if metadata and metadata.has("duration"):
            duration = metadata.get("duration").seconds
        await v_url.client.send_file(
            v_url.chat_id,
            result,
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(
                    duration=duration,
                    title=rip_data.get("title"),
                    performer=rip_data.get("uploader"),
                )
            ],
            thumb=thumb_image,
        )
        await v_url.delete()
    elif video:
        await v_url.edit(
            f"`Preparing to upload video:`\n**{rip_data.get('title')}**"
            f"\nby **{rip_data.get('uploader')}**"
        )
        f_path = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))[0]
        # Noob way to convert from .mkv to .mp4
        if f_path.endswith(".mkv"):
            base = os.path.splitext(f_path)[0]
            os.rename(f_path, base + ".mp4")
            f_path = glob(os.path.join(TEMP_DOWNLOAD_DIRECTORY, str(s_time), "*"))[0]
        f_name = os.path.basename(f_path)
        with open(f_path, "rb") as f:
            result = await upload_file(
                client=v_url.client,
                file=f,
                name=f_name,
                progress_callback=lambda d, t: get_event_loop().create_task(
                    progress(d, t, v_url, c_time, "Uploading..", f_name)
                ),
            )
        thumb_image = await get_video_thumb(f_path, "thumb.png")
        metadata = extractMetadata(createParser(f_path))
        duration = 0
        width = 0
        height = 0
        if metadata:
            if metadata.has("duration"):
                duration = metadata.get("duration").seconds
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
        await v_url.client.send_file(
            v_url.chat_id,
            result,
            thumb=thumb_image,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    supports_streaming=True,
                )
            ],
            caption=f"[{rip_data.get('title')}]({url})",
        )
        os.remove(thumb_image)
        await v_url.delete()


def deEmojify(inputString):
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)
