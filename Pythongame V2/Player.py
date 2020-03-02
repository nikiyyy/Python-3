from random import randint

class Player():
    race="human"
    max_movement_points=5
    movement_point=0
    maxHealth=50
    curHealth=0
    Y_cord=0
    X_cord=0
    combatmap=[]
    
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
    
    def cooldown(self):
        self.movement_points=self.max_movement_points