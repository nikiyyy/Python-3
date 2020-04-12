class item():

    def __init__ (self,ID,name,value,weight):
        self.ID=ID
        self.name=name
        self.value=value
        self.weight=weight
        
    def __str__(self):
        return self.name
        
    def destroy(self):
        pass
    
class M_weapons(item):
    #false - blunt    true - pearce 3 slash
    def __init__ (self,ID,name,damage_type,value,weight,damage,hands,atributes=None):
        super().__init__(ID,name,value,weight)
        self.damage_type=damage_type
        self.damage=damage
        self.hands=hands
        self.atributes=atributes
        
class R_weapons(item):  
    ismagic=False #F normal, True staff
    damage_type=False #B - blunt  P - pearce  S - swash , PS - pearce/swash
    damage=2
    ammo=5
    slot=3
    hands=1
    def __init__ (self,ID,name,damage_type,value,weight,damage,hands):
        self.ID=ID
        self.name=name
        self.value=value
        self.weight=weight
        self.damage_type=damage_type
        self.damage=damage  
        self.hands=hands
        
    def aim_channel(self):
        if self.ismagic==False:
            pass#increase acc
        else:pass#increase damage
    
class C_armour(item):
                    #ligh - L medium - M Heavy - H
    def __init__ (self,ID,name,value,weight,armour_type,defence,atributes=None):
        super().__init__(ID,name,value,weight)
        self.defence=defence
        self.armour_type=armour_type
        self.atributes=atributes
        
class C_shield(item):
    hands=1
    def __init__ (self,ID,name,value,weight,defence,size):
        super().__init__(ID,name,value,weight)
        self.defence=defence
        self.size=size

class C_consumable(item):
    ComType='F' #F - food D - Drink S- stamina H Health
    def __init__ (self,ID,name,value,weight,ComType):
        self.ID=ID
        self.name=name
        self.value=value
        self.weight=weight
        self.ComType=ComType
    
    
                    #ID,name,damage_type,value,weight,damage,hands):
weapon1=M_weapons(101,"Club",'B',3,1,4,1)
weapon2=M_weapons(102,"Dagger",'P',10,1,4,1)
weapon3=M_weapons(103,"Handaxe",'S',15,2,6,1)
weapon4=M_weapons(104,"Short Sword",'P',20,2,6,1)
weapon5=M_weapons(105,"Mace",'B',25,3,6,1)
weapon6=M_weapons(106,"Bastard Sword",'P',25,3,10,1)
weapon7=M_weapons(107,"Spear",'P',25,3,8,2)
weapon8=M_weapons(108,"Battle Axe",'S',35,5,12,2)
weapon9=M_weapons(109,"Great Sword",'S',35,5,12,2)
weapon10=M_weapons(110,"War Hammer",'B',35,5,12,2)

weapon69=R_weapons(169,"God's fist",'B',35,5,500,1)

Mweapons=(weapon1,weapon2,weapon3,weapon4,weapon5,weapon6,weapon7,weapon8,weapon9,weapon10,weapon69)

Rweapons=()

    #ID,name,value,weight,type,defence 
armour1=C_armour(201,"Common Clothes",10,1,'L',1)
armour2=C_armour(202,"Noble Clothes",100,1,'L',1)
armour3=C_armour(203,"Hide",10,5,'L',3)
armour4=C_armour(204,"Padded",25,3,'L',3)
armour5=C_armour(205,"Leather",35,4,'L',5)
armour6=C_armour(206,"Studded Leather",45,5,'L',7)
armour7=C_armour(207,"Chain Mail",60,8,'M',9)
armour8=C_armour(208,"Scale Mail",75,9,'M',11)
armour9=C_armour(209,"Splint Mail",100,13,'H',15)
armour10=C_armour(210,"Plate",130,20,'H',20)

Armour=(armour1,armour2,armour3,armour4,armour5,armour6,armour7,armour8,armour9,armour10)
#(self,ID,name,value,weight,defence,size):
shield1=C_shield(301,"Buckler",20,2,3,'S')
shield2=C_shield(302,"Round Shield",15,5,6,'M')
shield3=C_shield(303,"Tower Shield",30,10,10,'L')
Shield=(shield1,shield2,shield3)
#hitchanse se generira dinamichno na momenta spored nivoto na igracha ,protivika, urujieto