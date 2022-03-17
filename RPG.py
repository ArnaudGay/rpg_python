class Entity :
    def __init__(self, attack, magic, defence, mr, hp, level, experience):
        self.attack = attack
        self.magic = magic
        self.defence = defence
        self.mr = mr
        self.hp = hp
        
class PlayerRPG(Entity):
    def __init__(self, player_type, level, experience, level_xp):
        if player_type == "Warrior":
            Entity.__init__(self, 100, None, 80, 60, 630, 1, 0)
            self.inventory = ["Sword", "Shield", "Plate armor"]
            
        if player_type == "Paladin":
            Entity.__init__(self, 80, 80, 70, 80, 570, 1, 0)
            self.inventory = ["Hammer", "Plate armor", "Cape"]
        
        if player_type == "Hunter":
            Entity.__init__(self, 105, None, 60, 60, 510, 1, 0)
            self.inventory = ["Bow", "Arrow", "Mail armor"]
            
        if player_type == "Rogue":
            Entity.__init__(self, 115, None, 40, 60, 450, 1, 0)
            self.inventory = ["Double Dagger", "Leather armor"]
            
        if player_type == "Priest":
            Entity.__init__(self, 5, 80, 20, 90, 420, 1, 0)
            self.inventory = ["Magic baton", "Cloth armor"]
        
        if player_type == "Death Knight":
            Entity.__init__(self, 90, 60, 80, 60, 570, 1, 0)
            self.inventory = ["Enchanted Sword", "Plate armor"]
            
        if player_type == "Shaman":
            Entity.__init__(self, 60, 80, 60, 70, 510, 1, 0)
            self.inventory = ["Sledgehammer", "Mail armor"]
        
        if player_type == "Mage":
            Entity.__init__(self, 5, 100, 20, 85, 420, 1, 0)
            self.inventory = ["Magic baton", "Cloth armor"]
            
        if player_type == "Warlock":
            Entity.__init__(self, 5, 105, 20, 75, 420, 1, 0)
            self.inventory = ["Possessed baton", "Cloth armor"]
            
        if player_type == "Monk":
            Entity.__init__(self, 80, None, 60, 60, 540, 1, 0)
            self.inventory = ["Baton", "Leather armor"]
            
        if player_type == "Druid":
            Entity.__init__(self, 60, 80, 60, 70, 435, 1, 0)
            self.inventory = ["Magic baton", "Leather armor"]
            
        if player_type == "Demon Hunter":
            Entity.__init__(self, 80, 20, 60, 60, 525, 1, 0)
            self.inventory = ["Blaided Glaive", "Leather armor"]
        
        self.level = level
        self.experience = experience 
        self.level_xp = 200 * level
             
          
    def level_experience(self):
        if self.experience == self.level_xp:
            self.level += 1      
            
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
            player.attack += self.effect_amount
        elif self.effect == "Defence":
            player.defence += self.effect_amount
        
    def Throw(self, monster):
        if self.effect == "Heal":
            monster.hp -= self.effect_amount
        elif self.effect == "Strength":
            monster.attack -= self.effect_amount
        elif self.effect == "Defence":
            monster.defence -= self.effect_amount
            
class Move:
    def __init__(self):
        pass
        
class Chest:
    def __init__(self):
        self.chest = ["Class weapon", "Class armor", "Heal potion", "Force potion", "Resistance potion", "Weakness potion",]      

    def Item_dropped(self):
        if self.chest[0] in PlayerRPG.inventory :
            PlayerRPG.attack += 40 + 2 * PlayerRPG.level
        
        if self.chest[1] in PlayerRPG.inventory:
            PlayerRPG.defence += 10 + 1 * PlayerRPG.level
        
class Donjon:
    def __init__(self):
        pass

class Fight:
    def __init__(self):
        pass

class Interface:
    def __init__(self):
        pass

class Map:
    def __init__(self, size):
        self.size = [[0 for row in range(10)]0 for col in range(10)]
        for y in range(10):
            for x in range(1O):
                if y == 0:
                    self.size[y][x] = -1
                elif x == 0:
                    self.size[y][x] = -1
                elif y == (10 - 1):
                    self.size[y][x] = -1
                elif x == (10 - 1):
                    self.size[y][x] = -1


        

class Fight:
    def __init__(self):
        pass