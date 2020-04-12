import loading
import shutil
import glob, os
import loading

def save():
    try:
        os.chdir("F:\project's\pyhton\chat_adventrue\game\ingame")
        scoure = "F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\"
        target = "F:\\project's\\pyhton\\chat_adventrue\\game\\load\\"
        for file in glob.glob("*.ch"):

            shutil.copyfile(scoure+file, target+file)
    except:
        pass
