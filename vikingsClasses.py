import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def battleCry(self):
        return f"¡Odin os posee a todos!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"<{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en acto de combate"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"Saxon ha recibido {damage} puntos de daño"
        else:
            return f"Un saxon ha muerto en acto de combate"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        rand_saxon = random.choice(self.saxonArmy)
        rand_viking = random.choice(self.vikingArmy)

        damage = rand_viking.strength
        result = rand_saxon.receiveDamage(damage)

        if rand_saxon.health <= 0:
            self.saxonArmy.remove(rand_saxon)
        return result  
        
        
    def saxonAttack(self):        
        rand_saxon = random.choice(self.saxonArmy)
        rand_viking = random.choice(self.vikingArmy)

        damage = rand_saxon.strength
        result = rand_viking.receiveDamage(damage)

        if rand_viking.health <= 0:
            self.vikingArmy.remove(rand_viking)

        return result
        
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.vikingArmy) == 0:
            return f"Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return f"Los Vikingos y los Sajones todavía están en plena batalla."
    pass

#yop
#class War2:

 #   def __init__(self):
        # your code here

  #  def addViking(self, Viking):
        # your code here
    
   # def addSaxon(self, Saxon):
        # your code here
    
    #def vikingAttack(self):
        # your code here

    #def saxonAttack(self):
        # your code here

    #def showStatus(self):
        # your code here

    #pass


