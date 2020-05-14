# import des modules
import time
import clipboard
import keyboard
import configparser
from configparser import RawConfigParser

def auto_command():
    try:
        with open('commands.txt') and open('times.ini'):
            file_exist()
    except IOError:
        print("Erreur fichier(s) manquant")
        time.sleep(1)
        create_file()

def command_file_exist():
    try:
        with open('commands.txt'):
            print('le fichier commands.txt existe déjà')
    except IOError:

        print("Création du fichier commands.txt")
        time.sleep(1.5)
        commands_file = open("commands.txt", 'w', encoding="utf-8")
        commands_file.close()


# fonction qui va récupéré les commandes une par une et va simuler le "ctrl + v" et la touche "Entrer" pour les coller et entrer dans la console
def allcommand(time_wait, time_wait_items, commands):
    print("------------------------AUTO-COMMAND Scum V1------------------------\n")
    print("Démarrage dans",time_wait,"secondes...")
    time.sleep(float(time_wait))
    print("----------------Démarrage------------------")
    for value in commands:
        print("give de l'item :", value)
        keyboard.write(value)
        time.sleep(float(time_wait_items))
        keyboard.press_and_release('enter')
    print("------------------FIN---------------------")

# On creer les fichiers si ils existent
def create_file():
    try:
        with open('times.ini'):
            print("le fichier times.ini existe déjà")
    except IOError:
        print("Création du fichier times.ini")
        time.sleep(1)
        #création du fichier de configuration
        config = configparser.RawConfigParser()
        config['TIME'] = {'time_items': '12','time_wait_items': '0.8'}
        with open('times.ini', 'w') as configfile:
            config.write(configfile)
        program_continue = True
        program_execute = input("Les fichiers ont été créer. Voulez-vous exécuter le programme tout de suite? [oui/non] : ")
        while program_continue:
            if program_execute == "oui":
                auto_command()
                program_continue = False
            elif program_execute == "non":
                print("A bientôt !")
                program_continue = False
            else:
                program_execute = input("Je n'ai pas compris votre réponse. Voulez vous poursuivre ? taper \"oui\" ou \"non\" : ")
                program_continue = True

def file_exist():
    commands_file = open("commands.txt", 'r', encoding="utf-8")
    commands = commands_file.read().splitlines()
    commands_file.close()
    # Chargement de la configuration
    config = RawConfigParser()
    load_ini = open('times.ini', 'r', encoding='utf-8')
    config.read_file(load_ini)
    config = dict(config['TIME'])
    load_ini.close()
    time_wait = config['time_items']
    time_wait_items = config['time_wait_items']
    allcommand(time_wait, time_wait_items, commands)

auto_command()
