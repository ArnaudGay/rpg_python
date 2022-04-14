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
            print("BRAVO !!! Vous gagnez un niveau")
            print("Vous passez niveau", self.level)

    def open_inventory(self):
        for i in range(0, len(self.inventory), 1):
            print(i, self.inventory[i])

    def choose_item(self):
        print("Quel objet souhaitez-vous utiliser ?")
        choice = int(input())
        self.inventory[choice].use(self)

    def attack(self, attack, monster):
        if attack == 1:
            print("Vous utilisez 'Brise-armure'")
            if self.player_type == "Guerrier":
                self.dps = 70
            if self.player_type == "Chasseur":
                self.dps = 90
            if self.player_type == "Voleur":
                self.dps = 110
            if self.player_type == "Moine":
                self.dps = 80
            self.dps += 12 + self.level
            self.dps -= monster.defence/10

        if attack == 2:
            print("Vous utilisez 'Fendoir'")
            self.dps = player_type.dps
            self.dps += 20 + self.level
            self.dps -= monster.defence/10

        if attack == 3:
            print("Vous utilisez 'Attaque légère'")
            self.dps = player_type.dps
            self.dps += 8 + self.level
            self.dps -= monster.defence/10

        if attack == 4:
            print("Vous utilisez 'Attaque lourde'")
            self.dps = player_type.dps
            self.dps += 14 + self.level
            self.dps -= monster.defence/10


class Monster(Entity):
    def __init__(self, monster_type):
        if monster_type == 1:
            print("")
            print("Vous affrontez un humain")
            print("")
            Entity.__init__(self, 30, 10, 220)
        if monster_type == 2:
            print("")
            print("Vous affrontez un mort-vivant")
            print("")
            Entity.__init__(self, 35, 12, 180)
        if monster_type == 3:
            print("")
            print("Vous affrontez un robot")
            print("")
            Entity.__init__(self, 40, 15, 300)
        if monster_type == 4:
            print("")
            print("Vous affrontez un démon")
            print("")
            Entity.__init__(self, 45, 13, 260)
        if monster_type == 5:
            print("")
            print("Vous affrontez un boss")
            print("")
            Entity.__init__(self, 70, 20, 500)

    def attack(self, player):
        L = ["Attaque légère", "Attaque légère", "Attaque légère", "Attaque lourde"]
        attack = choice(L)

        if attack == "Attaque légère":
            self.dps += 5
            self.dps -= player.defence/10
            print("Il utilise une attaque légère", "\n")

        if attack == "Attaque lourde":
            self.dps += 10
            self.dps -= player.defence/10
            print("Il utilise une attaque lourde" "\n")


class Potion():
    def __init__(self, type, effect_amount, quantity):
        self.type = type
        self.effect_amount = effect_amount
        self.quantity = quantity

    def use(self, player):
        print("")
        print("Quelle potion souhaitez-vous utiliser : [1] Potion de soin / [2] Potion de force / [3] Potion de résistance")
        potion_choice = input("> ")
        if potion_choice == 1 and "Potion de soin" in player.inventory:
            player.hp += 200
            player.inventory.remove("Potion de soin")
        elif self.effect == 2 and "Potion de force" in player.inventory:
            player.dps += 10
            player.inventory.remove("Potion de force")
        elif self.effect == 3 and "Potion de résistance" in player.inventory:
            player.defence += 10
            player.inventory.remove("Potion de résistance")


class Chest():
    def __init__(self):
        self.chest = ["Arme", "Armure", "Potion de soin", "Potion de force",
                      "Potion de résistance"]

    def item_dropped(self, player):
        drop = choice(self.chest)
        if drop == "Arme":
            player.dps += 5 * player.level
            print("Vous avez gagné", 5*player.level, "d'attaque.")
        elif drop == "Armure":
            player.defence += 4 * player.level
            print("Vous avez gagné", 4*player.level, "de défense.")
        elif drop == "Potion de soin":
            player.inventory.append("Potion de soin")
            player.effect_amount = 250 * player.level
            print("Vous avez gagné une potion de soin.")
        elif drop == "Potion de force":
            player.inventory.append("Potion de force")
            player.effect_amount = 10 * player.level
            print("Vous avez gagné une Potion de force.")
        elif drop == "Potion de résistance":
            player.inventory.append("Potion de résistance")
            player.effect_amount = 5 * player.level
            print("Vous avez gagné une Potion de résistance.")


def fight(player, monster):
    while player.hp > 0 and monster.hp > 0:
        print("Souhaitez-vous attaquer ou ouvrir votre inventaire ?\n")
        result = input("[1] Attaquer / [2] Inventaire\n>")
        if result == "1":
            print("")
            print("Choisissez une attaque contre ce monstre.", "\n")
            print("[1] Brise-armure / [2] Fendoir / [3] Attaque légère / [4] Attaque lourde", "\n")
            choice = int(input("Quel attaque voulez-vous utiliser ?\n>"))
            player.attack(choice, monster)
            monster.hp -= player.dps
            print("---------------------------------------")
            print("Vous infligez", player.dps,"dégats")
            print("Voici les points de vie du monstre: ", monster.hp)
            print("---------------------------------------")
            print("Le monstre vous attaque !", "\n")
            monster.attack(player)
            if monster.dps > (player.defence / 10):
                player.hp -= monster.dps
                print("Cette attaque vous fait", monster.dps, "dégats")
                print("Voici vos points de vie: ", player.hp)
            else:
                print("Cette attaque ne vous fait rien")
            print("---------------------------------------")
        elif result == "2":
            print("Voici votre inventaire:")
            for i in range(len(player.inventory)):
                print(i, player.inventory[i])
            print("")
            print("Choissisez l'objet que vous souhaitez utiliser, potion uniquement.")
        else:
            print("Votre action n'est pas possible !")
    if monster.hp <= 0 :
        player.experience += 200

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
                    if step == "droite" and map.size[i][j+1] in liste_condi:
                        if map.size[i][j+1] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("----------------------")
                            print("!!! Vous entrez en combat !!!")
                            print("----------------------")
                            monstre = choice(range(1, 5))
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i][j+1] == 8:
                            print("Vous sortez de cette partie du donjon",  "\n")
                            map.place += 1
                            return
                        map.size[i][j+1] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "droite" and map.size[i][j+1] == 2:
                        Chest().item_dropped(joueur)
                        return
                if j != 0:
                    if step == "gauche" and map.size[i][j-1] in liste_condi:
                        if map.size[i][j-1] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("----------------------")
                            print("Vous entrez en combat")
                            print("----------------------")
                            monstre = choice(range(1, 5))
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i][j-1] == 8:
                            print("Vous sortez de cette partie du donjon", "\n")
                            map.place += 1
                            return
                        map.size[i][j-1] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "gauche" and map.size[i][j-1] == 2:
                        coffre = Chest()
                        coffre.item_dropped(joueur)
                        print(joueur.inventory)
                        return
                if i != 9:
                    if step == "bas" and map.size[i+1][j] in liste_condi:
                        if map.size[i+1][j] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("----------------------")
                            print("Vous entrez en combat")
                            print("----------------------")
                            monstre = choice(range(1, 5))
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i+1][j] == 8:
                            print("Vous sortez de cette partie du donjon", "\n")
                            map.place += 1
                            return
                        map.size[i+1][j] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "bas" and map.size[i+1][j] == 2:
                        Chest().item_dropped(joueur)
                        return
                if i != 0:
                    if step == "haut" and map.size[i-1][j] in liste_condi:
                        if map.size[i-1][j] == 5:
                            for x in range(10):
                                print(map.size[x])
                            print("----------------------")
                            print("Vous entrez en combat")
                            print("----------------------")
                            monstre = choice(range(1, 5))
                            figter1 = Monster(monstre)
                            fight(joueur, figter1)
                        elif map.size[i-1][j] == 8:
                            print("Vous sortez de cette partie du donjon", "\n")
                            map.place += 1
                            return
                        map.size[i-1][j] = 7
                        map.size[i][j] = 0
                        for x in range(10):
                            print(map.size[x])
                        return
                    elif step == "haut" and map.size[i-1][j] == 2:
                        Chest().item_dropped(joueur)
                        return
    print("")
    print("!!! Vous ne pouvez pas aller ici !!!", "\n")


def affichage(numero):
    if numero == 0:
        story0 = tk.Tk()
        story0.title("RPG ATA")
        story0.attributes('-fullscreen', True)
        story0.bind('<Escape>', lambda e: story0.destroy())
        story0.configure(bg="black")
        story0_image = ImageTk.PhotoImage(Image.open("Images/Story0.png"))
        story0_label = tk.Label(bd=0, image=story0_image)
        story0_label.pack(side="bottom", pady=300)
        story0.mainloop()
    if numero == 1:
        story1 = tk.Tk()
        story1.title("RPG ATA")
        story1.attributes('-fullscreen', True)
        story1.bind('<Escape>', lambda e: story1.destroy())
        story1.configure(bg="black")
        story1_image = ImageTk.PhotoImage(Image.open("Images/Story1.png"))
        story1_label = tk.Label(bd=0, image=story1_image)
        story1_label.pack(side="bottom", pady=350)
        story1.mainloop()
    elif numero == 2:
        story2 = tk.Tk()
        story2.attributes('-fullscreen', True)
        story2.bind('<Escape>', lambda e: story2.destroy())
        story2.configure(bg="black")
        story2_image = ImageTk.PhotoImage(Image.open("Images/Story2.png"))
        story2_label = tk.Label(bd=0, image=story2_image)
        story2_label.pack(side="bottom", pady=400)
        story2.mainloop()
    elif numero == 3:
        story3 = tk.Tk()
        story3.attributes('-fullscreen', True)
        story3.bind('<Escape>', lambda e: story3.destroy())
        story3.configure(bg="black")
        story3_image = ImageTk.PhotoImage(Image.open("Images/Story3.png"))
        story3_label = tk.Label(bd=0, image=story3_image)
        story3_label.pack(side="bottom", pady=350)
        story3.mainloop()
    elif numero == 4:
        story4 = tk.Tk()
        story4.attributes('-fullscreen', True)
        story4.bind('<Escape>', lambda e: story4.destroy())
        story4.configure(bg="black")
        story4_image = ImageTk.PhotoImage(Image.open("Images/Story4.png"))
        story4_label = tk.Label(bd=0, image=story4_image)
        story4_label.pack(side="bottom", pady=400)
        story4.mainloop()


affichage(0)
print("--------------------------------------------------------------------------------------------------------------------")
print("Bienvenue sur RPG ATA, veuillez choisir votre classe de personnage entre: ")
print("[1] Guerrier / [2] Chasseur / [3] Voleur / [4] Moine")
print("--------------------------------------------------------------------------------------------------------------------")
player_type = input("> ")
if player_type == "1" or player_type == "guerrier":
    player_type = "Guerrier"
elif player_type == "2" or player_type == "chasseur":
    player_type = "Chasseur"
elif player_type == "3" or player_type == "voleur":
    player_type = "Voleur"
elif player_type == "4" or player_type == "moine":
    player_type = "Moine"
joueur = PlayerRPG(player_type)
print("")
print("Vous vous trouvez dans la forêt. Voici la carte: ", "\n")
verif = 1
map = Map(1)
print("")
print("Vous êtes le chiffre 7, où souhaitez-vous vous déplacer ?", "\n")
print("[1] Droite / [2] Gauche / [3] Bas / [4] Haut")
step = input("> ")
if step == "1" or step == "Droite":
    step = "droite"
elif step == "2" or step == "Gauche":
    step = "gauche"
elif step == "3" or step == "Bas":
    step = "bas"
elif step == "4" or step == "Haut":
    step = "haut"
move(step)


def game(verif, map):
    while map.place == verif:
        print("Où souhaitez-vous vous déplacer ? \n")
        print("[1] Droite / [2] Gauche / [3] Bas / [4] Haut")
        step2 = input("> ")
        if step2 == "1" or step2 == "Droite":
            step2 = "droite"
        elif step2 == "2" or step2 == "Gauche":
            step2 = "gauche"
        elif step2 == "3" or step2 == "Bas":
            step2 = "bas"
        elif step2 == "4" or step2 == "Haut":
            step2 = "haut"
        move(step2)
    map = Map(map.place)
    if map.place < 5:
        affichage(verif)
        verif = map.place
        game(verif, map)
    else:
        print("BRAVO !!! Vous avez fini le jeu \n")


game(verif, map)
