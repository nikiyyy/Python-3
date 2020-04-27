import Items 

class shop():
    #special inventory items sold by player for 24 hours
    #reputation with player
    #

  def  __init__(self):
      self.boughtItems=[]
  
  def menu(self,player):
      while True:
          izbor=input("1. buy 2. sell 3.exit")
          if izbor=="1":
              availible=[]
              index=0
              availible.extend(Items.Mweapons)
              for i in availible:
                  print(index,i,i.value)
                  index+=1
              buy=input("enter the coresponding number")   
              if player.money>=availible[int(buy)].value:
                  player.money-=player.money-availible[int(buy)].value
                  player.Inventory.append(availible[int(buy)])
              else:
                  print("not enough gold")
              
          elif izbor=="2":
              index=0
              print(player.money,"money")
              for i in player.Inventory:
                  print(index,i,i.value)
                  index+=1
              sell=input("enter the coresponding number")
              player.money+=player.Inventory[int(sell)].value
              #add to special items
              self.boughtItems.append(player.Inventory[int(sell)])
              del player.Inventory[int(sell)]
              
          elif izbor=="3":
              break

geniral_goods=shop()