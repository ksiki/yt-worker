from ytworker.errors.invalid_link_error import InvalidLinkError
from ytworker.tools import validator
from yt_dlp import YoutubeDL 

import ytworker.tools.formatter as formatter


def download_video(link: str, indir: str, name: str = ""):
    if not validator.link_validate(link):
        raise InvalidLinkError
    if name == "":
        name = "%(title)s"
    if not validator.path_to_dir_validate(indir):
        indir = formatter.format_path_to_dir(indir)

    ydl_opts = {               
        "merge_output_format": "mp4",         
        "outtmpl": indir + name + ".%(ext)s"
    }
    download(link, ydl_opts)


def download_playlist(link: str, indir: str, folder_name: str = ""):
    if not validator.link_validate(link):
        raise InvalidLinkError
    if not validator.path_to_dir_validate(indir):
        indir = formatter.format_path_to_dir(indir)
    if folder_name != "":
        indir += folder_name

    ydl_opts = {                
        "merge_output_format": "mp4",         
        "outtmpl": indir + "%(title)s" + ".%(ext)s"
    }
    download(link, ydl_opts)


def download(link: str, ydl_opts: dict[str, str]):
    with YoutubeDL(ydl_opts) as ydl:  # pyright: ignore[reportArgumentType]
        ydl.download(link)
