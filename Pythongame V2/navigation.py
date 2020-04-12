import combat as comb
import Player as PL


player=PL.Player("human",7,880)
#comb.Combat(player,5,"Thug",emem2type="Bandit",emem3type="Pit_Fighter",emem4type="Pit_Fighter",emem5type="Pit_Fighter")             
#comb.Combat(player,2,"Thug",enemNam1="george",emem2type="Bandit")     
#dcomb.Combat(player,1,"Thug",enemNam1="bob") 


while True:
    izbor=input("\n1.Fight\n2.Open inventory\n3.Player progress\n4.Save game\n5.Load game \n6.Exit")
    if izbor == "1":
        comb.Combat(player,2,"Thug",enemNam1="george",emem2type="Bandit")  
        player.reset()
    elif izbor == "2":
        player.Inventory_manage("menu")
    elif izbor == "3":
        player.atribute_poins()
    elif izbor == "4":
        print("WIP")
    elif izbor == "5":
        print("WIP")
    elif izbor == "6":
        print("end game")   
        break
    else:print("invalid input")