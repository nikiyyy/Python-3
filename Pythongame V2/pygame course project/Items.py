class item():
    value=5
    weight=1.5
    
    def __init__ (self):
        pass

class M_weapons(item):
    damage_type=1 #1 - blunt    2 - pearce
    damage=2
    def __init__ (self,damage_type,value,weight,damage):
        self.value=value
        self.weight=weight
        self.damage_type=damage_type
        self.damage=damage
        
class R_weapons(item):  
    ismagic=False
    damage_type=1 #1 - blunt    2 - pearce 3
    damage=2
    ammo=5
    def __init__ (self,damage_type,value,weight,damage):
        self.value=value
        self.weight=weight
        self.damage_type=damage_type
        self.damage=damage  
    
    def aim_channel(self):
        if self.ismagic==False:
            pass
        else:pass
    
class armour(item):
    
    def __init__ (self):
        pass
    
class consumable(item):
    
    def __init__ (self):
        pass