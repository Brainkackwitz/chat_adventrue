import os
import glob
import shutil


os.chdir("F:\project's\pyhton\chat_adventrue\game\load")
scoure = "F:\\project's\\pyhton\\chat_adventrue\\game\\load\\"
target = "F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\"


for file in glob.glob("*.ch"):
    shutil.copyfile(scoure+file, target+file)
