import save
import sys
def menu():
    c=0
    a=1
    while c < a:
        optionen = (['weiter', 'Speichern', 'exit'])
        for i, x in enumerate(optionen):
            print(f"{i+1}.", x)
        aktion = int(input('\nWähle deine Aktion '))
        if aktion == 1:
            break
        if aktion == 2:
            save.save()
            break
        if aktion == 3:
            os._exit(1)
menu()
