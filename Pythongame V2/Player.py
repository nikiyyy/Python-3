from random import randint
from math import ceil
import Items 

class Player():
    race="human"
    name="stranger"
    max_movement_points=5
    movement_point=0
    maxHealth=50
    curHealth=0
    Y_cord=0
    X_cord=0
    combatmap=[]
    level=1
    equippedOH=None # off hand equipment
    equippedW=Items.weapon5 # Main hand equipment
    equippedA=None
    stats={"STR":5,"END":5,"DIP":10,"DEX":2,"PER":2,"INT":1}
    
    
    
    def __init__ (self,race,max_movement_points,maxHealth):
        self.race=race
        self.max_movement_points=max_movement_points
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.cooldown()
        
    def am_i_touching(self,Enemy,karta):
        if karta[self.Y_cord+1][self.X_cord]=="3" and karta[Enemy.Y_cord-1][Enemy.X_cord]=="2":
            return True
        elif karta[self.Y_cord-1][self.X_cord]=="3" and karta[Enemy.Y_cord+1][Enemy.X_cord]=="2":
            return True
        elif karta[self.Y_cord][self.X_cord+1]=="3" and karta[Enemy.Y_cord][Enemy.X_cord-1]=="2":
            return True
        elif karta[self.Y_cord][self.X_cord-1]=="3" and karta[Enemy.Y_cord][Enemy.X_cord+1]=="2":
            return True
        
        elif karta[self.Y_cord+1][self.X_cord+1]=="3" and karta[Enemy.Y_cord-1][Enemy.X_cord-1]=="2":
            return True
        elif karta[self.Y_cord-1][self.X_cord-1]=="3" and karta[Enemy.Y_cord+1][Enemy.X_cord+1]=="2":
            return True
        elif karta[self.Y_cord+1][self.X_cord-1]=="3" and karta[Enemy.Y_cord-1][Enemy.X_cord+1]=="2":
            return True
        elif karta[self.Y_cord-1][self.X_cord+1]=="3" and karta[Enemy.Y_cord+1][Enemy.X_cord-1]=="2":
            return True
        else: return False
    
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
    
    def Perry_chance(self):
        return 5 
    
    def Hit_chance(self):
        hitchanse=randint(1,21)
        if self.equippedW != None and self.equippedW.damage_type=='P' and hitchanse+5>=20:
            hitchanse+=5
            
        if hitchanse == 20:
            print("Critical strike!"*50)
            return 1000
        
        return hitchanse+self.level+ceil(self.stats["DEX"]/2)
    
    def cooldown(self):
        self.movement_points=self.max_movement_points
        
    def genirate_damage(self):
        if self.equippedW==None:
            return randint(1,3)+self.stats["STR"]
        else: return randint(1,3)+self.equippedW.damage+self.stats["STR"]
    
    def take_damage(self, enemy,crit = None):
        damage=enemy.genirate_damage()
        if self.equippedA != None:
            print(self.equippedA.name + " blocks "+ str(damage-self.equippedA.defence) + " damage!")
            self.curHealth-=damage-self.equippedA.defence
        else:
            self.curHealth-=damage