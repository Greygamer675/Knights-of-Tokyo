#Knights_of_Tokyo will be a simple text based rpg similiar to Chrono Trigger.
#List of things to add
#Classes
#Input interactions.
#Hero switching.
#Status effects
#Visuals?
#Armor and Magic Resist stats
#
#
import math

#All classes go here.
class Hero(object):
    name = ''
    Hp = ''
    Str = ''
    Mag = ''
    Dex = ''
    inventory = []

    def __init__(self,name,Hp,Str,Mag,Dex,Amr,Mr,inventory):
        self.name = name
        self.Hp = Hp
        self.Str = Str
        self.Mag = Mag
        self.Dex = Dex
        self.Inv = inventory

    def equip(item):
        if item in inventory:
            Hero.Str += item.Str


    def get_item(item):
        inventory.append(item)


inventory = []
def get_item(item):
    inventory.append(item)

class Item(object):
    name = ''
    Armor = ''
    Str = ''
    Mag = ''
    Dex = ''
    Magic Resist = ''
    def __init__(self,name,Hp,Str,Mag,Dex)

    def equip(item):
        if item in inventory:
            Hero.Str +=


    def get_item(item):
        inventory.append(item)



    def
class Man(object):
    name = ''
    Hp = ''
    Str = ''
    Mag = ''
    Dex = ''

    def __init__(self,name='Villager',Hp=11,Str=3,Mag=0,Dex=1)


