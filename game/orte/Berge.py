import time
import sys
from pygame import mixer
import os
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

            if aktion == 1 && type == "Mensch" or type == "":
                delay_print("Nach eta einer Stunde stehst du an den Toren der Stadt")



            if aktion == 2:
                if type ==
        except:
            continue
start()


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
