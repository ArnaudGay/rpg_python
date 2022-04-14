import tkinter as tk
from PIL import ImageTk, Image
from random import choice


class Entity:
    def __init__(self, dps, defence, hp):
        self.dps = dps
        self.defence = defence
        self.hp = hp


class PlayerRPG(Entity):
    def __init__(self, player_type):
        if player_type == "Guerrier":
            Entity.__init__(self, 70, 80, 640)
            self.inventory = ["Épée à deux mains", "Armure en plaques"]
        if player_type == "Chasseur":
            Entity.__init__(self, 90, 60, 520)
            self.inventory = ["Arc", "Armure en mailles"]
        if player_type == "Voleur":
            Entity.__init__(self, 110, 40, 480)
            self.inventory = ["Dagues", "Armure en cuir"]
        if player_type == "Moine":
            Entity.__init__(self, 80, 60, 580)
            self.inventory = ["Bâton", "Armure en cuir"]
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
        print("Quel objet souhaitez-vous utiliser ?")
        choice = int(input())
        self.inventory[choice].use(self)

    def attack(self, attack, monster):
        if attack == 1:
            self.dps += 12 + self.level
            monster.defence -= 2 * (0.2 * self.level)

        if attack == 2:
            self.dps += 20 + self.level

        if attack == 3:
            self.dps += 8 + self.level

        if attack == 4:
            self.dps += 14 + self.level


class Monster(Entity):
    def __init__(self, monster_type):
        if monster_type == "Humain":
            Entity.__init__(self, 19, 5, 220)
        if monster_type == "Mort-vivant":
            Entity.__init__(self, 21, 7, 180)
        if monster_type == "Robot":
            Entity.__init__(self, 20, 10, 300)
        if monster_type == "Démon":
            Entity.__init__(self, 25, 8, 260)
        if monster_type == "Boss":
            Entity.__init__(self, 50, 18, 500)

    def attack(self):
        L = ["Attaque légère", "Attaque légère", "Attaque légère", "Attaque lourde"]
        attack = choice(L)

        if attack == "Attaque légère":
            self.dps += 5
            print(attack)

        if attack == "Attaque lourde":
            self.dps += 10

            print(attack)


class Item:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Potion(Item):
    def __init__(self, name, price, type, effect_amount, quantity):
        super().__init__(name, price)
        self.type = type
        self.effect_amount = effect_amount
        self.quantity = quantity

    def use(self, player):
        if self.effect == "Soin":
            player.hp += self.effect_amount
        elif self.effect == "Force":
            player.dps += self.effect_amount
        elif self.effect == "Résistance":
            player.defence += self.effect_amount
            self.quantity -= 1


class Chest(PlayerRPG):
    def __init__(self, effect_amount, level):
        super().__init__(level)
        self.chest = ["Arme", "Armure", "Potion de soin", "Potion de force",
                      "Potion de résistance"]

    def item_dropped(self, player):
        if self.chest == "Arme":
            player.dps += 5 * self.level

        if self.chest == "Armure":
            player.defence += 4 * self.level

        if self.chest == "Potion de soin":
            self.effect_amount = 250 * self.level

        if self.chest == "Potion de force":
            self.effect_amount = 10 * self.level

        if self.chest == "Potion de résistance":
            self.effect_amount = 5 * self.level


def fight(player, monster):
    while player.hp > 0 and monster.hp > 0:
        print("Choisissez une attaque contre ce monstre.", "\n")
        print("[1] Brise-armure, [2] Fendoir, [3] Attaque légère, [4] Attaque lourde", "\n")
        choice = input("Quel attaque voulez-vous utiliser ?\n> ")
        player.attack(choice, monster)
        monster.hp -= player.dps - monster.defence
        print("")
        print("Voici les points de vie du monstre", monster.hp)
        print("")
        print("Le monstre vous attaque.", "\n")
        monster.attack()
        if monster.dps > player.defence:
            player.hp -= monster.dps - player.defence
        print("Voici vos points de vie", player.hp)
        print("")


class Map:
    def __init__(self, place):
        self.size = [[0 for row in range(10)] for col in range(10)]
        self.place = place
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
            print("")
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
            print("")
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
            print("")
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
            print("")
            terr = []
            for ligne in fic:
                terr_bis = []
                for item in ligne:
                    if item != '\n':
                        terr_bis.append(int(item))
                terr.append(terr_bis)
            fic.close()
            self.size = terr
        for i in range(10):
            print(self.size[i])


def move(step):
    liste_condi = [0, 3, 5, 8]
    for i in range(len(map.size)):
        for j in range(1, 10):
            if map.size[i][j] == 7:
                if j != 9:
                    if step == "right" and map.size[i][j+1] in liste_condi:
                        if map.size[i][j+1] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("Vous entrez en combat.", "\n")
                            monstre = choice(["Humain", "Mort-vivant", "Robot", "Démon", "\n"])
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i][j+1] == 8:
                            print("Vous sortez de cette partie du donjon.",  "\n")
                            map.place += 1
                        map.size[i][j+1] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "right" and map.size[i][j+1] == 2:
                        Chest().item_dropped(joueur)
                        return
                if j != 0:
                    if step == "left" and map.size[i][j-1] in liste_condi:
                        if map.size[i][j-1] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("Vous entrez en combat. \n")
                            monstre = choice(["Human", "Undead", "Robot", "Demon", "\n"])
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i][j-1] == 8:
                            print("Vous sortez de cette partie du donjon.", "\n")
                            map.place += 1
                        map.size[i][j-1] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "left" and map.size[i][j-1] == 2:
                        Chest().item_dropped(joueur)
                        return
                if i != 9:
                    if step == "down" and map.size[i+1][j] in liste_condi:
                        if map.size[i+1][j] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("Vous entrez en combat. \n")
                            monstre = choice(["Humain", "Mort-vivant", "Robot", "Démon", "\n"])
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i+1][j] == 8:
                            print("Vous sortez de cette partie du donjon. \n")
                            map.place += 1
                        map.size[i+1][j] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "down" and map.size[i+1][j] == 2:
                        Chest().item_dropped(joueur)
                        return
                if i != 0:
                    if step == "up" and map.size[i-1][j] in liste_condi:
                        if map.size[i-1][j] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("Vous entrez en combat. \n")
                            monstre = choice(["Humain", "Mort-vivant", "Robot", "Démon", "\n"])
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i-1][j] == 8:
                            print("Vous sortez de cette partie du donjon. \n")
                            map.place += 1
                        map.size[i-1][j] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "up" and map.size[i-1][j] == 2:
                        Chest().item_dropped(joueur)
                        return
    print("Vous ne pouvez pas aller ici ! \n")


def affichage(numero):
    if numero == 1:
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
    elif numero == 2:
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
    elif numero == 3:
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
    elif numero == 4:
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


print("Bienvenue sur RPG ATA, veuillez choisir votre classe de personnage entre : 'Guerrier', 'Chasseur', 'Voleur', 'Moine'.", "\n")
player_type = input("> ")
joueur = PlayerRPG(player_type)
print("Vous vous trouvez dans la forêt. Voici la carte :", "\n")
verif = 1
map = Map(1)
affichage(map.place)
print("")
print("Vous êtes le numéro 7, où souhaitez-vous vous déplacer ?", "\n")
print("'droite', 'gauche', 'bas', 'haut'")
step = input("> ")
move(step)


def game(verif):
    global map
    while map.place == verif:
        print("Où souhaitez-vous vous déplacer ? \n")
        print("'droite', 'gauche', 'bas', 'haut'")
        step2 = input("> ")
        move(step2)
    map = Map(map.place + 1)
    if map.place < 5:
        affichage(map.place)
        verif = map.place
        game(verif)
    else:
        print("Vous avez fini le jeu. \n")


game(verif)
