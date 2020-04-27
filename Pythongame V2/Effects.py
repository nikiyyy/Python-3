class Effect():
    
    def __init__(self,ID,EFTpye,intencity,duration,name):
        self.ID=ID
        self.EFTpye=EFTpye
        self.intencity=intencity
        self.duration=duration
        self.name=name
        
    def apply(self,user=None):
        if self.EFTpye == 'P':
            user.curHealth-=self.intencity
        elif self.EFTpye == 'H':
            user.curHealth-=self.intencity
    def __str__(self):
        return str(self.ID)
    
poison1=Effect(101,'P',10,3,"corona 1")
poison2=Effect(102,'P',20,4,"corona 2")
poison3=Effect(103,'P',30,5,"corona 3")

regenerate=Effect(201,'H',5,5,"regeneration")
tupple_effects=(poison1,poison2,poison3)