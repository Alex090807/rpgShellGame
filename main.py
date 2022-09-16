#Imports
import random
from email.base64mime import header_length
from typing_extensions import Self


#Weapons
class Weapon01: 
    damage = 10

class Weapon02: 
    damage = 15

class Weapon03: 
    damage = 20

class Weapon04: 
    damage = 25

weaponsArray = [Weapon01().damage, Weapon02().damage, Weapon03().damage, Weapon04().damage]

#Armor
class Armor01: 
    protection = 5

class Armor02: 
    protection = 10

class Armor03: 
    protection = 15

class Armor04: 
    protection = 20

armorsArray = [Armor01().protection, Armor02().protection, Armor03().protection, Armor04().protection]


#lifePackages
class lifePackages01: 
    life = 20

class lifePackages02: 
    life = 25

class lifePackages03: 
    life = 30

class lifePackages04: 
    life = 35

lifePackagesArray = [lifePackages01().life, lifePackages02().life, lifePackages03().life, lifePackages04().life]


#LootBoxes
lootBoxes = ["lootBox01", "lootBox02", "lootBox02"]

class WeaponLootBox01: 
    availableLoot = [weaponsArray[0], weaponsArray[1]] #90% - 10% - 0.1% = 100%

class WeaponLootBox02: 
    availableLoot = [weaponsArray[0], weaponsArray[1], weaponsArray[2]] #50% - 45% - 5% = 100%

class WeaponLootBox02: 
    availableLoot = [weaponsArray[0], weaponsArray[1], weaponsArray[2]] #15% - 60% - 15% = 100%



#USER PROFILE

class UserProfileTemplate:
    health= 100
    damage= 5
    protection= 0

userProfileGenerated = UserProfileTemplate()

#FONDAMENTAL FUNCTIONS

#WEAPON RANDOM LOOTBOX FUNCTIONS

def getWeaponLoot01():
    randomNumberWeapon = random.randint(1,100)

    if randomNumberWeapon <= 90:
        UserProfileTemplate.damage = [weaponsArray[0]]
    else:
        UserProfileTemplate.damage = [weaponsArray[1]]

    print(userProfileGenerated.damage)

def getWeaponLoot02():
    randomNumberWeapon = random.randint(1,100)

    if randomNumberWeapon in range(1,50):
        UserProfileTemplate.damage = [weaponsArray[0]]
    elif randomNumberWeapon in range(50,95):
        UserProfileTemplate.damage = [weaponsArray[1]]
    elif randomNumberWeapon in range(95,100):
        UserProfileTemplate.damage = [weaponsArray[2]]
    print(userProfileGenerated.damage)


def getWeaponLoot03():
    randomNumberWeapon = random.randint(1,100)

    if randomNumberWeapon in range(1,15):
        UserProfileTemplate.damage = [weaponsArray[0]]
    elif randomNumberWeapon in range(15,70):
        UserProfileTemplate.damage = [weaponsArray[1]]
    elif randomNumberWeapon in range(70,95):
        UserProfileTemplate.damage = [weaponsArray[2]]
    elif randomNumberWeapon in range(95,100):
        UserProfileTemplate.damage = [weaponsArray[3]]
    print(userProfileGenerated.damage)


#ARMOUR RANDOM LOOTBOX FUNCTIONS

def getArmorLoot01():
    randomNumberArmor = random.randint(1,100)

    if randomNumberArmor <= 90:
        UserProfileTemplate.damage = [armorsArray[0]]
    else:
        UserProfileTemplate.damage = [armorsArray[1]]

    print(userProfileGenerated.damage)

def getArmorLoot02():
    randomNumberArmor = random.randint(1,100)

    if randomNumberArmor in range(1,50):
        UserProfileTemplate.damage = [armorsArray[0]]
    elif randomNumberArmor in range(50,95):
        UserProfileTemplate.damage = [armorsArray[1]]
    elif randomNumberArmor in range(95,100):
        UserProfileTemplate.damage = [armorsArray[2]]
    print(userProfileGenerated.damage)


def getArmorLoot03():
    randomNumberArmor = random.randint(1,100)

    if randomNumberArmor in range(1,15):
        UserProfileTemplate.damage = [armorsArray[0]]
    elif randomNumberArmor in range(15,70):
        UserProfileTemplate.damage = [armorsArray[1]]
    elif randomNumberArmor in range(70,95):
        UserProfileTemplate.damage = [armorsArray[2]]
    elif randomNumberArmor in range(95,100):
        UserProfileTemplate.damage = [armorsArray[3]]
    print(userProfileGenerated.damage)



getArmorLoot03()