import random
from vikingsClasses import Soldier, Viking, Saxon, War

nombres_vikingos = ["Adrian","Carla","Montse"] 
nombres_saxons = ["David","Gonzalo","Elena"]

def crear_vikingos(num):
    vikingos = [Viking(random.choice(nombres_vikingos), 100, 50) for _ in range(num)]
    return vikingos

def crear_saxons(num):
    saxons = [Saxon(100, 50) for _ in range(num)]
    return saxons

def juego():
    print("Creando guerra...")
    guerra = War()
    num_vikingos = 2
    num_saxons = 2

    for viking in crear_vikingos(num_vikingos):
        guerra.addViking(viking)
    for saxon in crear_saxons(num_saxons):
        guerra.addSaxon(saxon)

    print("Iniciando batalla...")
    while guerra.vikingArmy and guerra.saxonArmy:
        print("Vikingo ataca")
        guerra.vikingAttack()
        if not guerra.saxonArmy:
            print(f"¡Los vikingos han ganado la batalla!")
            break
        print("Saxon ataca")
        guerra.saxonAttack()
        if not guerra.vikingArmy:
            print(f"¡Los Saxons han ganado la batalla!")
            break

    guerra.showStatus()
    print("Fin del juego")
    
juego()
    
        

