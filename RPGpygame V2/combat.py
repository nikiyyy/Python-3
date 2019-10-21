from random import randint
from termcolor import colored
from time import sleep

def genmap(x,y,terain,objpass=None ,caller=None,enemnum=1,enemy=None,enemy2=None,enemy3=None,enemy4=None,enemy5=None):   #caller = 1 - player your || caller = 2 - enemy tirn
    # tuk vliza samo vednuj v nachaloto na bitka
    biglist=[]
    cx=objpass.X_cord
    cy=objpass.Y_cord
    tempx=cx
    tempy=cy
    if objpass.combatmap==[]:
        cx=2
        cy=int(y/2)
        tempx=cx
        tempy=cy
        rowlist=[]
        for i in range(0,x): #generira teren - 0-obsicle 1-free 2-player 3-enemy1
            for j in range(0,y):
                if terain==0:
                    rowlist.append('1')
                elif terain==1:
                    if randint(0,(y*x)/5)==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==2:
                    if randint(0,int((y*x)/7))==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==3:
                    if randint(0,int((y*x)/10))==5:
                        rowlist.append('0') 
                    else: 
                        rowlist.append('1')
                elif terain==4:
                    if randint(0,int((y*x)/13))==5:
                        rowlist.append('0')
                    else: 
                        rowlist.append('1')
                elif terain==5:
                    if randint(0,int((y*x)/16))==5:
                        rowlist.append('0') 
                    else: 
                        rowlist.append('1')
            biglist.append(rowlist)
            rowlist=[]
        if enemnum>=1:
            biglist[int(y/2)][x-2]='3'
            enemy.X_cord=int(y/2)
            enemy.Y_cord=x-2
            if enemnum>=2:
                biglist[int(y/2)+2][x-2]='3'
                enemy2.X_cord=int(y/2)+2
                enemy2.Y_cord=x-2
                if enemnum>=3:
                    biglist[int(y/2)-2][x-2]='3'
                    enemy3.X_cord=int(y/2)-2
                    enemy3.Y_cord=x-2
                    if enemnum>=4:
                        biglist[int(y/2)-4][x-2]='3'
                        enemy4.X_cord=int(y/2)-4
                        enemy4.Y_cord=x-2
                        if enemnum>=5:
                            biglist[int(y/2)+4][x-2]='3'
                            enemy5.X_cord=int(y/2)+4
                            enemy5.Y_cord=x-2
        objpass.combatmap=biglist
        
    else: biglist=objpass.combatmap
    #
    while True:
        try:
            print('\n'*25)
            print("movement points "+str(objpass.movement_points))
            biglist[tempy][tempx]='1'
            biglist[cy][cx]='2'
            for i in biglist:
                #print(i)
                print("|")
                for j in i:     # 0 = unavalable , 1 = free , 2 = You , 3 = Enemy
                    if j =='1':
                        print('|__', end = '')
                    elif j =='2':
                        print (colored('|██', 'blue'),end = '')
                    elif j =='0':
                        print('|▓▓', end = '')
                    elif j =='3':
                        print(colored('|██', 'red'),end = '')

            biglist[tempy][tempx]='1'
            biglist[cy][cx]='2'
            tempx=cx
            tempy=cy
            objpass.X_cord=cx
            objpass.Y_cord=cy
            if caller == 1:
                inp=input(" choose ")
                if inp=="s":
                    if biglist[cy+1][cx]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy+=1
                    objpass.movement_points-=1
                elif inp=="w":
                    if biglist[cy-1][cx]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy-=1
                    objpass.movement_points-=1
                elif inp=="d":
                    if biglist[cy][cx+1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="a":
                    if biglist[cy][cx-1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cx-=1
                    objpass.movement_points-=1
                elif inp=="aw" or inp=="wa":
                    if biglist[cy-1][cx-1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy-=1
                    cx-=1
                    objpass.movement_points-=1
                elif inp=="dw" or inp=="wd":
                    if biglist[cy-1][cx+1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy-=1
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="ds" or inp=="sd":
                    if biglist[cy+1][cx+1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy+=1
                    cx+=1
                    objpass.movement_points-=1
                elif inp=="as" or inp=="sa":
                    if biglist[cy+1][cx-1]!='1' or objpass.movement_points<=0:
                        raise IndexError
                    cy+=1
                    cx-=1
                    objpass.movement_points-=1
                elif inp =="gg":
                    break
                else: print("Invalid Input")
            else:
                print("\nroflmao\n")
                if enemnum>=1:
                    biglist=enemy.decision(biglist)
                    if enemnum>=2:
                        biglist=enemy2.decision(biglist)
                        if enemnum>=3:
                            biglist=enemy3.decision(biglist)
                            if enemnum>=4:
                                biglist=enemy4.decision(biglist) 
                                if enemnum>=5:
                                    biglist=enemy5.decision(biglist)
                                       
                
                
                break
        except IndexError:
            cx=tempx
            cy=tempy
            

class Player():
    race="human"
    movement_points=5
    max_movement_points=5
    Y_cord=0
    X_cord=0
    combatmap=[]
    def cooldown(self):
        self.movement_points=self.max_movement_points
    
    
class Enemy():
    def __init__(self,name=None):
        self.name=name
    Y_cord=0
    X_cord=0
    movement_points=0
    def decision(self,karta):
        #oldx=self.X_cord
        #oldy=self.Y_cord
        enemy_cords=[]
        x_counter=-1 #tezi counteri markurat poziciqta kadeto ima player
        for i in karta:#vzema red
            x_counter+=1#resetva pokazatelq
            y_counter=-1
            for j in i:#vzema jikina
                y_counter+=1
                if karta[x_counter][y_counter]=='2':
                    enemy_cords.append(x_counter) #vkarva poziciqta na player v enemy_cord masiva
                    enemy_cords.append(y_counter)
        print("caller X&Y cord "+ str(self.Y_cord) +"/"+ str(self.X_cord)+"\n"+str(enemy_cords))
        if self.Y_cord != enemy_cords[1]:
            print("Y_cord e razlichen")
            if self.Y_cord > enemy_cords[1] and karta[self.X_cord][self.Y_cord+1] != karta[x_counter][y_counter]: #self.Y_cord > enemy_cords[1] and (self.Y_cord-1!=enemy_cords[1] or (self.X_cord-1!=enemy_cords[0] and self.X_cord+1!=enemy_cords[0])): ##karta[self.X_cord][self.Y_cord+1] != '2'  #or (self.X_cord-1!=enemy_cords[0] and self.X_cord+1!=enemy_cords[0]) 
                print("decrese")
                self.Y_cord-=1
                karta[self.X_cord][self.Y_cord+1]='1'
            if self.Y_cord < enemy_cords[1] and (self.Y_cord+1!=enemy_cords[1] and (self.X_cord-1!=enemy_cords[0] or self.X_cord+1!=enemy_cords[0])):
                self.Y_cord+=1
                print("increse")
                karta[self.X_cord][self.Y_cord-1]='1'
"""
cod za X
        if self.X_cord != enemy_cords[1]:
            print("Y_cord e razlichen")
            if self.X_cord > enemy_cords[1] and karta[self.X_cord][self.Y_cord+1] != karta[x_counter][y_counter]: #self.Y_cord > enemy_cords[1] and (self.Y_cord-1!=enemy_cords[1] or (self.X_cord-1!=enemy_cords[0] and self.X_cord+1!=enemy_cords[0])): ##karta[self.X_cord][self.Y_cord+1] != '2'  #or (self.X_cord-1!=enemy_cords[0] and self.X_cord+1!=enemy_cords[0]) 
                print("decrese")
                self.X_cord-=1
                karta[self.X_cord][self.Y_cord+1]='1'
            if self.Y_cord < enemy_cords[1] and (self.Y_cord+1!=enemy_cords[1] and (self.X_cord-1!=enemy_cords[0] or self.X_cord+1!=enemy_cords[0])):
                self.Y_cord+=1
                print("increse")
                karta[self.X_cord][self.Y_cord-1]='1'

            //karta[self.X_cord][self.Y_cord]='3
            
            """
            #return karta
            #return [self.Y_cord, self.X_cord ]
        #action = "move"
        #return action
 
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
    
def Combat(combNum,emem1type,enemNam1=None,emem2type=None,enemNam2=None,emem3type=None,enemNam3=None,emem4type=None,enemNam4=None,emem5type=None,enemNam5=None):
#
    enem1=Placeholder("ph")
    enem2=Placeholder("ph")
    enem3=Placeholder("ph")
    enem4=Placeholder("ph")
    enem5=Placeholder("ph")
    
    player=Player()
    
    if emem1type == "Thug":
        enem1=Thug(enemNam1)
    elif emem1type == "Bandit":
        enem1=Bandit(enemNam1)
    elif emem1type == "Pit_Fighter":
        enem1=Pit_Fighter(enemNam1)
    # 
    if enem1.name==None: 
        enem1.name=emem1type
#
    if combNum>1:
        if emem2type == "Thug":
            enem2=Thug()
        elif emem2type == "Bandit":
            enem2=Bandit()
        elif emem2type == "Pit_Fighter":
            enem2=Pit_Fighter() 
        enem2.name=emem2type 
        # 
        if enem2.name==None: 
            enem2.name=emem2type  
#
    if combNum>2:
        if emem3type == "Thug":
            enem3=Thug()
        elif emem3type == "Bandit":
            enem3=Bandit()
        elif emem3type == "Pit_Fighter":
            enem3=Pit_Fighter() 
        enem3.name=emem3type 
        # 
        if enem3.name==None: 
            enem3.name=emem3type
#
    if combNum>3:
        if emem4type == "Thug":
            enem4=Thug()
        elif emem4type == "Bandit":
            enem4=Bandit()
        elif emem4type == "Pit_Fighter":
            enem4=Pit_Fighter() 
        enem4.name=emem4type 
        # 
        if enem4.name==None: 
            enem4.name=emem4type
#
    if combNum>4:
        if emem5type == "Thug":
            enem5=Thug()
        elif emem5type == "Bandit":
            enem5=Bandit()
        elif emem5type == "Pit_Fighter":
            enem5=Pit_Fighter() 
        enem5.name=emem5type 
        #
        if enem5.name==None: 
            enem5.name=emem5type
    izbor_sur=0
    while True:
        if izbor_sur==1:
            break
        print("entering combat")
        while True:# player's turn
            print("entering player phase")
            #print(testprint)
            try:
                if enem1.curHealth>0:
                    print('Enemy: {} - Health: {}/{}'.format(enem1.name,enem1.curHealth,enem1.maxHealth))
                if combNum>1:
                    if enem2.curHealth>0:
                        print('Enemy: {} - Health: {}/{}'.format(enem2.name,enem2.curHealth,enem2.maxHealth))
                    if combNum>2:
                        if enem3.curHealth>0:
                             print('Enemy: {} - Health: {}/{}'.format(enem3.name,enem3.curHealth,enem3.maxHealth))
                        if combNum>3:
                            if enem4.curHealth>0:
                                print('4 Enemy: {} - Health: {}/{}'.format(enem4.name,enem4.curHealth,enem4.maxHealth))
                            if combNum>4:
                                if enem5.curHealth>0:
                                    print('5 Enemy: {} - Health: {}/{}'.format(enem5.name,enem5.curHealth,enem5.maxHealth))
                             
                                
                                
                izbor=int(input("\n1 - Move \n2 - Attack\n3 - Defend\n4 - use Ability\n5 - Use item\n6 - Do Nothing\n7 - Surrender\n"))
                if izbor == 1:
                    genmap(15,15,5,objpass=player,enemnum=combNum,caller=1,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
                elif izbor == 2:
                    if enem1.curHealth>0:
                        print('Enemy: {} - Health: {}/{}'.format(enem1.name,enem1.curHealth,enem1.maxHealth))
                    if combNum>1:
                        if enem2.curHealth>0:
                            print('Enemy: {} - Health: {}/{}'.format(enem2.name,enem2.curHealth,enem2.maxHealth))
                        if combNum>2:
                            if enem3.curHealth>0:
                                 print('Enemy: {} - Health: {}/{}'.format(enem3.name,enem3.curHealth,enem3.maxHealth))
                            if combNum>3:
                                if enem4.curHealth>0:
                                    print('Enemy: {} - Health: {}/{}'.format(enem4.name,enem4.curHealth,enem4.maxHealth))
                                if combNum>4:
                                    if enem5.curHealth>0:
                                        print('Enemy: {} - Health: {}/{}'.format(enem5.name,enem5.curHealth,enem5.maxHealth))
                        
                    
                    izbor_Atk=int(input("6. Back"))
                    if izbor_Atk==1 and enem1.curHealth>0:
                        enem1.curHealth-=20
                        break
                    elif izbor_Atk==1 and enem1.curHealth<0: print("target unavalable")
                    if izbor_Atk==2 and enem2.curHealth>0:
                        enem2.curHealth-=20
                        break
                    elif izbor_Atk==2 and enem2.curHealth<0: print("target unavalable")
                    if izbor_Atk==3 and enem3.curHealth>0:
                        enem3.curHealth-=20
                        break
                    elif izbor_Atk==3 and enem3.curHealth<0: print("target unavalable")
                    if izbor_Atk==4 and enem4.curHealth>0:
                        enem4.curHealth-=20
                        break
                    elif izbor_Atk==4 and enem4.curHealth<0: print("target unavalable")
                    if izbor_Atk==5 and enem5.curHealth>0:
                        enem5.curHealth-=20
                        break
                    elif izbor_Atk==5 and enem5.curHealth<0: print("target unavalable")
                    if izbor_Atk==6:
                        pass
                elif izbor == 3:
                    print("debug Defend")
                elif izbor == 4:
                    print("debug Ability")
                elif izbor == 5:
                    print("debug item")
                elif izbor == 6:
                    print("You do nothing")
                elif izbor == 7:
                    izbor_sur=int(input("Are you sure you want to surrender?\1 - yes\2 - no"))
                    if izbor_sur==1:
                        break
    
                print("\n\nenemy tirn\n\n")
                player.cooldown()
                if enem1!=None:
                    genmap(15,15,5,objpass=player,caller=2,enemnum=combNum,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5) 
                    
            except ValueError:
                print("Invalid Input")
        
#Combat(5,"Thug",emem2type="Bandit",emem3type="Pit_Fighter",emem4type="Pit_Fighter",emem5type="Pit_Fighter")             
Combat(2,"Thug",enemNam1="george",emem2type="Bandit")         