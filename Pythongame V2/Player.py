from random import randint
from math import ceil
import Items 
import Effects 
import Specialisations

class Player():
    race="human"
    name="stranger"
    specialisation=Specialisations.test
    max_movement_points=5
    movement_point=0
    maxHealth=50
    curHealth=0
    maxEnergy=50
    curEnergy=maxEnergy
    Y_cord=0
    X_cord=0
    combatmap=[]
    level=1
    equippedOH=None#Items.shield3 # off hand equipment
    equippedW=None#Items.weapon69 # Main hand equipment
    equippedA=Items.armour8
    stats={"STR":5,"END":5,"DIP":10,"DEX":2,"PER":2,"INT":1}
    skills={"One handed":5,"Two handed":5,"Throwing":5,"Shooting":5,"Blocking":5,"Heavy armour":5,"Medium armour":5,"Light armour":5,"Destruction magic":5,"Restoration magic":5}
    XP=0
    XPlevel=1
    XPcaps=(100,225,350,500,800)
    ability_points=0
    money=0
    Inventory=[Items.armour8,Items.weapon69,Items.weapon10,Items.armour7,Items.shield2,Items.weapon2,Items.weapon9,Items.R_weapon1,Items.potion1,Items.R_weapon4]
    effects=[]#{3:101},{15:101}
    
    def __init__ (self,race,max_movement_points,maxHealth):
        self.race=race
        self.max_movement_points=max_movement_points
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.maxHealth=maxHealth
        self.curHealth=maxHealth
        self.cooldown()
        
    def char_create(self):
        choise = input("What race are you?\n1.Human\n2.Elf\n3.Dwarf\n4.Orc")   
        
        if choise == 3:
            self.race = "dwarf"
            self.stats["END"]+=1
            
        elif choise == 2:
            self.race = "elf"
            self.stats["DEX"]+=1
            
        elif choise == 1:
            self.race = "human"
            self.stats["DIP"]+=1
    
        elif choise == 4:
            self.race = "orc"
            self.stats["STR"]+=1
            
        choise = input("what specialisation do you chose \n1.warrior\n2.ranger\n3.mage\n4.rogue")   
    
        if choise == 1:
            self.race = "dwarf"
            self.stats["END"]+=1
            
        elif choise == 2:
            self.race = "elf"
            self.stats["DEX"]+=1
            
        elif choise == 3:
            self.race = "human"
            self.stats["DIP"]+=1
    
        elif choise == 4:
            self.race = "orc"
            self.stats["STR"]+=1
            
            
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

    def spoils_of_war(self,enem1,emem2,enem3,enem4,enem5):
        loot=[]
        loot.extend(enem1.inventory)
        loot.extend(emem2.inventory)
        loot.extend(enem3.inventory)
        loot.extend(enem4.inventory)
        loot.extend(enem5.inventory)
        
        while True:
            index=0
            for i in loot:
                print(index,i)
                index+=1
            izbor=input("choose the corespoding number \ninput 'E' to exit")
            if izbor=='E' or izbor=='e':
                break
            self.Inventory.append(loot.pop(int(izbor)))

    def atribute_poins(self):
        print("XP {}/{}\nLevel {}\nAtribute points {}".format(self.XP,self.XPcaps[self.XPlevel-1],self.XPlevel,self.ability_points))
        print("STATS:\n1. Strenght: {}\n2. Endurance: {}\n3. Deplomacy: {}\n4. Dexterity: {}\n5. Perception: {}\n6. Inteligence: {}".format(Player.stats["STR"],Player.stats["END"],Player.stats["DIP"],Player.stats["DEX"],Player.stats["PER"],Player.stats["INT"]))
        for i in self.skills:
            print(i,Player.skills[i])
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
    
    def apply_effect(self,turns):
        
        for i in self.effects:
            #print(i.get(i.keys()))
            if list(i.keys())[0]>=turns:
                #print(list(i.keys())[0])
                #print(i[list(i.keys())[0]])
                for j in Effects.tupple_effects:
                    if j.ID == i[list(i.keys())[0]]:
                        print("afflicted with {} for {} tirns".format(j.name,list(i.keys())[0]-turns))
                        j.apply(self)
            else:
                print("expired")
            #check if turns is > effects.
        
    
    def Inventory_manage(self,Called_from):
        while True:
            print("gold: {}\n\nWearing {}\nweaponMH {}\nweaponOH {}\nhealth {}/{}\n".format(self.money,self.equippedA,self.equippedW,self.equippedOH,self.curHealth,self.maxHealth))
            
            for i in self.Inventory:
                print(i)
            izbor=int(input("\n1.Change armor\n2.Change weapon\n3.Use consumable\n4.Unequipn\n5.Delete item\n6. exit"))
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
                izb_consum=input("choose the corespoding number")
                available[int(izb_consum)].use(self)
                del self.Inventory[self.Inventory.index(available[int(izb_consum)])]
                    
            elif izbor==4: 
                izb_uniq=input("1. Wearing: {}\n2. weaponMH: {}\n3. weaponOH: {}".format(self.equippedA,self.equippedW,self.equippedOH))
                if izb_uniq == '1':
                    if self.equippedA != None:
                        self.Inventory.append(self.equippedA)
                        self.equippedA = None
                        
                    else: print("nothing to unequip")
                    
                elif izb_uniq == '2':
                    if self.equippedW != None:
                        self.Inventory.append(self.equippedW)
                        self.equippedW = None
                        
                    else: print("nothing to unequip")
                    
                elif izb_uniq == '3':
                    if self.equippedOH != None:
                        self.Inventory.append(self.equippedOH)
                        self.equippedOH = None
                        
                    else: print("nothing to unequip")
                    
            elif izbor == 5:
                counter=0
                for i in self.Inventory:
                    print(counter,i)                    
                    counter+=1
                izb_delete=input("choose the corespoding number")
                conformation=input("are you susre you whant to delete {} \n1.Yes \n2.No".format(self.Inventory[int(izb_delete)]))
                if conformation == '1':
                    del self.Inventory[int(izb_delete)]
            elif izbor == 6:
                break
    
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
            hitchanse=randint(5,10)+self.stats["DEX"]+randint(0,self.skills["Heavy armour"]//6)
        elif self.equippedA.armour_type == 'M':
            hitchanse=randint(3,7)+self.stats["DEX"]+randint(0,self.skills["Heavy armour"]//8)
        elif self.equippedA.armour_type == 'H':
            hitchanse=randint(0,5)+self.stats["DEX"]+randint(0,self.skills["Heavy armour"]//10)
        return (hitchanse+self.level)
    
    def Hit_chance(self):
        hitchanse=randint(1,21)
        if self.equippedW != None and isinstance(self.equippedW, Items.R_weapons):
            return hitchanse+self.level+ceil(self.stats["PER"]/2)
        else:
            if self.equippedW != None and self.equippedW.damage_type=='P' and hitchanse+5>=20:
                hitchanse+=5
                
            if hitchanse == 20:
                return 1000
            
            return hitchanse+self.level+ceil(self.stats["DEX"]/2)
    
    
    def cooldown(self):
        self.movement_points=self.max_movement_points
        
    def genirate_damage(self):
        
        skillDamage=0
        if self.equippedW != None and self.equippedW.hands == 1:
            if isinstance(self.equippedW, Items.M_weapons):
                skillDamage=self.skills["One handed"]//10
            else:
                skillDamage=self.skills["Throwing"]//10
                
        elif self.equippedW != None and self.equippedW.hands == 2:
            if isinstance(self.equippedW, Items.M_weapons):
                skillDamage=self.skills["Two handed"]//10
            else:
                skillDamage=self.skills["Shooting"]//10
            
            #for off hand
        if self.equippedOH != None:
            if isinstance(self.equippedOH, Items.M_weapons):
                skillDamage=self.skills["One handed"]//10
            elif isinstance(self.equippedOH,Items.R_weapons):
                skillDamage=self.skills["Throwing"]//10
        
        
        if self.equippedW==None:
            return randint(1,4)+self.stats["STR"]
        else: return randint(1,3)+randint(1,self.equippedW.damage)+self.stats["STR"]+skillDamage
        
    def genirate_damage_offhand(self):
        if self.equippedOH==None or isinstance(self.equippedOH, Items.C_shield):
            return 0
        else: return (randint(1,3)+self.equippedOH.damage+self.stats["STR"])//2
        
    def Block_chance(self):
        
            if isinstance(self.equippedOH, Items.C_shield):
                return randint(self.equippedOH.defence//2,self.equippedOH.defence)+randint(0,self.skills["Blocking"]//8)
            else: return randint(0,5)+randint(0,self.skills["Blocking"]//10)
     
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
        #ima shans da uvelichi nqkoi stat
        increase=randint(0,10)
        if increase == 0 and self.equippedA != None and self.equippedA.armour_type=='L':
            self.skills["Light armour"]+=1
        elif increase == 0 and self.equippedA != None and self.equippedA.armour_type=='M':
            self.skills["Medium armour"]+=1
        elif  increase == 0 and self.equippedA != None and self.equippedA.armour_type=='H':
            self.skills["Heavy armour"]+=1
            
        if self.equippedOH!= None and isinstance(self.equippedOH, Items.C_shield):
                self.skills["Blocking"]+=1