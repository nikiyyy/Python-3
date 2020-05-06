import combat as comb
import Player as PL
import Database as DB
import market
from datetime import datetime

player=PL.Player("human",7,880)
#comb.Combat(player,5,"Thug",emem2type="Bandit",emem3type="Pit_Fighter",emem4type="Pit_Fighter",emem5type="Pit_Fighter")             
#comb.Combat(player,2,"Thug",enemNam1="george",emem2type="Bandit")     
#dcomb.Combat(player,1,"Thug",enemNam1="bob") 


while True:
    izbor=input("\n1.Fight\n2.Open inventory\n3.Player progress\n4.Shop\n5.Save game\n6.Load game \n7.Exit")
    if izbor == "1":
        comb.Combat(player,2,"Thug",enemNam1="george",emem2type="Bandit")  
        player.reset()
    elif izbor == "2":
        player.Inventory_manage("menu")
    elif izbor == "3":
        player.atribute_poins()
    elif izbor == "4":
        market.geniral_goods.menu(player)
    elif izbor == "5":
        savename = input("chose a save name")
        
        if player.equippedOH==None and player.equippedW==None and player.equippedA==None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel,None, None, None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH!=None and player.equippedW==None and player.equippedA==None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH==None and player.equippedW!=None and player.equippedA==None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH==None and player.equippedW==None and player.equippedA!=None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH!=None and player.equippedW!=None and player.equippedA==None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,None,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH!=None and player.equippedW==None and player.equippedA!=None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, None,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        elif player.equippedOH==None and player.equippedW!=None and player.equippedA!=None:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, None, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))
        
        else:
            DB.add_row(savename,player.race,player.name,player.specialisation.profession,player.max_movement_points,player.maxEnergy,player.maxHealth,player.curHealth,player.XPlevel, player.equippedOH.name, player.equippedW.name,player.equippedA.name,player.compressDictValues(player.stats), player.compressDictValues(player.skills),player.ability_points,player.money,player.XP,player.compressInventory(),datetime.now().strftime("%d.%m.%Y/%R"))#stats, skill, abp, money, XP, inv
    
    elif izbor == "6":
        DB.view()
        loald = input("chose a save name to load")
        player.loadFromFile(DB.load(loald))
    elif izbor == "7":
        print("end game")   
        break
    else:print("invalid input")