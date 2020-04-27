class Spacialisation():
    spelldict={}#key - name value - energie soust
    def abilitylist():
        pass
    #activates spells


class Rogue(Spacialisation):
    abilitylist={}
    def menu(self):
        for i in self.abilitylist:
            print(i)

class Warrior(Spacialisation):
    abilitylist={"test1":15,"test2":20}
    def menu(self,user):
        for i in self.abilitylist:
            print(i)

class Ranger(Spacialisation):
    abilitylist={"":"","":""}
    def menu(self,user):
        for i in self.abilitylist:
            print(i)

class Mage(Spacialisation):
    abilitylist={}
    def menu(self):
        input("lol")

test=Warrior()