from random import choice
from re import L

class Entity:
    def __init__(self, attack, magic, defence, mr, hp):
        self.attack = attack
        self.magic = magic
        self.defence = defence
        self.mr = mr
        self.hp = hp


class PlayerRPG(Entity):
    def __init__(self, player_type, player):
        if player_type == "Warrior":
            Entity.__init__(self, player, 100, None, 80, 60, 630)
            self.inventory = ["Sword", "Shield", "Plate armor"]
        if player_type == "Paladin":
            Entity.__init__(self, player, 80, 80, 70, 80, 570)
            self.inventory = ["Hammer", "Plate armor", "Cape"]
        if player_type == "Hunter":
            Entity.__init__(self, player, 105, None, 60, 60, 510)
            self.inventory = ["Bow", "Arrow", "Mail armor"]
        if player_type == "Rogue":
            Entity.__init__(self, player, 115, None, 40, 60, 450)
            self.inventory = ["Double Dagger", "Leather armor"]
        if player_type == "Priest":
            Entity.__init__(self, player, 5, 80, 20, 90, 420)
            self.inventory = ["Magic baton", "Cloth armor"]
        if player_type == "Death Knight":
            Entity.__init__(self, player, 90, 60, 80, 60, 570)
            self.inventory = ["Enchanted Sword", "Plate armor"]
        if player_type == "Shaman":
            Entity.__init__(self, player, 60, 80, 60, 70, 510)
            self.inventory = ["Sledgehammer", "Mail armor"]
        if player_type == "Mage":
            Entity.__init__(self, player, 5, 100, 20, 85, 420)
            self.inventory = ["Magic baton", "Cloth armor"]
        if player_type == "Warlock":
            Entity.__init__(self, player, 5, 105, 20, 75, 420)
            self.inventory = ["Possessed baton", "Cloth armor"]
        if player_type == "Monk":
            Entity.__init__(self, player, 80, None, 60, 60, 540)
            self.inventory = ["Baton", "Leather armor"]
        if player_type == "Druid":
            Entity.__init__(self, player, 60, 80, 60, 70, 435)
            self.inventory = ["Magic baton", "Leather armor"]
        if player_type == "Demon Hunter":
            Entity.__init__(self, player, 80, 20, 60, 60, 525)
            self.inventory = ["Blaided Glaive", "Leather armor"]
        self.level = 1
        self.experience = 0
        self.level_xp = 200 * self.level

    def level_experience(self):
        if self.experience == self.level_xp:
            self.level += 1
            self.experience = 0

    def open_inventory(self):
        for i in range(0, len(self.inventory), 1):
            print(i, self.inventory[i])

    def choose_item_to_use(self):
        print("which item do you want ?")
        choice = int(input())
        self.inventory[choice].use(self)
    
    def attack(self,attack,monster):
        if attack == "armor_breaker" : 
            self.attack += 12 + self.level
            monster.defence -= 2 * (0,2 *  self.level)   

        if attack == "cleaver" : 
            self.attack += 20 + self.level  

        if attack == "light_attack" : 
            self.attack += 8 + self.level

        if attack == "heavy_attack" :  
            self.attack += 14 + self.level

class Monster(Entity):
    def __init__(self, monster_type, monster):
        if monster_type == "Beast":
            Entity.__init__(self, monster, 8, None, 8, 0, 300)
        if monster_type == "Human":
            Entity.__init__(self, monster, 12, None, 15, 15, 340)
        if monster_type == "Undead":
            Entity.__init__(self, monster, 13, None, 20, 20, 380)
        if monster_type == "Robot":
            Entity.__init__(self, monster, 15, 12, 17, 17, 400)
        if monster_type == "Giant":
            Entity.__init__(self, monster, 10, None, 20, 20, 420)
        if monster_type == "Demon":
            Entity.__init__(self, monster, 18, 16, 20, 20, 400)
        if monster_type == "Boss":
            Entity.__init__(self, monster, 50, 50, 30, 30, 800)


    def attack(self, attack) : 


        L = ["light_attack","light_attack","light_attack","heavy_attack"] 
        attack = choice(L)

        if attack == "light_attack" :
            self.attack += 6 + self.level
            
            print(attack)

        if attack == "heavy_attack" :
            self.attack += 12 + self.level

            print(attack)

class Item:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
    def use(self, item_name, player):
        if item_name == "Class weapon":
            PlayerRPG.attack = 40 + (2 * PlayerRPG.level)
        if item_name == "Class armor":
            PlayerRPG.attack = 10 + (1 * PlayerRPG.level)


class Potion(Item):
    def __init__(self, name, price, effect, effect_amount, quantity):
        super().__init__(name, price)
        self.effect = effect
        self.effect_amount = effect_amount
        self.quantity = quantity

    def use(self, player):
        if self.effect == "Heal":
            player.hp += self.effect_amount
        elif self.effect == "Strength":
            player.attack += self.effect_amount
        elif self.effect == "Defence":
            player.defence += self.effect_amount
            self.quantity -= 1

    def throw(self, monster):
        if self.effect == "Heal":
            monster.hp -= self.effect_amount
        elif self.effect == "Strength":
            monster.attack -= self.effect_amount
        elif self.effect == "Defence":
            monster.defence -= self.effect_amount
            self.quantity -= 1


class Move:
    def __init__(self):
        pass


class Chest:
    def __init__(self):
        self.chest = ["Class weapon", "Class armor", "Heal potion", "Strength potion", "Resistance potion", "Weakness potion"]

    def item_dropped(self):
        if self.chest[0] in PlayerRPG.inventory:
            PlayerRPG.attack = 40 + (2 * PlayerRPG.level)
        if self.chest[1] in PlayerRPG.inventory:
            PlayerRPG.defence = 10 + (1 * PlayerRPG.level)


class Donjon:
    def __init__(self):
        pass

def fight(player,monster):
    while player.hp > 0 :
        print("armor breaker", "cleaver", "light attack", "heavy attack")
        choice = input("Which attack do you want ?")
        player.attack(choice,monster)
        monster.hp -= player.attack * monster.defence 
    while monster.hp > 0 :
        player.hp -= monster.attack * player.defence 


class Interface:
    def __init__(self):
        pass

class Map:
    def __init__(self):
        self.size = [[0 for row in range(10)] for col in range(10)]
        for y in range(10):
            for x in range(10):
                if y == 0:
                    self.size[y][x] = -1
                elif x == 0:
                    self.size[y][x] = -1
                elif y == (10 - 1):
                    self.size[y][x] = -1
                elif x == (10 - 1):
                    self.size[y][x] = -1

    def forest_map():
        pass

    def clearing_map():
        pass

    def hall_donjon():
        pass

    def throne_hall():
        pass

    def rooftop_donjon():
        pass
