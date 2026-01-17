def format_path_to_dir(path: str) -> str:
    if not path.endswith("/"):
        path += "/"

    return path