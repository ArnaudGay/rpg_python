class Entity :
    def __init__(self, attack, magic, defence, magic_resistance, hp):
        self.attack = attack
        self.magic = magic
        self.defence = defence
        self.hp = hp
        
class PlayerRPG(Entity):
    def __init__(self, Player_type):
        if Player_type == "Warrior":
            Entity.__init__(100, None, 80, 630)
            self.inventory = ["Sword", "Shield", "Plate armor"]
            
        if Player_type == "Paladin":
            Entity.__init__(80, 80, 80, 570)
            self.inventory = ["Hammer", "Plate armor", "Cape"]
        
        if Player_type == "Hunter":
            Entity.__init__()
            self.attack = 105
            self.magic = None
            self.defence = 60
            self.hp = 510
            self.inventory = ["Bow", "Arrow", "Mail armor"]
            
        if Player_type == "Rogue":
            self.attack = 115
            self.magic = None
            self.defence = 40
            self.hp = 450
            self.inventory = ["Double Dagger", "Leather armor"]
            
        if Player_type == "Priest":
            self.attack = 5
            self.magic = 80
            self.defence = 20
            self.hp = 420
            self.inventory = ["Magic baton", "Cloth armor"]
        
        if Player_type == "Death Knight":
            self.attack = 90
            self.magic = 60
            self.defence = 80
            self.hp = 570
            self.inventory = ["Enchanted Sword", "Plate armor"]
            
        if Player_type == "Shaman":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 510
            self.inventory = ["Sledgehammer", "Mail armor"]
        
        if Player_type == "Mage":
            self.attack = 5
            self.magic = 100
            self.defence = 20
            self.hp = 420
            self.inventory = ["Magic baton", "Cloth armor"]
            
        if Player_type == "Warlock":
            self.attack = 5
            self.magic = 105
            self.defence = 20
            self.hp = 420
            self.inventory = ["Possessed baton", "Cloth armor"]
            
        if Player_type == "Monk":
            self.attack = 80
            self.magic = None
            self.defence = 60
            self.hp = 540
            self.inventory = ["Baton", "Leather armor"]
            
        if Player_type == "Druid":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 435
            self.inventory = ["Magic baton", "Leather armor"]
            
        if Player_type == "Demon Hunter":
            self.attack = 80
            self.magic = 20
            self.defence = 60
            self.hp = 525
            self.inventory = ["Blaided Glaive", "Leather armor"]
            
    def Open_inventory(self):
        print(self.inventory) 

class Monster(Entity):
    def __init__(self, monster_type):
        if monster_type == "Beast":
            Entity().__init__(8, None, 8, 0, 140,) . 
            self.attack = 8
            self.defence = 8
            self.magic_resistance = 0
            self.hp = 140
            
        if monster_type == "Human":
            self.attack = 12
            self.defence = 15
            self.magic_resistance = 15
            self.hp = 180
            
        if monster_type == "Undead": 
            self.attack = 13
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 180
            
        if monster_type == "Robot" :
            self.attack == 15
            self.defence = 17
            self.magic_resistance = 17
            self.hp = 200
            
        if monster_type == "Giant":
            self.attack = 10
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 220
            
        if monster_type == "Demon":
            self.attack = 18
            self.defence = 20
            self.magic_resistance = 20
            self.hp = 200
            
        if monster_type == "Boss":
            self.attack = 50
            self.defence = 30
            self.magic_resistance = 30
            self.hp = 500 
                         
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


class Interface:
    def __init__(self):
        pass


class Save:
    def __init__(self):
        pass
