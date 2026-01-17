PROGRAM_NAME = "yt-tools"
COMMANDS_CONFIGURATION: dict[str, dict[str, dict]] = {
    "vid-dwnl": {
        "link": {
            "type": str,
            "help": "link on video"
        },
        "indir": {
            "type": str,
            "help": "path to dir for save video"
        },
        "--name": {
            "type": str,
            "required": False,
            "default": "",
            "help": "name for the saved video"
        }
    },
    "playlist-dwnl": {
        "link": {
            "type": str,
            "help": "link on video"
        },
        "indir": {
            "type": str,
            "help": "path to dir for save video"
        },
        "--folder_name": {
            "type": str,
            "required": False,
            "default": "",
            "help": "name dir for save video"
        }
    },
    "vid-info": {
        "link": {
            "type": str,
            "help": "link on video"
        },
        "--short": {
            "required": False,
            "action": "store_true",
            "help": "short info about video ('channel name', 'title', 'description', 'publish date')"
        }
    }
}
