def link_validate(link: str) -> bool:
    if not link.startswith("https://www.youtube.com/"):
        return False
    return True


def path_to_dir_validate(path: str) -> bool:
    if not path.endswith("/"):
        return False
    return True