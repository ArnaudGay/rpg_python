class PlayerRPG:
    def __init__(self):
        if Player_type == "Warrior":
            self.attack = 100
            self.magic = 0
            self.defence = 80
            self.hp = 100
            self.inventory = ["Sword", "Shield", "Plate armor"]
            
        if Player_type == "Paladin":
            self.attack = 60
            self.magic = 80
            self.defence = 80
            self.hp = 80
            self.inventory = ["Hammer", "Plate armor"]
        
        if Player_type == "Hunter":
            self.attack = 100
            self.magic = 0
            self.defence = 60
            self.hp = 70
            self.inventory = ["Bow", "Arrow", "Mail armor"]
            
        if Player_type == "Rogue":
            self.attack = 110
            self.magic = 0
            self.defence = 40
            self.hp = 60
            self.inventory = ["Double Dagger", "Leather armor"]
            
        if Player_type == "Priest":
            self.attack = 1
            self.magic = 80
            self.defence = 20
            self.hp = 55
            self.inventory = ["Magic wand", "Cloth armor"]
        
        if Player_type == "Death Knight":
            self.attack = 90
            self.magic = 60
            self.defence = 80
            self.hp = 90
            self.inventory = ["Enchanted Sword", "Plate armor"]
            
        if Player_type == "Shaman":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 80
            self.inventory = ["Sledgehammer", "Mail armor"]
        
        if Player_type == "Mage":
            self.attack = 1
            self.magic = 100
            self.defence = 20
            self.hp = 50
            self.inventory = ["Magic baton", "Cloth armor"]
            
        if Player_type == "Warlock":
            self.attack = 1
            self.magic = 110
            self.defence = 10
            self.hp = 45
            self.inventory = ["Possessed baton", "Cloth armor"]
            
        if Player_type == "Monk":
            self.attack = 80
            self.magic = 0
            self.defence = 60
            self.hp = 80
            self.inventory = ["Leather armor"]
            
        if Player_type == "Druid":
            self.attack = 60
            self.magic = 80
            self.defence = 60
            self.hp = 60
            self.inventory = ["Magic", "Leather armor"]
            
        if Player_type == "Demon Hunter":
            self.attack = 80
            self.magic = 0
            self.defence = 60
            self.hp = 70
            self.inventory = ["Blaided Glaive", "Leather armor"]

class Monster:
    def __init__(self):
        pass

class Use_Potion():
    def __init__(self):
        pass

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
