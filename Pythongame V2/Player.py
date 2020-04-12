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
    equippedOH=None#Items.shield3 # off hand equipment
    equippedW=None#Items.weapon69 # Main hand equipment
    equippedA=Items.armour8
    stats={"STR":5,"END":5,"DIP":10,"DEX":2,"PER":2,"INT":1}
    XP=0
    XPlevel=1
    XPcaps=(100,225,350,500,800)
    ability_points=0
    money=0
    Inventory=[Items.armour8,Items.weapon69,Items.weapon10,Items.armour7,Items.shield2,Items.weapon2,Items.weapon9]
    
    def __init__ (self,race,max_movement_points,maxHealth):
        self.race=race
        self.max_movement_points=max_movement_points
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.cooldown()
        
    def reset(self):
        self.combatmap=[]
    
    def get_xp(self,gain):
        self.XP+=gain
        #print("vleze {}".format(self.XPlevel))
        if self.XP>=self.XPcaps[self.XPlevel-1]:
            print(self.XPcaps[(self.XPlevel)])
            self.XPlevel+=1
            self.ability_points+=1
            print("level up")
            
    def get_gold(self,gain):
        self.money+=gain

    def atribute_poins(self):
        print("XP {}/{}\nLevel {}\nAtribute points {}".format(self.XP,self.XPcaps[self.XPlevel-1],self.XPlevel,self.ability_points))
        print("STATS:\n1. Strenght: {}\n2. Endurance: {}\n3. Deplomacy: {}\n4. Dexterity: {}\n5. Perception: {}\n6. Inteligence: {}".format(Player.stats["STR"],Player.stats["END"],Player.stats["DIP"],Player.stats["DEX"],Player.stats["PER"],Player.stats["INT"]))
        while self.ability_points != 0:
            izb=input("Whith stat do you wnat to increase?\nPress the coresponding number!")
            if izb=='1':
                Player.stats["STR"]+=1
                self.ability_points-=1
            elif izb=='2':
                Player.stats["END"]+=1
                self.ability_points-=1
            elif izb=='3':
                Player.stats["DIP"]+=1
                self.ability_points-=1
            elif izb=='4':
                Player.stats["DEX"]+=1
                self.ability_points-=1
            elif izb=='5':
                Player.stats["PER"]+=1
                self.ability_points-=1
            elif izb=='6':
                Player.stats["INT"]+=1
                self.ability_points-=1
            else: pass
    
    def char_create():
        pass
    
    def save_game(world_obj):
        pass
    
    def Load_game():
        pass
    
    def callmenu():
        pass
    
    def Inventory_manage(self,Called_from):
        print("gold: {}\n\nWearing {}\nweaponMH {}\nweaponOH {}\nhealth {}/{}\n".format(self.money,self.equippedA,self.equippedW,self.equippedOH,self.curHealth,self.maxHealth))
        
        for i in self.Inventory:
            print(i)
        izbor=int(input("\n1.Change armor\n2.Change weapon\n3.Use consumable\n4.Unequip\5.Delete item"))
        if izbor==1 :
            try:
                available=[n for n in self.Inventory if isinstance(n,Items.C_armour)]
                counter=0
                for i in available:
                    print(counter,i)
                    counter+=1
                izb_armor=input("choose the corespoding number")
                if self.equippedA!=None:
                    self.Inventory.append(self.equippedA)
                    self.equippedA=available[int(izb_armor)]
                    del self.Inventory[self.Inventory.index(available[int(izb_armor)])]
                else:
                    self.equippedA=available[int(izb_armor)]
                    del self.Inventory[self.Inventory.index(available[int(izb_armor)])]
            except:
                print("error")
                
        elif izbor==2: 
            available=[n for n in self.Inventory if isinstance(n,Items.M_weapons) or isinstance(n,Items.C_shield) or isinstance(n,Items.R_weapons)]
            counter=0
            for i in available:
                print(counter,i)                    
                counter+=1
            izb_weapon=input("choose the corespoding number")
             #2 hands   
            if available[int(izb_weapon)].hands == 2:
                if self.equippedW != None:
                    self.Inventory.append(self.equippedW)
                if self.equippedOH != None:
                    self.Inventory.append(self.equippedOH)
                self.equippedW=available[int(izb_weapon)]
                self.equippedOH=None
                del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                #onehand
            else:   
                if isinstance(available[int(izb_weapon)],Items.C_shield):
                    if self.equippedW != None and self.equippedW.hands==2:
                        self.Inventory.append(self.equippedW)
                        self.equippedW=None
                        self.equippedOH = available[int(izb_weapon)]
                        del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                    else:
                        if self.equippedOH != None:
                            self.Inventory.append(self.equippedOH)
                        self.equippedOH = available[int(izb_weapon)]
                        del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                else:
                    izb_hand=input("\ndo you want to equip on main or off hand\n1.Main 2.Off hand")
                    if izb_hand == '1':
                        if self.equippedW != None:
                            self.Inventory.append(self.equippedW)
                        self.equippedW = available[int(izb_weapon)]
                        del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                    elif izb_hand == '2':
                        if self.equippedW != None and self.equippedW.hands == 2:
                            self.Inventory.append(self.equippedW)
                            self.equippedW = None
                            self.equippedOH = available[int(izb_weapon)]
                            del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]
                        else:
                            if self.equippedOH != None:
                                self.Inventory.append(self.equippedOH)
                            self.equippedOH = available[int(izb_weapon)]
                            del self.Inventory[self.Inventory.index(available[int(izb_weapon)])]

        elif izbor==3: 
            available=[n for n in self.Inventory if isinstance(n,Items.C_consumable)]
            counter=0
            for i in available:
                print(counter,i)                    
                counter+=1
                
        elif izbor==4: print("WIP")
        
        elif izbor==5: print("WIP")

    
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
        
    def genirate_damage_offhand(self):
        if self.equippedOH==None or isinstance(self.equippedOH, Items.C_shield):
            return 0
        else: return (randint(1,3)+self.equippedOH.damage+self.stats["STR"])//2
        
    def Block_chance(self):
            if isinstance(self.equippedOH, Items.C_shield):
                return randint(self.equippedOH.defence//2,self.equippedOH.defence)
            else: return randint(0,5)
     
    def take_damage(self, enemy, crit = None):
        damage=enemy.genirate_damage()
        off_damage=enemy.genirate_damage_offhand()
        print("offhand damage",off_damage)
        if crit != None:
            damage*=2
            
        if self.equippedA != None:

            if self.equippedA.armour_type == 'H' and enemy.equippedW.damage_type == 'B':
                print("using a blunt weapon extdadamage")
                damage*=1.25
            elif self.equippedA.armour_type == 'H' and enemy.equippedW.damage_type == 'S':
                print("using a sword agains heavy armour")
                damage*=0.75
            elif self.equippedA.armour_type == 'L' and enemy.equippedW.damage_type == 'S':
                print("using a sword agains light armour")
                damage*=1.25
            if off_damage != 0:
                if self.equippedA.armour_type == 'H' and enemy.equippedOH.damage_type == 'B':
                    print("using a blunt weapon extdadamage")
                    off_damage*=1.25
                elif self.equippedA.armour_type == 'H' and enemy.equippedOH.damage_type == 'S':
                    print("using a sword agains heavy armour")
                    off_damage*=0.75
                elif self.equippedA.armour_type == 'L' and enemy.equippedOH.damage_type == 'S':
                    print("using a sword agains light armour")
                    off_damage*=1.25

            if (damage+off_damage)-self.equippedA.defence//2 <=0:
                print(self.equippedA.name + " absorbes all the damage!")
            else:
                print(self.equippedA.name + " blocks "+ str((damage+off_damage)-self.equippedA.defence//2) + " damage!")
                self.curHealth-=(damage+off_damage)-self.equippedA.defence//2

        else:
            self.curHealth-=(damage+off_damage)*2
        if self.curHealth<=0:
            enemy.combatmap=self.died(enemy.combatmap)        