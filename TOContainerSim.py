from random import randint
import numpy as np
from colorama import init, Fore, Style
init(autoreset=True)

global tankoins, crystals, nitro, da, dp, batteries, golds, premium, containers, coinboxes, ultraconts, health
tankoins = 500
crystals = 10000
da, dp, nitro, health = 100, 100, 100, 10
batteries, golds = 5, 5
premium = 0
containers, coinboxes, ultraconts = 0, 0, 0

def openContainer():
    global tankoins, crystals, nitro, da, dp, batteries, golds,premium, containers, coinboxes, ultraconts, health

    commonProbability = 0.56250000
    lessCommonProbability = 0.25000000
    rareProbability = 0.12500000
    exoticProbability = 2.00000000 / 48.00000000
    for _ in range(1):
        seed = np.random.random()
        if seed <= commonProbability:
            item = commonItems[randint(0, len(commonItems) - 1)]
            print(Style.BRIGHT + Fore.YELLOW + item)
            #["3500 Crystals Pack", "125 Mines", "125 Speed Boost", "125 Boosted Armor","125 Boosted Damage", "5 Goldboxes Set", "3 Tankoins"]
            if item == "3500 Crystals Pack": crystals += 3500
            elif item == "5 Goldboxes Set": golds += 5
            elif item == "3 Tankoins": tankoins += 3
            elif item == "50 Batteries": batteries += 50
            elif item == "125 Speed Boost": nitro += 125
            elif item == "125 Boosted Damage": dp += 125
            elif item == "125 Boosted Armor": da += 125

        elif commonProbability < seed <= commonProbability + lessCommonProbability:
            item = lessCommonItems[randint(0, len(lessCommonItems) - 1)]
            print(Style.BRIGHT + Fore.GREEN + item)
            #["10000 Crystals Pack", "125 Repair Kits", "50 Batteries", "100 All of Supplies Pack","3 Days of Premium", "10 Goldboxes Set", "10 Tankoins"]
            if item == "10000 Crystals Pack": crystals += 10000
            elif item == "100 All of Supplies Pack":
                da += 100
                dp += 1000
                nitro += 100
                batteries += 100
            elif item == "10 Goldboxes Set": golds += 10
            elif item == "10 Tankoins": tankoins += 10
            elif item == "50 Batteries": batteries += 50
            elif item == "3 Days of Premium": premium += 3
            elif item == "125 Repair Kits": health += 125

        elif commonProbability + lessCommonProbability < seed <= commonProbability + lessCommonProbability + rareProbability:
            item = rareItems[randint(0, len(rareItems) - 1)]
            print(Style.BRIGHT + Fore.BLUE + item)
            #["25000 Crystals Pack", "125 Batteries", "250 All of Supplies Pack", "100 Tankoins", "10 Days of Premium", "Coinbox", "25 Goldboxes Set"]
            if item == "25000 Crystals Pack": crystals += 25000
            elif item == "250 All of Supplies Pack":
                da += 250
                dp += 250
                nitro += 250
                batteries += 250
            elif item == "25 Goldboxes Set": golds += 25
            elif item == "100 Tankoins": tankoins += 100
            elif item == "125 Batteries": batteries += 125
            elif item == "10 Days of Premium": premium += 10
            elif item == "Coinbox": coinboxes += 1

        elif commonProbability + lessCommonProbability + rareProbability < seed <= commonProbability + lessCommonProbability + exoticProbability:
            item = exoticItems[randint(0, len(exoticItems) - 1)]
            print(Style.BRIGHT + Fore.PURPLE + item)
            #["50000 Crystals Pack", "500 All of Supplies Pack", "50 Goldboxes Set", "3000 Tankoins"]
            if item == "50000 Crystals Pack": crystals += 50000
            elif item == "500 All of Supplies Pack":
                da += 500
                dp += 500
                nitro += 500
                batteries += 500
            elif item == "50 Goldboxes Set": golds += 50
            elif item == "3000 Tankoins": tankoins += 3000

        else:
            item = legendaryItems[randint(0, len(legendaryItems) - 1)]
            print(Style.BRIGHT + Fore.RED + item)
            #["1000000 Crystals Pack", "Coinbox 10 Boxes", "1000000 Tankoins"]
            if item == "100000 Crystals Pack": crystals += 100000
            elif item == "Coinbox 10 boxes": coinboxes += 10
            elif item == "1000000 Tankoins": tankoins += 1000000
    return True

def collectReward(N):
	print("Opening", N, "Containers!\n")
	for i in range(N): openContainer()
	return True


global hulls, hullAugments
hulls = [
    "Wasp", "Hornet", "Hopper", "Hunter", "Viking", "Crusader", "Dictator",
    "Mammoth", "Ares", "Titan"
]

hullAugments = [
    "Heat Resistance", "Cold Resistance", "Heat Immunity", "Cold Immunity",
    "Lightweight Construction", "Heavyweight Construction", "EMP Immunity",
    "Stun Immunity", "AP Immunity"
]

global commonItems
commonItems = [
    "3500 Crystals Pack", "125 Mines", "125 Speed Boost", "125 Boosted Armor",
    "125 Boosted Damage", "5 Goldboxes Set", "3 Tankoins"
]

global lessCommonItems
lessCommonItems = [
    "10000 Crystals Pack", "125 Repair Kits", "50 Batteries",
    "100 All of Supplies Pack", "3 Days of Premium", "10 Goldboxes Set",
    "10 Tankoins"
]

global rareItems
rareItems = [
    "25000 Crystals Pack", "125 Batteries", "250 All of Supplies Pack",
    "100 Tankoins", "10 Days of Premium", "Coinbox", "25 Goldboxes Set"
]

global exoticItems
exoticHullAugments = [
    hullAugments[j] + " for " + hulls[i] for j in range(len(hullAugments))
    for i in range(len(hulls))
]
fireAugments = [
    "Adrenaline", "High Pressure Pump for Firebird", "Incendiary Mix"
]
freezeAugments = [
    "Corrosive Mix", "Toxic Mix", "Shock Freee", "Arenaline",
    "High Pressure Pump for Freeze"
]
isidaAugments = ["Vampire Nanobots"]
hammerAugments = ["Duplet", "Dragon\'s Breath"]
thunderAugments = ["Sledgehammer Rounds"]
shaftAugments = [
    "Heavy Capacitors", "Light Capacitors", "Healing Emitters", "Rapid-Fire"
]
strikerAugments = [
    "Missile Launcher Cyclone", "Missile Launcher Uranium",
    "Stunning Missiles", "Remote-Control Rockets"
]
vulcanAugments = [
    "Incendiary Band", "Reinforced Aiming Transmission", "Rubberized Rounds"
]
twinsAugments = ["Heavy Plasmagun"]
ricochetAugments = ["Minus Field Stabilizer"]
magnumAugments = ["Harpoon"]
railgunAugments = [
    "Round Stabilization", "Round Destabilization", "Hyperspace Rounds",
    "Death Herald Compulsator", "Electromagnetic Accelerator",
    "Stun Rounds for Railgun", "Cryo Rounds for Railgun",
    "Incendiary Rounds for Railgun", "EMP Rounds for Railgun"
]
smokeyAugments = [
    "Autocannon", "Cryo Rounds for Smokey", "Incendiary Rounds for Smokey",
    "Stun Rounds for Smokey", "EMP Rounds for Smokey", "Sorted Ammunition",
    "High-Efficiency Aiming System"
]
exoticTurretAugments = fireAugments + freezeAugments + isidaAugments + hammerAugments + thunderAugments + shaftAugments + strikerAugments + vulcanAugments + twinsAugments + ricochetAugments + magnumAugments + railgunAugments + smokeyAugments
exoticItems = exoticHullAugments + exoticTurretAugments + [
    "50000 Crystals Pack", "500 All of Supplies Pack", "50 Goldboxes Set",
    "3000 Tankoins"
]

global legendaryItems
legendaryAugments = [
    "Blunderbuss", "Magnetic Pellets", "AP Sight", "Electromagnetic Salvo",
    "AP Rounds for Railgun", "AP Rounds for Smokey", "AP Freeze", "AP Salvo"
]
skins = ["XT", "Prime", "Legacy"]
legendarySkins = [
    hulls[j] + " " + skins[i] for j in range(len(hulls))
    for i in range(len(skins))
]
legendaryItems = legendaryAugments + [
    "1000000 Crystals Pack", "Coinbox 10 Boxes", "1000000 Tankoins"
] + legendarySkins

#collectReward(50)
while True:
    if crystals < 1500 and tankoins < 150: break
    print("You have", crystals, "crystals and", tankoins, "tankoins.\nDo you want to buy a container?")
    choice = input("Y/N ")
    if choice == "N": break
    howtopay = input("Crystals or Tankoins? ")
    if howtopay == "Crystals":
        if crystals < 1500:
            print("Invalid purchase")
            break
        else:
            crystals -= 1500
            containers += 1
            openCont = input("Do you want to open the container? Y/N ")
            if choice == "N": continue
            else: openContainer()
    if howtopay == "Tankoins":
        if tankoins < 150:
            print("Invalid purchase")
            break
        else:
            tankoins -= 150
            containers += 1
            openCont = input("Do you want to open the container? Y/N ")
            if choice == "N": continue
            else: openContainer()
