from datetime import datetime
from hashlib import sha256
from os import path
from pathlib import Path
from socket import create_connection
from datetime import datetime

def if_file_exists(filepath_str):
    if path.exists(filepath_str):
        return True
    else:
        return False


def is_connected_to_internet():
    try:
        create_connection(("1.1.1.1", 53), timeout=10)
        return True
    except OSError:
        pass
    return False


def strip_md(text):
    text = text.replace("#", "")
    text = text.replace("##", "")
    text = text.replace("###", "")
    text = text.replace("**", "")
    text = text.replace("*", "")
    text = text.replace("---", "\n")
    return text


def logger(message):
    return f"[{datetime.now().strftime('%H:%M:%S')}] " + message


def hasher(filepath):
    with open(filepath, "rb") as f:
        bytes = f.read()
        return sha256(bytes).hexdigest()


def remember_Me(file):
    folder_str = path.join(str(Path.home()), ".gigabook-lm")
    filepath_str = path.join(folder_str, "gatekeep.bin")
    if if_file_exists(filepath_str):
        with open(filepath_str, "rb") as f:
            files = pickle.load(f)
            if hasher(file) in files:
                return True
            else:
                f.seek(0)
                f.truncate()
                files.append(hasher(file))
                pickle.dump(files, f)
    else:
        l = []
        l.append(hasher(file))
        with open(filepath_str, "wb") as f:
            pickle.dump(l, f)
