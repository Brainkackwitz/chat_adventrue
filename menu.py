import time
import sys
from pygame import mixer
import os
import intro
import chat_adventure

mixer.init()

def menu(optionen):
    c = 0
    a = 1
    while c < a:
        os.system("cls")


    #mixer.music.load('intro.mp3')
    #mixer.music.play(0)
        try:
            for i, x in enumerate(optionen):
                print(f"{i+1}.", x)


            aktion = int(input('\nWähle deine Aktion '))
            if aktion == 1 :
                chat_adventure.game()
            if aktion == 2 :
                chat_adventure.load()
            if aktion == 3 :
                chat_adventure.optionen()

            if aktion == 4 :
                os._exit(1)
        except:

            print("ungülitige Antwort!")
            time.sleep(1)


if __name__ == '__main__':
    menu(['Start', 'Laden', 'Optionen', 'Exit'])
