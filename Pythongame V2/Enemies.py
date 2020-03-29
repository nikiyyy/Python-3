from random import randint
from termcolor import colored
from math import ceil
import combat
import Items 

class Enemy(): #enemy e baseclass koto se nasledqva ot vsichko protivnici
    def __init__(self,name=None):
        self.name=name
        self.gen_inventory
    level=1
    alive=True
    Y_cord=0
    X_cord=0
    movement_points=2
    maxHealth=30
    curHealth=maxHealth
    armor=2
    inventory=[]
    color=0
    equippedW=None
    equippedA=None
    stats={"STR":5,"END":5,"DIP":10,"DEX":2,"PER":2,"INT":1}
    
    def action(self,karta,pobj):
        choise=randint(0,10)
        if choise<9:
            #damage=0
            combat.Attack(self, pobj)
            #if self.equippedW != None:
                
                #damage=self.genirate_damage()
                #pobj.curHealth-=damage
                #print("ENEMY Deals "+str(damage) +" damage with "+ self.equippedW.name)
                
            #else:
                #pobj.curHealth-=randint(1,5)
                #print("ENEMY ATTACKS! with fists")
                
    def take_damage(self, player, crit = None):
        damage=player.genirate_damage()
        if crit != None:
            damage*=2
            
        if self.equippedA != None:

            if self.equippedA.armour_type == 'H' and player.equippedW.damage_type == 'B':
                print("using a blunt weapon extdadamage")
                damage*=1.5
            elif self.equippedA.armour_type == 'H' and player.equippedW.damage_type == 'S':
                print("using a sword agains heavy armour")
                damage*=0.75
            elif self.equippedA.armour_type == 'L' and player.equippedW.damage_type == 'S':
                print("using a sword agains light armour")
                damage*=1.5

            if damage-self.equippedA.defence <=0:
                print(self.equippedA.name + " absorbes all the damage!")
            else:
                print(self.equippedA.name + " blocks "+ str(damage-self.equippedA.defence) + " damage!")
                self.curHealth-=damage-self.equippedA.defence

        else:
            self.curHealth-=damage*2
        if self.curHealth<=0:
            player.combatmap=self.died(player.combatmap)        

    def genirate_damage(self):
        if self.equippedW==None:
            return randint(1,3)+self.stats["STR"]
        else: return randint(1,3)+self.equippedW.damage+self.stats["STR"]
        
    def died(self,karta):
        karta[self.Y_cord][self.X_cord]="1"
        self.movement_points=0    
        self.alive=False
        self.curHealth=0
        return karta
    
    def printme(self):
        if self.color==1:
            print("|"+colored('██', 'cyan'),end = '')
        elif self.color==2:
            print("|"+colored('▒▒', 'grey','on_red'),end = '')
        elif self.color==3:
            print("|"+colored('██', 'magenta'),end = '')
        elif self.color==4:
            print("|"+colored('██', 'red'),end = '')
        elif self.color==5:
            print("|"+colored('██', 'green'),end = '')

    def gen_inventory(self):
        weapon_var=randint(0,9)
        print(weapon_var)
        self.inventory.append(Items.Mweapons[weapon_var])
        self.equippedW=Items.Mweapons[weapon_var]
        
        armor_var=randint(0,9)
        print(armor_var)
        self.inventory.append(Items.Armour[armor_var])
        self.equippedA=Items.Armour[armor_var]
    
    def Dodege_chance(self):#s kakvo si oblechen,desxterity i level i se sravnqva sus hitchance na enemito
        if self.equippedA == None:
            hitchanse=randint(7,12)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'L' or self.equippedA.armour_type == 'C':
            hitchanse=randint(5,10)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'M':
            hitchanse=randint(3,7)+self.stats["DEX"]
        elif self.equippedA.armour_type == 'H':
            hitchanse=randint(0,5)+self.stats["DEX"]
        return (hitchanse+self.level)
    
    def Hit_chance(self):
        hitchanse=randint(1,21)
        return hitchanse+self.level+ceil(self.stats["DEX"]/2)
    
    def move(self,karta,pobj):#PX,PY
        try:
            #print("\nDebug\n"+"player X "+str(pobj.X_cord)+" player Y "+str(pobj.Y_cord)+"\n ENEMY X "+str(self.X_cord)+"ENEMY Y "+str(self.Y_cord)+"Debug")
            while self.movement_points>0:
                #diagonalno dvijenie
                if self.Y_cord > pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord-1] == "3" or karta[self.Y_cord-1][self.X_cord-1] == "0":
                        #print("\nobsticleA")
                        if karta[self.Y_cord-1][self.X_cord] == "1" :
                            #print("\nobsticleA1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1" :
                            #print("\nobsticleA2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleA3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord-1] == "2":
                        #print("\nearplayerA")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord-=1
                    self.movement_points-=1
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if  karta[self.Y_cord+1][self.X_cord+1] == "3" or karta[self.Y_cord+1][self.X_cord+1] == "0":
                        #print("\nobsticleB")
                        if karta[self.Y_cord+1][self.X_cord] == "1":
                            #print("\nobsticleB1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord+1] == "1":
                            #print("\nobsticleB2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleB3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord+1][self.X_cord+1] == "2":
                        #print("\nearplayerB")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord > pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord+1] == "3" or karta[self.Y_cord-1][self.X_cord+1] == "0":
                        #print("\nobsticleC")
                        if karta[self.Y_cord-1][self.X_cord] == "1":
                            #print("\nobsticleC1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1":
                            #print("\nobsticleC2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleC3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord+1] == "2":
                        #print("nearplayerC")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord+1][self.X_cord-1] == "3" or karta[self.Y_cord+1][self.X_cord-1] == "0":
                         #print("\nobsticleD")
                         if karta[self.Y_cord+1][self.X_cord] == "1":
                            #print("\nobsticleD1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                         elif karta[self.Y_cord][self.X_cord-1] == "1":
                           #print("\nobsticleD2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                         else:
                            #print("\nobsticleD3")
                            break
                         karta[self.Y_cord][self.X_cord]="3"
                         continue
                    
                    #enqountered player
                    elif karta[self.Y_cord+1][self.X_cord-1] == "2":
                        #print("\nearplayerD")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.X_cord-=1
                    self.movement_points-=1
                 #single axis movement
                elif self.Y_cord > pobj.Y_cord :
                    if karta[self.Y_cord-1][self.X_cord] == "3" or karta[self.Y_cord-1][self.X_cord] == "0":
                        #print("\nobsticleE")
                        if karta[self.Y_cord-1][self.X_cord-1] == "1":
                            #print("\nobsticleE2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            #print("\nobsticleE1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleE3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord] == "2":
                         #print("\nearplayerE")
                         if self.movement_points>0:
                             self.action(karta,pobj)
                         break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.movement_points-=1
                
                
                elif self.Y_cord < pobj.Y_cord :
                    if karta[self.Y_cord+1][self.X_cord] == "3" or karta[self.Y_cord+1][self.X_cord] == "0":
                        #print("\nobsticleF")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            #print("\nobsticleF2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord+1][self.X_cord+1] == "1":
                            #print("\nobsticleF1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleF3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord+1][self.X_cord] == "2":
                        #print("nearplayerF")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.movement_points-=1
                    
                elif self.X_cord > pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord-1] == "3" or karta[self.Y_cord][self.X_cord-1] == "0":
                        #print("\nobsticleG")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            #print("\nobsticleG1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord-1] == "1":
                            #print("\nobsticleG2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleG3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    if karta[self.Y_cord][self.X_cord-1] == "2":
                        #print("\nearplyerG")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.X_cord-=1
                    self.movement_points-=1  
                    
                elif self.X_cord < pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord+1] == "3" or karta[self.Y_cord][self.X_cord+1] == "0":
                        #print("\nobsticleH")
                        if karta[self.Y_cord+1][self.X_cord+1] == "1":
                            #print("\nobsticleH1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            #print("\nobsticleH2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            #print("\nobsticleH3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord][self.X_cord+1] == "2":
                        #print("\nearplayerH")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.X_cord+=1
                    self.movement_points-=1
                else:
                    break
    
                karta[self.Y_cord][self.X_cord]="3"
            if self.alive==True:
                self.movement_points=2
            return karta
        except IndexError:
            return karta
    
class Placeholder(Enemy):
    maxHealth=0
    curHealth=maxHealth
    
class Thug(Enemy):
    maxHealth=50
    curHealth=maxHealth
  
class Bandit(Enemy):
    maxHealth=60
    curHealth=maxHealth
    
class Pit_Fighter(Enemy):
    maxHealth=70
    curHealth=maxHealth
        
class Guard(Enemy):
    maxHealth=80
    curHealth=maxHealth
