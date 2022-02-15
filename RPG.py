class PlayerRPG:
    def __init__(self, Player_type):
        if Player_type == "Warrior":
            self.attack = 100
            self.magic = None
            self.defence = 80
            self.hp = 210
            self.inventory = ["Sword", "Shield", "Plate armor"]
            
        if Player_type == "Paladin":
            self.attack = 80
            self.magic = 80
            self.defence = 80
            self.hp = 190
            self.inventory = ["Hammer", "Plate armor", "Cape"]
        
        if Player_type == "Hunter":
            self.attack = 105
            self.magic = None
            self.defence = 60
            self.hp = 170
            self.inventory = ["Bow", "Arrow", "Mail armor"]
            
        if Player_type == "Rogue":
            self.attack = 115
            self.magic = None
            self.defence = 40
            self.hp = 150
            self.inventory = ["Double Dagger", "Leather armor"]
            
        if Player_type == "Priest":
            self.attack = 5
            self.magic = 80
            self.defence = 20
            self.hp = 140
            self.inventory = ["Magic baton", "Cloth armor"]
        
        if Player_type == "Death Knight":
            self.attack = 90
            self.magic = 60
            self.defence = 80
            self.hp = 190
            self.inventory = ["Enchanted Sword", "Plate armor"]
            
        if Player_type == "Shaman":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 170
            self.inventory = ["Sledgehammer", "Mail armor"]
        
        if Player_type == "Mage":
            self.attack = 5
            self.magic = 100
            self.defence = 20
            self.hp = 140
            self.inventory = ["Magic baton", "Cloth armor"]
            
        if Player_type == "Warlock":
            self.attack = 5
            self.magic = 105
            self.defence = 20
            self.hp = 140
            self.inventory = ["Possessed baton", "Cloth armor"]
            
        if Player_type == "Monk":
            self.attack = 80
            self.magic = None
            self.defence = 60
            self.hp = 180
            self.inventory = ["Baton", "Leather armor"]
            
        if Player_type == "Druid":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 145
            self.inventory = ["Magic baton", "Leather armor"]
            
        if Player_type == "Demon Hunter":
            self.attack = 80
            self.magic = 20
            self.defence = 60
            self.hp = 175
            self.inventory = ["Blaided Glaive", "Leather armor"]
            
    def Open_inventory(self):
        print(self.inventory) 

class Monster:
    def __init__(self, Monster_type):
        if Monster_type == "Beasts":
            self.attack = 8
            self.defence = 8
            self.magic_resistance = 0
            self.hp = 140
            
        if Monster_type == "Humans":
            self.attack = 12
            self.defence = 15
            self.magic_resistance = 15
            self.hp = 180
            
        if Monster_type == "Undead": 
            self.attack = 13
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 180
            
        if Monster_type == "Robots" :
            self.attack == 15
            self.defence = 17
            self.magic_resistance = 17
            self.hp = 200
            
        if Monster_type == "Giants":
            self.attack = 10
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 220
            
        if Monster_type == "Demons":
            self.attack = 18
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 200
            
        if Monster_type == "Boss": #Only for the lvl 1 Boss
            self.attack = 25
            self.defence = 30
            self.magic_resistance = 30
            self.hp = 300 
                         
class Potion:
    def __init__(self, name, effect, effect_amount):
        self.name = name
        self.effect = effect
        self.effect_amount = effect_amount
    
    def Use(self, player):
        if self.effect == "Heal":
            player.hp += self.effect_amount
        elif self.effect == "Strength":
            player.strength += self.effect_amount
        elif self.effect == "Defence":
            player.defence += self.effect_amount
        
    def Throw(self, monster):
        if self.effect == "Heal":
            monster.hp -= self.effect_amount
        elif self.effect == "Strength":
            monster.strength -= self.effect_amount
        elif self.effect == "Defence":
            monster.defence -= self.effect_amount
            
class Moves:
    def __init__(self):
        pass

class Chest:
    def __init__(self):
        pass

class Donjon:
    def __init__(self):
        pass

class Fight:
    def __init__(self):
        pass

print("oui")

print("non")