from tqdm import tqdm
from tqdm.auto import tqdm
import os
import glob
import shutil
import time
import chat_adventure
def loading():
    os.system("cls")
    loop = tqdm(total = 5000, position=0, leave=False)
    for k in range(5000):
        loop.set_description("Loading...".format(k))
        loop.update(1)
    loop.close()
def loading1():
    os.system("cls")
    for i in tqdm(range(10001)):
        print(" ", end='\r')
def loadcopy():
    a = []
    b = []
    i= 0
    os.chdir("F:\project's\pyhton\chat_adventrue\game\load")
    scoure = "F:\\project's\\pyhton\\chat_adventrue\\game\\load\\"
    target = "F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\"


    try:
            for file in glob.glob("*.ch"):
                os.remove(target+file)
    except:
        pass
    finally:
            for file in glob.glob("*.ch"):
                a.append(file)
                shutil.copyfile(scoure+file, target+file)

            for x in a:
                y = open(scoure+x)
                b.append(y.readline())

            chat_adventure.orte(b[0], b[1], b[6])

def gameload(Name, type, hp, atk, deff, inv, orte):
    if len(Name) > 0:
        n = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\1cname.ch", "w")
        n.write(Name)
        n.close()
    if len(type) > 0:
        n = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\2ctype.ch", "w")
        n.write(type)
        n.close()
    if len(hp) > 0:
        h = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\3chp.ch", "w")
        h.write(hp)
        h.close()
    if len(atk) > 0:
        a = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\4catk.ch", "w")
        a.write(atk)
        a.close()
    if len(deff) > 0:
        d = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\5cdeff.ch", "w")
        d.write(deff)
        d.close()
    if len(inv) > 0:
        i = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\6cinv.ch", "w")
        i.write(inv)
        i.close()
    if len(orte) >0:
        o = open("F:\\project's\\pyhton\\chat_adventrue\\game\\ingame\\7corte.ch", "w")
        o.write(orte)
        o.close()
