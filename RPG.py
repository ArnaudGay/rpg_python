class Entity :
    def __init__(self, attack, magic, defence, mr, hp):
        self.attack = attack
        self.magic = magic
        self.defence = defence
        self.mr = mr
        self.hp = hp
        
class PlayerRPG(Entity):
    def __init__(self, player_type):
        if player_type == "Warrior":
            Entity.__init__(self, 100, None, 80, 60, 630)
            self.inventory = ["Sword", "Shield", "Plate armor"]
            
        if player_type == "Paladin":
            Entity.__init__(self, 80, 80, 70, 80, 570)
            self.inventory = ["Hammer", "Plate armor", "Cape"]
        
        if player_type == "Hunter":
            Entity.__init__(self, 105, None, 60, 60, 510)
            self.inventory = ["Bow", "Arrow", "Mail armor"]
            
        if player_type == "Rogue":
            Entity.__init__(self, 115, None, 40, 60, 450)
            self.inventory = ["Double Dagger", "Leather armor"]
            
        if player_type == "Priest":
            Entity.__init__(self, 5, 80, 20, 90, 420)
            self.inventory = ["Magic baton", "Cloth armor"]
        
        if player_type == "Death Knight":
            Entity.__init__(self, 90, 60, 80, 60, 570)
            self.inventory = ["Enchanted Sword", "Plate armor"]
            
        if player_type == "Shaman":
            Entity.__init__(self, 60, 80, 60, 70, 510)
            self.inventory = ["Sledgehammer", "Mail armor"]
        
        if player_type == "Mage":
            Entity.__init__(self, 5, 100, 20, 85, 420)
            self.inventory = ["Magic baton", "Cloth armor"]
            
        if player_type == "Warlock":
            Entity.__init__(self, 5, 105, 20, 75, 420)
            self.inventory = ["Possessed baton", "Cloth armor"]
            
        if player_type == "Monk":
            Entity.__init__(self, 80, None, 60, 60, 540)
            self.inventory = ["Baton", "Leather armor"]
            
        if player_type == "Druid":
            Entity.__init__(self, 60, 80, 60, 70, 435)
            self.inventory = ["Magic baton", "Leather armor"]
            
        if player_type == "Demon Hunter":
            Entity.__init__(self, 80, 20, 60, 60, 525)
            self.inventory = ["Blaided Glaive", "Leather armor"]
            
    def Open_inventory(self):
        print(self.inventory) 

class Monster(Entity):
    def __init__(self, monster_type):
        if monster_type == "Beast":
            Entity.__init__(self, 8, None, 8, 0, 140)
            
        if monster_type == "Human":
            Entity.__init__(self, 12, None, 15, 15, 180)
            
        if monster_type == "Undead": 
            Entity.__init__(self, 13, None, 20, 20, 180)
            
        if monster_type == "Robot" :
            Entity.__init__(self, 15, 12, 17, 17, 200)
            
        if monster_type == "Giant":
            Entity.__init__(self, 10, None, 20, 20, 220)
            
        if monster_type == "Demon":
            Entity.__init__(self, 18, 16, 20, 20, 200)
            
        if monster_type == "Boss":
            Entity.__init__(self, 50, 50, 30, 30, 500)
                         
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