from json import dumps, load
from os import makedirs, path
from pathlib import Path

from pyinputplus import inputInt, inputNum, inputStr

from basictools import *

folder_str = path.join(str(Path.home()), ".gigabook-lm")
filepath_str = path.join(folder_str, "config.json")


def config_file_creator():
    data = dict()
    # data['parameter']=input<fn>("Enter <parameter>: ",blank=False)

    gigabook_path = inputStr("Enter GigaBook-LM Path: ", blank=False)
    if not if_file_exists(gigabook_path):
        data["gigabook_path"] = gigabook_path
        makedirs(gigabook_path, exist_ok=True)

    llama_cpp_path = inputStr("Enter llama.cpp path: ", blank=False)
    if if_file_exists(llama_cpp_path):
        data["llama_cpp_path"] = llama_cpp_path
    else:
        print(llama_cpp_path + " does not exist!")

    gguf_model_path = inputStr("Enter .GGUF model path: ", blank=False)
    if if_file_exists(gguf_model_path):
        data["gguf_model_path"] = gguf_model_path
    else:
        print(gguf_model_path + " does not exist!")

    data["cw_size"] = inputInt(
        "Enter Context Window Size [Refer your model's context window]: ", blank=True
    )

    data["temperature"] = inputNum(
        "Enter Temperature [Click Enter for 0.7]: ",
        default=0.7,
        blank=True,
        min=0.0,
        max=1.0,
    )

    data["bot_name"] = inputStr(
        "Enter Bot Name [Click Enter to leave it blank]: ",
        blank=True,
        default="GigaBook-LM",
    )

    json_str = dumps(data, indent=4)

    makedirs(folder_str, exist_ok=True)

    with open(filepath_str, "w") as f:
        f.write(json_str)
    print("Config folder and files have been created")


def return_config():
    if if_file_exists(filepath_str):
        data = dict()
        with open(filepath_str, "r") as f:
            data = load(f)
        return data
    else:
        print("Creating config folder and files...")
        config_file_creator()
        return_config()
