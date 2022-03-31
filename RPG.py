from random import choice
from re import L

class Entity:
    def __init__(self, attack, defence, hp):
        self.attack = attack
        self.defence = defence
        self.hp = hp


class PlayerRPG(Entity):
    def __init__(self, player_type, player):
        if player_type == "Warrior":
            Entity.__init__(self, 70, 80, 640, player)
            self.inventory = ["Two-handed sword", "Plate armor"]
        if player_type == "Hunter":
            Entity.__init__(self, 90, 60, 520, player)
            self.inventory = ["Bow", "Mail armor"]
        if player_type == "Rogue":
            Entity.__init__(self, 110, 40, 480, player)
            self.inventory = ["Daggers", "Leather armor"]
        if player_type == "Monk":
            Entity.__init__(self, 80, 60, 580, player)
            self.inventory = ["Stave", "Leather armor"]
        self.level = 1
        self.adaptative_attack = 2
        self.adaptative_defence = 1
        self.experience = 0
        self.level_xp = 200 * self.level

    def level_experience(self):
        if self.experience == self.level_xp:
            self.level += 1
            self.experience = 0

    def open_inventory(self):
        for i in range(0, len(self.inventory), 1):
            print(i, self.inventory[i])
            
    def choose_item(self):
        print("What object would you like to use ?")
        choice = int(input())
        self.inventory[choice].use(self)

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
        if monster_type == "Human":
            Entity.__init__(self, 19, 5, 220, monster)
        if monster_type == "Undead":
            Entity.__init__(self, 21, 7, 180, monster)
        if monster_type == "Robot":
            Entity.__init__(self, 20, 10, 300, monster)
        if monster_type == "Demon":
            Entity.__init__(self, 25, 8, 260, monster)
        if monster_type == "Boss":
            Entity.__init__(self, 50, 18, 500, monster)


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
    def __init__(self, name, level):
        self.name = name
        self.level = level
                
    def use(self, name, player):
        pass


class Potion(Item):
    def __init__(self, name, price, type, effect_amount, quantity):
        super().__init__(name, price)
        self.type = type
        self.effect_amount = effect_amount
        self.quantity = quantity

    def use(self, player):
        if self.effect == "Heal":
            player.hp += self.effect_amount
        elif self.effect == "Strength":
            player.attack += self.effect_amount
        elif self.effect == "Resistance":
            player.defence += self.effect_amount
            self.quantity -= 1


class Move:
    def __init__(self):
        pass


class Chest:
    def __init__(self, attack_stat, defence_stat, hp_stat):
        self.chest = ["Two-handed sword", "Daggers", "Stave", "Bow", "Leather armor", "Mail armor", "Plate armor", "Heal potion", "Strength potion", "Resistance potion"]

    def item_dropped(self, player):
        if self.chest == "Two-handed sword":
            player.attack = 10 + (2 * PlayerRPG.level)
            
        if self.chest == "Daggers":
            player.attack = 12 + (2 * PlayerRPG.level)
            
        if self.chest == "Stave":
            player.attack = 10 + (2 * PlayerRPG.level)
            
        if self.chest == "Bow":
            player.attack = 12 + (2 * PlayerRPG.level) 
                
        if self.chest == "Leather armor":
            player.defence = 4 + (PlayerRPG.level * PlayerRPG.adaptative_defence)
            
        if self.chest == "Mail armor":
            player.defence = 6 + (PlayerRPG.level * PlayerRPG.adaptative_defence)
            
        if self.chest == "Plate armor":
            player.defence = 8 + (PlayerRPG.level * PlayerRPG.adaptative_defence)
            
        if self.chest == "Heal potion":
            player.hp = 200 + (PlayerRPG.level * PlayerRPG.adaptative_defence)
            
        if self.chest == "Strenght potion":
            player.attack = 5 + (PlayerRPG.level * PlayerRPG.adaptative_attack)
            
        if self.chest == "Reistance potion":
            player.defence = 2 + (PlayerRPG.level * PlayerRPG.adaptative_defence)
            

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
    def __init__(self, place):
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
        self.map = place
        if place == 1:
            fic = open("forest_map.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
        elif place == 2:
            fic = open("clearing_map.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
        elif place == 3:
            fic = open("hall_donjon.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
        elif place == 4:
            fic = open("throne_hall.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
        elif place == 5:
            fic = open("rooftop_donjon.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
