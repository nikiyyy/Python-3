from random import randint

class Enemy(): #enemy e baseclass koto se nasledqva ot vsichko protivnici
    def __init__(self,name=None):
        self.name=name
        self.gen_inventory
        
    alive=True
    Y_cord=0
    X_cord=0
    movement_points=2
    maxHealth=30
    curHealth=maxHealth
    armor=2
    inventory=["1","2"]
    
    def action(self,karta,pobj):
        choise=randint(0,10)
        if choise<9:
            pobj.curHealth-=randint(1,8)
            print("ENEMY ATTACKS! GAHHH")
        
    def died(self,karta):
        karta[self.Y_cord][self.X_cord]="1"
        self.movement_points=0    
        self.alive=False
        self.curHealth=0
        return karta
    
    def gen_inventory(self):
        pass
    
    def move(self,karta,pobj):#PX,PY
        try:
            print("\nDebug\n"+"player X "+str(pobj.X_cord)+" player Y "+str(pobj.Y_cord)+"\n ENEMY X "+str(self.X_cord)+"ENEMY Y "+str(self.Y_cord)+"Debug")
            while self.movement_points>0:
                #diagonalno dvijenie
                if self.Y_cord > pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord-1] == "3" or karta[self.Y_cord-1][self.X_cord-1] == "0":
                        print("\nobsticleA")
                        if karta[self.Y_cord-1][self.X_cord] == "1" :
                            print("\nobsticleA1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1" :
                            print("\nobsticleA2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleA3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord-1] == "2":
                        print("\nearplayerA")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord-=1
                    self.movement_points-=1
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if  karta[self.Y_cord+1][self.X_cord+1] == "3" or karta[self.Y_cord+1][self.X_cord+1] == "0":
                        print("\nobsticleB")
                        if karta[self.Y_cord+1][self.X_cord] == "1":
                            print("\nobsticleB1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord+1] == "1":
                            print("\nobsticleB2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleB3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord+1][self.X_cord+1] == "2":
                        print("\nearplayerB")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord > pobj.Y_cord and self.X_cord < pobj.X_cord:
                    if karta[self.Y_cord-1][self.X_cord+1] == "3" or karta[self.Y_cord-1][self.X_cord+1] == "0":
                        print("\nobsticleC")
                        if karta[self.Y_cord-1][self.X_cord] == "1":
                            print("\nobsticleC1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.movement_points-=1
                            
                        elif karta[self.Y_cord][self.X_cord-1] == "1":
                            print("\nobsticleC2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleC3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord+1] == "2":
                        print("nearplayerC")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.X_cord+=1
                    self.movement_points-=1                
    
                elif self.Y_cord < pobj.Y_cord and self.X_cord > pobj.X_cord:
                    if karta[self.Y_cord+1][self.X_cord-1] == "3" or karta[self.Y_cord+1][self.X_cord-1] == "0":
                         print("\nobsticleD")
                         if karta[self.Y_cord+1][self.X_cord] == "1":
                            print("\nobsticleD1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.movement_points-=1
                            
                         elif karta[self.Y_cord][self.X_cord-1] == "1":
                            print("\nobsticleD2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.X_cord-=1
                            self.movement_points-=1
                         else:
                            print("\nobsticleD3")
                            break
                         karta[self.Y_cord][self.X_cord]="3"
                         continue
                    
                    #enqountered player
                    elif karta[self.Y_cord+1][self.X_cord-1] == "2":
                        print("\nearplayerD")
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
                        print("\nobsticleE")
                        if karta[self.Y_cord-1][self.X_cord-1] == "1":
                            print("\nobsticleE2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            print("\nobsticleE1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleE3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    elif karta[self.Y_cord-1][self.X_cord] == "2":
                         print("\nearplayerE")
                         if self.movement_points>0:
                             self.action(karta,pobj)
                         break
    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord-=1
                    self.movement_points-=1
                
                
                elif self.Y_cord < pobj.Y_cord :
                    if karta[self.Y_cord+1][self.X_cord] == "3" or karta[self.Y_cord+1][self.X_cord] == "0":
                        print("\nobsticleF")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            print("\nobsticleF2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord+1][self.X_cord+1] == "1":
                            print("\nobsticleF1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleF3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord+1][self.X_cord] == "2":
                        print("nearplayerF")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                    
                    karta[self.Y_cord][self.X_cord]="1"
                    self.Y_cord+=1
                    self.movement_points-=1
                    
                elif self.X_cord > pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord-1] == "3" or karta[self.Y_cord][self.X_cord-1] == "0":
                        print("\nobsticleG")
                        if karta[self.Y_cord+1][self.X_cord-1] == "1":
                            print("\nobsticleG1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord-=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord-1] == "1":
                            print("\nobsticleG2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord-=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleG3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    if karta[self.Y_cord][self.X_cord-1] == "2":
                        print("\nearplyerG")
                        if self.movement_points>0:
                            self.action(karta,pobj)
                        break
                        
                    karta[self.Y_cord][self.X_cord]="1"
                    self.X_cord-=1
                    self.movement_points-=1  
                    
                elif self.X_cord < pobj.X_cord :
                    if karta[self.Y_cord][self.X_cord+1] == "3" or karta[self.Y_cord][self.X_cord+1] == "0":
                        print("\nobsticleH")
                        if karta[self.Y_cord+1][self.X_cord+1] == "1":
                            print("\nobsticleH1")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord+=1
                            self.X_cord+=1
                            self.movement_points-=1
                        elif karta[self.Y_cord-1][self.X_cord+1] == "1":
                            print("\nobsticleH2")
                            karta[self.Y_cord][self.X_cord]="1"
                            self.Y_cord-=1
                            self.X_cord+=1
                            self.movement_points-=1
                        else:
                            print("\nobsticleH3")
                            break
                        karta[self.Y_cord][self.X_cord]="3"
                        continue
                    
                    elif karta[self.Y_cord][self.X_cord+1] == "2":
                        print("\nearplayerH")
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
