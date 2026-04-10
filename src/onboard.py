from pyinputplus import inputStr,inputNum
from basictools import *
from os import makedirs
def config_file_creator():
    data=dict()

    #data['parameter']=input<fn>("Enter <parameter>: ",blank=False)

    folder_path=inputStr("Enter GigaBook-LM Path: ",blank=False)
    if if_file_exists(folder_path):
        pass
    else:
        makedirs(folder_path,exist_ok=True)

    llama_cpp_path=inputStr("Enter llama.cpp path: ",blank=False)
    if if_file_exists(llama_cpp_path):
        data['llama_cpp_path']=llama_cpp_path
    else:
        print(llama_cpp_path+" does not exist!")

    gguf_model_path=inputStr("Enter .GGUF model path: ",blank=False)
    if if_file_exists(gguf_model_path):
        data['gguf_model_path']=gguf_model_path
    else:
        print(gguf_model_path+" does not exist!")

    data["cw_size"]=inputInt("Enter Context Window Size [Refer your model's context window]: ",blank=True)

    temperature = inputNum("Enter Temperature [Click Enter for 0.7]: ",default = 0.7,blank=True,min=0.0,max=1.0)

	data["bot_name"]=inputStr("Enter Bot Name [Click Enter to leave it blank]: ",blank=True,default="GigaBook-LM")

	json_str=dumps(data,indent=4)
	with open(f"{folder_path}/config.json","w") as f:
	    f.write(json_str)
	print("Config folder and files have been created")

'''def return_onboard() -> dict: I'll come back to this.'''
