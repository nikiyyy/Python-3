from random import randint #izpolzva se za generorane na proizvolni chesla
#from time import sleep

import GenirateMap as GM
import Enemies as EN
#import Player as PL        

#kogato ima bitka se izvikva funciqta Combat(), tq e pulna sus argumenti koito imat defaltni stoinoti kogato ne se izpolzvat
def Combat(player,combNum,emem1type,enemNam1=None,emem2type=None,enemNam2=None,emem3type=None,enemNam3=None,emem4type=None,enemNam4=None,emem5type=None,enemNam5=None):
#combNum e broq na opunentite za tzi butka
#emem1type priema za argument tipa protivnik
#enemNam1 se izpolzva samo ako protivnika ima specialno ime
    
    #paceholder obekti za protivnicite 
    enem1=EN.Placeholder("ph")
    enem2=EN.Placeholder("ph")
    enem3=EN.Placeholder("ph")
    enem4=EN.Placeholder("ph")
    enem5=EN.Placeholder("ph")
    
    #player=PL.Player()
    
    #tuk se izbira tipa i imeto na opunenta
    if emem1type == "Thug":
        enem1=EN.Thug(enemNam1)
    elif emem1type == "Bandit":
        enem1=EN.Bandit(enemNam1)
    elif emem1type == "Pit_Fighter":
        enem1=EN.Pit_Fighter(enemNam1)
    # 
    if enem1.name==None: 
        enem1.name=emem1type


    if combNum>1:
        if emem2type == "Thug":
            enem2=EN.Thug()
        elif emem2type == "Bandit":
            enem2=EN.Bandit()
        elif emem2type == "Pit_Fighter":
            enem2=EN.Pit_Fighter() 
        enem2.name=emem2type 
        # 
        if enem2.name==None: 
            enem2.name=emem2type  
#
    if combNum>2:
        if emem3type == "Thug":
            enem3=EN.Thug()
        elif emem3type == "Bandit":
            enem3=EN.Bandit()
        elif emem3type == "Pit_Fighter":
            enem3=EN.Pit_Fighter() 
        enem3.name=emem3type 
        # 
        if enem3.name==None: 
            enem3.name=emem3type
#
    if combNum>3:
        if emem4type == "Thug":
            enem4=EN.Thug()
        elif emem4type == "Bandit":
            enem4=EN.Bandit()
        elif emem4type == "Pit_Fighter":
            enem4=EN.Pit_Fighter() 
        enem4.name=emem4type 
        # 
        if enem4.name==None: 
            enem4.name=emem4type
#
    if combNum>4:
        if emem5type == "Thug":
            enem5=EN.Thug()
        elif emem5type == "Bandit":
            enem5=EN.Bandit()
        elif emem5type == "Pit_Fighter":
            enem5=EN.Pit_Fighter() 
        enem5.name=emem5type 
        #
        if enem5.name==None: 
            enem5.name=emem5type
            
    izbor_sur=0#exit 
    while enem1.curHealth>0 or enem2.curHealth>0 or enem3.curHealth>0 or enem4.curHealth>0 or enem5.curHealth>0:
        if izbor_sur==1:
            break
        print("entering combat")
        GM.genmap(15,15,5,objpass=player,enemnum=combNum,caller=0,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
        while enem1.curHealth>0 or enem2.curHealth>0 or enem3.curHealth>0 or enem4.curHealth>0 or enem5.curHealth>0:# player's turn
            print("entering player phase")
            if player.curHealth<=0:
                izbor_sur=1
                break
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
                print("your health : "+str(player.curHealth)+"/"+str(player.maxHealth))
                    
                izbor=int(input("\n1 - Move \n2 - Attack\n3 - Defend\n4 - use Ability\n5 - Use item\n6 - Do Nothing\n7 - Surrender\n"))
                if izbor == 1:#move - generira karta v nachaloto na bitkata 
                    GM.genmap(15,15,5,objpass=player,enemnum=combNum,caller=1,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5)  
                #(X,Y,Grubost na terena (5MAX),tekuchtata karta se zapamenqva v classa na igracha,broi vragove, kogato caller e 1 genmap e povikana ot igracha kogato e 0 e povikana ot protivnik, podavam enemy obektite)
                elif izbor == 2: #igracha si izbira koi da atakuva
                    if enem1.curHealth>0 and player.am_i_touching(enem1,player.combatmap):
                        print('1- Enemy: {} - Health: {}/{}'.format(enem1.name,enem1.curHealth,enem1.maxHealth))
                    if combNum>1:
                        if enem2.curHealth>0 and player.am_i_touching(enem2,player.combatmap):
                            print('2- Enemy: {} - Health: {}/{}'.format(enem2.name,enem2.curHealth,enem2.maxHealth))
                        if combNum>2:
                            if enem3.curHealth>0 and player.am_i_touching(enem3,player.combatmap):
                                 print('3- Enemy: {} - Health: {}/{}'.format(enem3.name,enem3.curHealth,enem3.maxHealth))
                            if combNum>3:
                                if enem4.curHealth>0 and player.am_i_touching(enem4,player.combatmap):
                                    print('4- Enemy: {} - Health: {}/{}'.format(enem4.name,enem4.curHealth,enem4.maxHealth))
                                if combNum>4:
                                    if enem5.curHealth>0 and player.am_i_touching(enem5,player.combatmap):
                                        print('5- Enemy: {} - Health: {}/{}'.format(enem5.name,enem5.curHealth,enem5.maxHealth))
                        
                    izbor_Atk=int(input("6. Back"))
                    
                    if izbor_Atk==1 and enem1.curHealth>0 and player.am_i_touching(enem1,player.combatmap):
                        enem1.curHealth-=20
                        if enem1.curHealth<=0:
                            player.combatmap=enem1.died(player.combatmap)
                        #break
                    elif izbor_Atk==1 and enem1.curHealth<=0: print("target unavalable")
                    if izbor_Atk==2 and enem2.curHealth>0 and player.am_i_touching(enem2,player.combatmap):
                        enem2.curHealth-=20
                        if enem2.curHealth<=0:
                            player.combatmap=enem2.died(player.combatmap)
                        #break
                    elif izbor_Atk==2 and enem2.curHealth<=0: print("target unavalable")
                    if izbor_Atk==3 and enem3.curHealth>0 and player.am_i_touching(enem3,player.combatmap):
                        enem3.curHealth-=20
                        if enem3.curHealth<=0:
                            player.combatmap=enem3.died(player.combatmap)
                        #break
                    elif izbor_Atk==3 and enem3.curHealth<=0: print("target unavalable")
                    if izbor_Atk==4 and enem4.curHealth>0 and player.am_i_touching(enem4,player.combatmap):
                        enem4.curHealth-=20
                        if enem4.curHealth<=0:
                            player.combatmap=enem4.died(player.combatmap)
                        #break
                    elif izbor_Atk==4 and enem4.curHealth<=0: print("target unavalable")
                    if izbor_Atk==5 and enem5.curHealth>0 and player.am_i_touching(enem5,player.combatmap):
                        enem5.curHealth-=20
                        if enem5.curHealth<=0:
                            player.combatmap=enem5.died(player.combatmap)
                        #break
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
                    GM.genmap(15,15,5,objpass=player,caller=2,enemnum=combNum,enemy=enem1,enemy2=enem2,enemy3=enem3,enemy4=enem4,enemy5=enem5) 
                    #protivnicite pravqt hod
            except ValueError:
                print("Invalid Input")
        
 