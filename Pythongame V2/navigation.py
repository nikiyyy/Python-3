import combat as comb
import Player as PL
import Database as DB
import market

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
        DB.add_row(savename,player.XP)
    elif izbor == "6":
        DB.view()
        loald = input("chose a save name to load")
        player.XP=DB.load(loald)[0][1]
    elif izbor == "7":
        print("end game")   
        break
    else:print("invalid input")