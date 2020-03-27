# import des modules
import time
import clipboard
import keyboard

# liste de toutes les commandes
command = ["#spawnitem Baseball_Cap_01","#spawnitem Pilot_Glasses","#spawnitem StabProof_Vest_04","#spawnitem Backpack_02_01","#spawnitem Military_Shirt_06","#spawnitem Open_Finger_Gloves_01","#spawnitem Waist_Bag_Small_02","#spawnitem WorkPants_02","#spawnitem Hiking_Boots_02","#spawnitem Lighter","#spawnitem MRE_Stew","#spawnitem MRE_TunaSalad","#spawnitem Water_05L 2","#spawnitem Banana","#spawnitem BP_Compass_Basic","#spawnitem BP_Weapon_590A11","#spawnitem 12_Gauge_Ammobox_Closed 3","#spawnitem 1H_Bushman","#spawnitem Emergency_Bandage 2"]
time_wait = 15
time_wait_items = 1
# fonction qui va récupéré les commandes une par une et va simuler le "ctrl + v" et la touche "Entrer" pour les coller et entrer dans la console
def allcommand():
    print("Démarage dans",time_wait,"secondes...")
    print("")
    time.sleep(time_wait)
    print("----------------Démarage------------------")
    for value in command:
        print("give de l'items :", value)
        clipboard.copy(value)
        time.sleep(time_wait_items)
        keyboard.write(value)
        keyboard.press_and_release('enter')
    print("------------------FIN---------------------")
allcommand()
