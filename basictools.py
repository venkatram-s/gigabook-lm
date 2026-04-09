from os import path
from socket import create_connection
from datetime import datetime
from hashlib import new,update,
def if_file_exists(filepath_str):
    if (path.exists(filepath_str)):
        return True
    else:
        return False

def is_connected_to_internet():
    try:
        create_connection(('1.1.1.1', 53),timeout=10)
        return True
    except OSError:
        pass
    return False

def strip_md(text):
  text=text.replace('#','')
  text=text.replace('##','')
  text=text.replace('###','')
  text=text.replace('**','')
  text=text.replace('*','')
  text=text.replace('---','\n')
  return text

def logger(message):
    return F'[datetime.now().strftime("%H:%M:%S")] '+message

def hasher():


def remember_Me(file):
    try:
        with open('gatekeep.bin','rb+') as f:
            files=pickle.load(f)
            if hasher(file) in files:
                return True
            else:
                f.seek(0)
                f.truncate()
                files.append(hasher(file))
                pickle.dump(files,f)
    except FileNotFoundError:
        l=[]
        l.append(file)
        with open('gatekeep.bin','ab+') as f:
            pickle.dump(l,f)
