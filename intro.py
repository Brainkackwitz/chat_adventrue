import time
import sys
from pygame import mixer
import os
import chat_adventure, loading
import random
def delay_print(s):

    for c in s:
        mixer.music.load("F:\\project's\\pyhton\\chat_adventrue\\sounds\\text.mp3")
        f = open("F:\\project's\\pyhton\\chat_adventrue\\sounds\\settings.txt","r")
        mixer.music.set_volume(int(f.readline()[-3:-1])/100)
        f.close()
        mixer.music.play(0)
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    mixer.music.stop()
mixer.init()

def start():
    os.system("cls")
    delay_print("DU MUSST DIESEN TEST ERLICH UND MIT BESTEM GEWISSEN VOLLZIEHEN!\n")
    time.sleep(1)
    c = 0
    a = 1


    delay_print("Welche Klasse/Rasse entspringst du?\n\n")
    optionen = (['Goblin', 'Riese', 'Tierwesen', 'Mensch', 'Fee', 'Elf'])
    for i, x in enumerate(optionen):
        time.sleep(0.4)
        print(f"{i+1}.", x)
    time.sleep(0.8)
    while c < a:
        try:
            aktion = int(input('Wähle deine Aktion '))
            if aktion == 1:
                type = optionen[0]
                break
            if aktion == 2:
                type = optionen[1]
                break
            if aktion == 3:
                type = optionen[2]


                os.system("cls")
                delay_print("Was für ein Tierwesen bist du?\n\n")
                optionen = (['Werwolf', 'Basilisk'])
                for i, x in enumerate(optionen):
                        time.sleep(0.4)
                        print(f"{i+1}.", x)
                time.sleep(0.8)
                while c < a:
                    try:
                        aktion = int(input('Wähle deine Aktion '))
                        if aktion == 1:
                            type = optionen[0]
                            break
                        if aktion == 2:
                            type = optionen[1]
                            break
                    except:
                        os.system("cls")
                        print("Was für ein Tierwesen bist du?\n")
                        optionen = (['Werwolf', 'Basilisk'])
                        for i, x in enumerate(optionen):
                                print(f"{i+1}.", x)
                        continue
            if aktion == 4:
                type = optionen[3]
                break
            if aktion == 5:
                type = optionen[4]
                break
            if aktion == 6:
                type = optionen[5]
                break
        except:
                print("ungülitige Antwort!")
                time.sleep(1)
                os.system("cls")
                print("DU MUSST DIESEN TEST ERLICH UND MIT BESTEM GEWISSEN VOLLZIEHEN!")
                print("Welche Klasse/Rasse entspringst du?\n")
                optionen = (['Troll', 'Riese', 'Tierwesen', 'Mensch', 'Fee', 'Elf'])
                for i, x in enumerate(optionen):
                    print(f"{i+1}.", x)
                continue
    while c < a:
            Name = str(input('\nWähle deinen Namen: '))
            if len(Name) > 1:
                break
            else:
                print("ungülitige Antwort!")
                time.sleep(1)
                os.system("cls")
                print("DU MUSST DIESEN TEST ERLICH UND MIT BESTEM GEWISSEN VOLLZIEHEN!")
                continue
    f = 0.2
    while c < a:
        try:
            os.system("cls")
            print("Das sind deine Gewürfelten stats\n")

            stats = {"hp":'10', "atk":'10',"deff":'10', "inv":'10'}

            b = random.randint(5,f*50)

            stats["atk"]= random.randint(5,f*100-b)

            stats["deff"] = random.randint(5,f*150-(stats["atk"]+b))

            stats["inv"] = random.randint(5,f*200-(stats["deff"]+stats["atk"]+b))
            stats["hp"] = random.randint(5, f*200-(stats["deff"]+stats["atk"]+stats["inv"]))
            print("HP: ", stats["hp"])
            print("Atk", stats["atk"])
            print("Deff", stats["deff"])
            print("Inv", stats["inv"])
            print()
            optionen = (['Neu Würfeln', 'Stats Übernehmen', 'Faktor ändern'])
            for i, x in enumerate(optionen):
                print(f"{i+1}.", x)
            aktion = int(input('\nWähle deine Aktion '))


            if aktion == 1:
                continue
            if aktion == 2:
                #f = open("F:\project's\pyhton\chat_adventrue\load\game.txt","w")
                #f.write("Name\n"+Name+"\ntype\n"+type+"\nHP\n"+str(stats["hp"])+"\nAtk\n"+str(stats["atk"])+"\nDeff\n"+str(stats["deff"])+"\nInv\n"+str(stats["inv"])+"\n")
                loading.gameload(Name, type, str(stats["hp"]),str(stats["atk"]), str(stats["deff"]), str(stats["inv"]), "")






                break
            if aktion == 3:
                f = float(input('\nWähle deinen Faktor über 0: '))
                if f > 0:
                    continue
                else:
                    print("ungülitige Antwort!")
                    time.sleep(1)
                    os.system("cls")
                    continue

            #max = 200
            #for i in range(4):
                #print(random.randrange(0, 101, 5))

            #if hp+atk+def+inv > max:
                #continue



        except:
            print("ungülitige Antwort!")
            time.sleep(1)
            os.system("cls")
            continue

    while c < a:
        os.system("cls")
        print('\nWeißt du wo du bist?')
        print("\nOptionen:\n")
        optionen = (['Ich bin in den Bergen', 'Ich wollte ich die Landeshauptstadt', 'Ich habe mich verlaufen'])
        try:
            for i, x in enumerate(optionen):
                print(f"{i+1}.", x)



            aktion = int(input('\nWähle deine Aktion '))

            if aktion == 1 :
                chat_adventure.orte(Name, type, "Berge")

            if aktion == 2 :

                chat_adventure.load()
            if aktion == 3 :

                chat_adventure.orte(Name, type, orte)

            if aktion == 4 :
                os._exit(1)
        except:
            print("ungülitige Antwort!")
            time.sleep(1)

if __name__ == '__main__':
    start()
