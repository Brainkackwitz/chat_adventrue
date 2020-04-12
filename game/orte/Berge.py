import time
import sys
from pygame import mixer
import os
import random
mixer.init()
def delay_print(s):

    for c in s:
        mixer.music.load("F:\\project's\\pyhton\\chat_adventrue\\game\\sounds\\text.mp3")
        f = open("F:\\project's\\pyhton\\chat_adventrue\\game\\sounds\\settings.txt","r")
        mixer.music.set_volume(int(f.readline()[-3:-1])/100)
        f.close()
        mixer.music.play(0)
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    mixer.music.stop()
mixer.music.load("F:\\project's\\pyhton\\chat_adventrue\\game\\sounds\\berge.mp3")
f = open("F:\\project's\\pyhton\\chat_adventrue\\game\\sounds\\settings.txt","r")
mixer.music.set_volume(int(f.readline()[-3:-1])/100)
f.close()
mixer.music.play(0)
def luck(Name, type, hp, atk, deff, inv):
    global l
    if type == "Basilisk" or type == "Riese":
        l = 1.1
    if type == "Goblin":
        l = 2
    if type == "Werwolf" or type == "Mensch" or type == "Elf":
        l = 1
    if type == "Fee":
        l = 3
    if inv > 10:
        l = l+1


def start(Name, type, hp, atk, deff, inv):
    os.system("cls")
    c = 0
    a = 1
    delay_print("Du bist auf der Suche nach deiem Kindheits Freund\num ihm nach etwas Geld zu bitten.\nMomentan befindetest du dich im Wald vor der der Stadt\nin dem dein Kindheitsfreund Lebt")
    while c < a:
        try:
            delay_print("\n\033[1;35;40mDu bist Hungrig ")
            print("\033[0;37;40m\nOptionen:\n")
            optionen = (['Du Läuft die nächste Stunde zur Stadt', 'Ich versuche per Anhalter zu Stadt zu kommen'])
            for i, x in enumerate(optionen):
                print(f"{i+1}.", x)
            aktion = int(input("Wähle deine Aktion "))

            if aktion == 1 and type != "Riese":
                delay_print("Nach eta einer Stunde stehst du an den Toren der Stadt")
                break
            if aktion == 1 and type == "Riese":
                delay_print("Du brauchtest keine Stunde, was der Fischer gesagt hat da du ein "+type+" bist.")
                break
            if aktion == 2:


                f = 1
                luck(Name, type, hp, atk, deff, inv)
                u = 60/(f - l)
                d = u-20
                b = u+20
                t = random.randrange(d, b, 5)
                print("Weil dich ein Abendteuer mit genommen hat, hast du "+t+" Minuten gebraucht")
                if t < 50:
                    print("er hat dir was zu esse gegeben")
                break
        except:
            os.system("cls")
            continue
start("Name", "Riese", 10, 10, 10, 15)


def Berge(Name, type):

    os.system("cls")
    delay_print("Guck mal einer an aus dem Geschlecht der "+type+"!\n")
    delay_print("Du wachst benommen in einem Bett auf.\n")
    delay_print("Du sieht einen Zwerg.")


    print("\nOptionen:\n")
    optionen = (['Du fragst dich wo du bist', 'Wer ist der Zwerg', 'Warum bin ich so nass?'])
    for i, x in enumerate(optionen):
        print(f"{i+1}.", x)

    aktion = int(input())
    if aktion == 1 :
        delay_print("Du bist in meiner Kneipe die ich schon seit 117 Jahren betreibe.\n")
        delay_print("Man sieht deutlich das Sie ein " +type+ " sind.\nDeshalb muss ich fragen ob auch ein Abendteuer sind.\n\n")
        optionen = (['Ja, ich übe den Beruf erst seit kurzem aus', 'Nein was macht ein Abendteuer'])
        for i, x in enumerate(optionen):
            print(f"{i+1}.", x)

        aktion = int(input())
        if aktion == 1:
            delay_print("a.ah das habe ich mir gleich gedacht.\n In meiner Kneipe gibt es einige QUEST auf dem Schwarzenbrett.")


        if aktion == 2:
            delay_print("Ein Abendteuer sucht wie der Name schon sagt nach den Reizen des Lebens.\nJede Nacht und Jeden Tag zu spüren das man Lebt.\nDazu Nehmen sie Aufgaben sogenannte QUEST an und damit verdienen sie auch ihr Geld.")
            delay_print("Ich dachte nur wer so aussieht muss schon mit Monstern gekämpft haben.")


    if aktion == 2 :
        delay_print("ich.. Na Allbrecht, aber du kennst mich doch, "+Name+"!")
        delay_print("hatt der Stutz dein Gedächnis geraubt?")

    if aktion == 3 :
        delay_print("Ich habe dich aus dem Jogong Fluss nahe der Hauptstadt erraus gezogen")
        delay_print("Wie heißt du mein Freund?")

#Berge("Name", "type")
