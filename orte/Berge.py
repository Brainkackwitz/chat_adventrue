import time
import sys
from pygame import mixer
import os
def delay_print(s):

    for c in s:

        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
mixer.init()
def Berge(Name, type):
    mixer.music.load("F:\\project's\\pyhton\\chat_adventrue\\sounds\\berge.mp3")
    f = open("F:\\project's\\pyhton\\chat_adventrue\\sounds\\settings.txt","r")
    mixer.music.set_volume(int(f.readline()[-3:-1])/100)
    f.close()
    mixer.music.play(0)
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
