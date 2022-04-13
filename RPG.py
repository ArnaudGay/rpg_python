import tkinter as tk
from PIL import ImageTk, Image
from random import choice

class Entity:
    def __init__(self, dps, defence, hp):
        self.dps = dps
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
        self.experience = 0
        self.level_xp = 200 * self.level

    def level_experience(self):
        if self.experience == self.level_xp:
            self.level += 1
            self.experience = 0
            self.dps += 5 * self.level
            self.defence += 5 * self.level
            self.hp += 20 * self.level

    def open_inventory(self):
        for i in range(0, len(self.inventory), 1):
            print(i, self.inventory[i])

    def choose_item(self):
        print("What object would you like to use ?")
        choice = int(input())
        self.inventory[choice].use(self)

    def attack(self, attack, monster):
        if attack == "armor_breaker":
            self.attack += 12 + self.level
            monster.defence -= 2 * (0.2 * self.level)

        if attack == "cleaver":
            self.attack += 20 + self.level

        if attack == "light_attack":
            self.attack += 8 + self.level

        if attack == "heavy_attack":
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

    def attack(self, attack):

        L = ["light_attack", "light_attack", "light_attack", "heavy_attack"]
        attack = choice(L)

        if attack == "light_attack":
            self.dps += 5 + self.level
            print(attack)

        if attack == "heavy_attack":
            self.dps += 10 + self.level

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


class Chest(PlayerRPG):
    def __init__(self, effect_amount, level):
        super().__init__(level)
        self.chest = ["Weapon", "Armor", "Heal potion", "Strength potion",
                      "Resistance potion"]

    def item_dropped(self, player):
        if self.chest == "Weapon":
            player.attack += 5 * self.level

        if self.chest == "Armor":
            player.defence += 4 * self.level

        if self.chest == "Heal potion":
            self.effect_amount = 250 * self.level

        if self.chest == "Strenght potion":
            self.effect_amount = 10 * self.level

        if self.chest == "Reistance potion":
            self.effect_amount = 5 * self.level


class Donjon:
    def __init__(self):
        pass

    def fight(player, monster):
        while player.hp > 0:
            print("Armor breaker", "Cleaver", "Light attack", "Heavy attack")
            choice = input("Which attack do you want ?")
            player.attack(choice, monster)
            monster.hp -= player.attack - monster.defence
        while monster.hp > 0:
            player.hp -= monster.attack - player.defence


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
            fic = open("Maps/1 - forest_map.txt", "r")
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
            fic = open("Maps/2 - clearing_map.txt", "r")
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
            fic = open("Maps/3 - hall_donjon.txt", "r")
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
            fic = open("Maps/4 - throne_hall.txt", "r")
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
            fic = open("Maps/5 - rooftop_donjon.txt", "r")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr

    def move(self, step):
        step = step
        for i in range(len(self.size)):
            for j in range(1, 10):
                if step == "right_key":
                    self.size[i][j] == self.size[i][j+1]
                    if self.size[j] == 2:
                        self.size[i][j] -= self.size[i][j-1]
                    if self.size[j] == 3:
                        self.size[i][j] -= self.size[i][j-1]
                    if self.size[j] == 4:
                        self.size[i][j] -= self.size[i][j-1]
                if step == "left_key":
                    self.size[i][j] == self.size[i][j-1]
                    if self.size[j] == 2:
                        self.size[i][j] -= self.size[i][j+1]
                    if self.size[j] == 3:
                        self.size[i][j] -= self.size[i][j+1]
                    if self.size[j] == 4:
                        self.size[i][j] -= self.size[i][j+1]
                if step == "down_key":
                    self.size[i][j] == self.size[i-1][j]
                    if self.size[j] == 2:
                        self.size[i][j] -= self.size[i+1][j]
                    if self.size[j] == 3:
                        self.size[i][j] -= self.size[i+1][j]
                    if self.size[j] == 4:
                        self.size[i][j] -= self.size[i+1][j]
                if step == "up_key":
                    self.size[i][j] == self.size[i+1][j]
                    if self.size[j] == 2:
                        self.size[i][j] -= self.size[i-1][j]
                    if self.size[j] == 3:
                        self.size[i][j] -= self.size[i-1][j]
                    if self.size[j] == 3:
                        self.size[i][j] -= self.size[i-1][j]



class Interface:
    def __init__(self):
        story1 = tk.Tk()
        story1.title("RPG ATA")
        story1.attributes('-fullscreen', True)
        story1.bind('<Escape>', lambda e: story1.destroy())
        story1.configure(bg="black")
        story1_image = ImageTk.PhotoImage(Image.open("Images/Story1.png"))
        story1_label = tk.Label(bd=0, image=story1_image)
        story1_label.pack()
        button = tk.Button(story1, text='Suivant', font=('arial', '24'), command=story1.destroy)
        button.pack(side='right', padx=50)
        story1.mainloop()
    
        story2 = tk.Tk()
        story2.attributes('-fullscreen', True)
        story2.bind('<Escape>', lambda e: story2.destroy())
        story2.configure(bg="black")
        story2_image = ImageTk.PhotoImage(Image.open("Images/Story2.png"))
        story2_label = tk.Label(bd=0, image=story2_image)
        story2_label.pack()
        button = tk.Button(story2, text='Suivant', font=('arial', '24'), command=story2.destroy)
        button.pack(side='right', padx=50)
        story2.mainloop()

        story3 = tk.Tk()
        story3.attributes('-fullscreen', True)
        story3.bind('<Escape>', lambda e: story3.destroy())
        story3.configure(bg="black")
        story3_image = ImageTk.PhotoImage(Image.open("Images/Story3.png"))
        story3_label = tk.Label(bd=0, image=story3_image)
        story3_label.pack()
        button = tk.Button(story3, text='Suivant', font=('arial', '24'), command=story3.destroy)
        button.pack(side='right', padx=50)
        story3.mainloop()

        story4 = tk.Tk()
        story4.attributes('-fullscreen', True)
        story4.bind('<Escape>', lambda e: story4.destroy())
        story4.configure(bg="black")
        story4_image = ImageTk.PhotoImage(Image.open("Images/Story4.png"))
        story4_label = tk.Label(bd=0, image=story4_image)
        story4_label.pack()
        button = tk.Button(story4, text='Suivant', font=('arial', '24'), command=story4.destroy)
        button.pack(side='right', padx=50)
        story4.mainloop()

map = Map(1)
interface = Interface()
