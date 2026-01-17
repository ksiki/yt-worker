from ytworker.errors.invalid_link_error import InvalidLinkError
from ytworker.errors.unknown_command_error import UnknownCommand
from ytworker.tools import downloader


def run_command(command: str, **kwargs) -> str:
    match command:
        case "vid-dwnl":
            return download_video(**kwargs)
        case "playlist-dwnl":
            return download_playlist(**kwargs)
        case "vid-info":
            return info_video(**kwargs)
        case _:
            raise UnknownCommand


def download_video(link: str, indir: str, name: str = "") -> str:
    try:
        downloader.download_video(link, indir, name)
        return "The video was uploaded successfully."
    except InvalidLinkError:
        return "Invalid link"
    

def download_playlist(link: str, indir: str, folder_name: str = "") -> str:
    try:
        downloader.download_playlist(link, indir, folder_name) 
        return "The playlist was uploaded successfully."
    except InvalidLinkError:
        return "Invalid link"
    

def info_video(link: str, short: bool = False) -> str:
    return "Pass"