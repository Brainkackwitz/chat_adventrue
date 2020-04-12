import time
import sys
from pygame import mixer
import os
import intro , menu

from game.orte import Berge
import loading
import save



mixer.init()
s = "F:\\project's\\pyhton\\chat_adventrue\\game\\sounds\\settings.txt"
def delay_print(s):

    for c in s:
        mixer.music.load('game/sounds/text.mp3')
        f = open(s,"r")
        mixer.music.set_volume(int(f.readline()[-3:-1])/100)
        f.close()
        mixer.music.play(0)
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    mixer.music.stop()

def game():
    loading.loading1()
    time.sleep(0.5)
    intro.start()


def orte(Name, type, hp, atk, deff, inv, orte):
    loading.gameload("", "", "", "", "", "", orte)
    if orte == "Berge":
        #Berge.Berge(Name, type)
        Berge.start(Name, type, hp, atk, deff, inv)

def load():
    loading.loading()
    loading.loadcopy()
def optionen():

    os.system("cls")
    for i, x in enumerate(['Volume', 'Credis', 'Zurück']):
        print(f"{i+1}.", x)
    aktion = int(input('\nWähle deine Aktion '))
    if aktion == 1:

        f = open(s,"r")
        print(f.readline())
        f.close()
        i = int(input())
        f = open(s,"w")

        print("volume = "+str(i))
        f.write("volume = "+str(i)+" ")
        f.close()
        time.sleep(1)
        optionen()
    if aktion == 2:
        os.system("cls")
        delay_print("This game is developed by Brainkackwitz")
        time.sleep(1)
        optionen()
    if aktion == 3:
        menu.menu(['Start', 'Laden', 'Optionen', 'Exit'])

#loading.loading()

if __name__ == '__main__':
    menu.menu(['Start', 'Laden', 'Optionen', 'Exit'])
