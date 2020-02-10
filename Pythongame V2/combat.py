from random import randint #izpolzva se za generorane na proizvolni chesla
from termcolor import colored#izpolzva se za ocvetqvane na kvadratite
from time import sleep

def genmap(x,y,terain,objpass=None ,caller=None,enemnum=1,enemy=None,enemy2=None,enemy3=None,enemy4=None,enemy5=None):   #caller = 1 - player your || caller = 2 - enemy tirn
    biglist=[]
    cx=objpass.X_cord# cx stava X kodinata na player obekta
    cy=objpass.Y_cord# cy stava Y kodinata na player obekta
    tempx=cx# vremenni promenlivi
    tempy=cy#
    if objpass.combatmap==[]:#tuk vliza samo vednuj v nachaloto na bitka, ako veche naqma generirana karta
        cx=2# dava startova poziciq na igracha
        cy=int(y/2)
        tempx=cx
        tempy=cy
        rowlist=[]
        for i in range(0,x): #generira teren - 0-obsicle 1-free 2-player 3-enemy1
            for j in range(0,y): #Pulni biglist red po red spored rowlist
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
        if enemnum>=1: #nasilstveno(override stara poziciq) postavq protivnici
            biglist[int(y/2)][x-2]='3'
            enemy.Y_cord=int(y/2)
            enemy.X_cord=x-2
            if enemnum>=2:
                biglist[int(y/2)+2][x-2]='3'
                enemy2.Y_cord=int(y/2)+2
                enemy2.X_cord=x-2
                if enemnum>=3:
                    biglist[int(y/2)-2][x-2]='3'
                    enemy3.Y_cord=int(y/2)-2
                    enemy3.X_cord=x-2
                    if enemnum>=4:
                        biglist[int(y/2)-4][x-2]='3'
                        enemy4.Y_cord=int(y/2)-4
                        enemy4.X_cord=x-2
                        if enemnum>=5:
                            biglist[int(y/2)+4][x-2]='3'
                            enemy5.Y_cord=int(y/2)+4
                            enemy5.X_cord=x-2
        objpass.combatmap=biglist#veche gotovata karta se zapazva v instance na player obekta 
        
    else: biglist=objpass.combatmap
    
    while True:
        try:#izkarvane na jartata na konzola
            print('\n'*25)
            print("movement points "+str(objpass.movement_points))
            biglist[tempy][tempx]='1'#iztriva starata poziciq
            biglist[cy][cx]='2'
            for i in biglist:#iterira prez vseki eliment i go izpisva na konzola
                print("|")
                for j in i:     # 0 = unavalable , 1 = free , 2 = You , 3 = Enemy
                    if j =='1':
                        print('|__', end = '')
                    elif j =='2':
                        print ("|"+colored('██', 'blue'),end = '')
                    elif j =='0':
                        print('|▓▓', end = '')
                    elif j =='3':
                        print("|"+colored('██', 'red'),end = '')

            biglist[tempy][tempx]='1'
            biglist[cy][cx]='2'
            tempx=cx
            tempy=cy
            objpass.X_cord=cx
            objpass.Y_cord=cy
            if caller == 1:#ako hoda na igracha, toi shte ima vuzmojnost da se dviji
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
                elif inp =="gg":#"gg" e za prekluchvane na dvijenieto
                    break
                else: print("Invalid Input")
            else:
                print("\nEnemy thinkng:\n")#hoda na privnika
                if enemnum>=1:
                    biglist=enemy.decision(biglist,objpass.X_cord,objpass.Y_cord)#vzema kartata updejtva q v svoq chlen funkciq i a vrushta obratno
                    if enemnum>=2:
                        biglist=enemy2.decision(biglist,objpass.X_cord,objpass.Y_cord)
                        if enemnum>=3:
                            biglist=enemy3.decision(biglist,objpass.X_cord,objpass.Y_cord)
                            if enemnum>=4:
                                biglist=enemy4.decision(biglist,objpass.X_cord,objpass.Y_cord) 
                                if enemnum>=5:
                                    biglist=enemy5.decision(biglist,objpass.X_cord,objpass.Y_cord)
                                       
                objpass.combatmap=biglist
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
    
    
class Enemy(): #enemy e baseclass koto se nasledqva ot vsichko protivnici
    def __init__(self,name=None):
        self.name=name
    Y_cord=0
    X_cord=0
    movement_points=2
    
    def decision(self,karta,PX,PY): 
        print("\nDebug\n"+"player X "+str(PX)+" player Y "+str(PY)+"\n ENEMY X "+str(self.X_cord)+"ENEMY Y "+str(self.Y_cord)+"Debug")

        while self.movement_points>0:
            #diagonalno dvijenie
            if self.Y_cord > PY and self.X_cord > PX:
                if karta[self.Y_cord-1][self.X_cord-1] == "3" or karta[self.Y_cord-1][self.X_cord-1] == "0":
                    print("\nobsticleA")
                    if karta[self.Y_cord-1][self.X_cord] == "1":
                        print("\nobsticleA1")
                        karta[self.Y_cord][self.X_cord]="1"
                        self.Y_cord-=1
                        self.movement_points-=1
                        
                    elif karta[self.Y_cord][self.X_cord-1] == "1":
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
                    break
                    
                
                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord-=1
                self.X_cord-=1
                self.movement_points-=1

            elif self.Y_cord < PY and self.X_cord < PX:
                if  karta[self.Y_cord+1][self.X_cord+1] == "3" or karta[self.Y_cord+1][self.X_cord+1] == "0":
                    print("\nobsticleB")
                    #AHHHHHHHHHHHHH
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
                    #AHHHHHHHHHHHHHHH
                elif karta[self.Y_cord+1][self.X_cord+1] == "2":
                    print("\nearplayerB")
                    break
                
                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord+=1
                self.X_cord+=1
                self.movement_points-=1                

            elif self.Y_cord > PY and self.X_cord < PX:
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
                    break

                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord-=1
                self.X_cord+=1
                self.movement_points-=1                

            elif self.Y_cord < PY and self.X_cord > PX:
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
                    break
                
                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord+=1
                self.X_cord-=1
                self.movement_points-=1
             #single axis movement
            elif self.Y_cord > PY :
                if karta[self.Y_cord-1][self.X_cord] == "3" or karta[self.Y_cord-1][self.X_cord] == "0":
                    print("\nobsticleE")
                    if karta[self.Y_cord-1][self.X_cord+1] == "1":
                        print("\nobsticleE1")
                        karta[self.Y_cord][self.X_cord]="1"
                        self.Y_cord-=1
                        self.X_cord+=1
                        self.movement_points-=1
                    elif karta[self.Y_cord-1][self.X_cord-1] == "1":
                        print("\nobsticleE2")
                        karta[self.Y_cord][self.X_cord]="1"
                        self.Y_cord-=1
                        self.X_cord-=1
                        self.movement_points-=1
                    else:
                        print("\nobsticleE3")
                        break
                    karta[self.Y_cord][self.X_cord]="3"
                    continue
                elif karta[self.Y_cord-1][self.X_cord] == "2":
                     print("\nearplayerE")
                     break

                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord-=1
                self.movement_points-=1
            
            
            elif self.Y_cord < PY :
                if karta[self.Y_cord+1][self.X_cord] == "3" or karta[self.Y_cord+1][self.X_cord] == "0":
                    print("\nobsticleF")
                    if karta[self.Y_cord+1][self.X_cord+1] == "1":
                        print("\nobsticleF1")
                        karta[self.Y_cord][self.X_cord]="1"
                        self.Y_cord+=1
                        self.X_cord+=1
                        self.movement_points-=1
                    elif karta[self.Y_cord+1][self.X_cord-1] == "1":
                        print("\nobsticleF2")
                        karta[self.Y_cord][self.X_cord]="1"
                        self.Y_cord+=1
                        self.X_cord-=1
                        self.movement_points-=1
                    else:
                        print("\nobsticleF3")
                        break
                    karta[self.Y_cord][self.X_cord]="3"
                    continue
                
                elif karta[self.Y_cord+1][self.X_cord] == "2":
                    print("nearplayerF")
                    break
                
                karta[self.Y_cord][self.X_cord]="1"
                self.Y_cord+=1
                self.movement_points-=1
                
            elif self.X_cord > PX :
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
                    break
                    
                karta[self.Y_cord][self.X_cord]="1"
                self.X_cord-=1
                self.movement_points-=1  
                
            elif self.X_cord < PX :
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
                    break
                
                karta[self.Y_cord][self.X_cord]="1"
                self.X_cord+=1
                self.movement_points-=1
            else:
                break

            karta[self.Y_cord][self.X_cord]="3"
        self.movement_points=2
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
    
#kogato ima bitka se izvikva funciqta Combat(), tq e pulna sus argumenti koito imat defaltni stoinoti kogato ne se izpolzvat
def Combat(combNum,emem1type,enemNam1=None,emem2type=None,enemNam2=None,emem3type=None,enemNam3=None,emem4type=None,enemNam4=None,emem5type=None,enemNam5=None):
#combNum e broq na opunentite za tzi butka
#emem1type priema za argument tipa protivnik
#enemNam1 se izpolzva samo ako protivnika ima specialno ime
    
    #paceholder obekti za protivnicite 
    enem1=Placeholder("ph")
    enem2=Placeholder("ph")
    enem3=Placeholder("ph")
    enem4=Placeholder("ph")
    enem5=Placeholder("ph")
    
    player=Player()
    
    #tuk se izbira tipa i imeto na opunenta
    if emem1type == "Thug":
        enem1=Thug(enemNam1)
    elif emem1type == "Bandit":
        enem1=Bandit(enemNam1)
    elif emem1type == "Pit_Fighter":
        enem1=Pit_Fighter(enemNam1)
    # 
    if enem1.name==None: 
        enem1.name=emem1type


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
            
    izbor_sur=0#exit 
    while True:
        if izbor_sur==1:
            break
        print("entering combat")
        while True:# player's turn
            print("entering player phase")
            try:    #izkarva atrebutite na protivnicite
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
                             
                                
                #menu selector                
                izbor=int(input("\n1 - Move \n2 - Attack\n3 - Defend\n4 - use Ability\n5 - Use item\n6 - Do Nothing\n7 - Surrender\n"))
                if izbor == 1:#move - generira karta v nachaloto na bitkata 
                    genmap(15,15,5,objpass=player,enemnum=combNum,caller=1,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
                #(X,Y,Grubost na terena (5MAX),tekuchtata karta se zapamenqva v classa na igracha,broi vragove, kogato caller e 1 genmap e povikana ot igracha kogato e 0 e povikana ot protivnik, podavam enemy obektite)
                elif izbor == 2: #igracha si izbira koi da atakuva
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
                    elif izbor_Atk==1 and enem1.curHealth<=0: print("target unavalable")
                    if izbor_Atk==2 and enem2.curHealth>0:
                        enem2.curHealth-=20
                        break
                    elif izbor_Atk==2 and enem2.curHealth<=0: print("target unavalable")
                    if izbor_Atk==3 and enem3.curHealth>0:
                        enem3.curHealth-=20
                        break
                    elif izbor_Atk==3 and enem3.curHealth<=0: print("target unavalable")
                    if izbor_Atk==4 and enem4.curHealth>0:
                        enem4.curHealth-=20
                        break
                    elif izbor_Atk==4 and enem4.curHealth<=0: print("target unavalable")
                    if izbor_Atk==5 and enem5.curHealth>0:
                        enem5.curHealth-=20
                        break
                    elif izbor_Atk==5 and enem5.curHealth<=0: print("target unavalable")
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
                player.cooldown()#refreshva cooldowns na player
                if enem1!=None:
                    genmap(15,15,5,objpass=player,caller=2,enemnum=combNum,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5) 
                    #protivnicite pravqt hod
            except ValueError:
                print("Invalid Input")
        
#Combat(5,"Thug",emem2type="Bandit",emem3type="Pit_Fighter",emem4type="Pit_Fighter",emem5type="Pit_Fighter")             
Combat(2,"Thug",enemNam1="george",emem2type="Bandit")     
#Combat(1,"Thug",enemNam1="bob")     