from datetime import datetime
import random

class Tasks:
    def __init__(self, name, priorty, typeofwork):
        self.id=random.randint(0,9999)
        self.name=name
        self.priorty=priorty
        self.typeofwork=typeofwork
        self.dateAdded=datetime.today().strftime('%Y-%m-%d')
    
    def __str__(self):
        return str(self.id) + " " + self.name +" "+ self.typeofwork +" "+ self.priorty +" "+ self.dateAdded
    
def addTask(task, typeofwork, priority):
    if task != '' and typeofwork != '' and priority != '':
        obj1 = Tasks(task, typeofwork, priority)
        with open("data.txt","a") as f:
            f.write("\n"+str(obj1))
            
def removeTask(identifier):
    if identifier != "":
        rows=[]
        with open("data.txt","r") as f:
            fileContent=f.readlines()
            for i in fileContent:
                if identifier in i:
                    continue
                rows.append(i)   
        with open("data.txt","w") as f:
            for i in rows:
                f.write(i)              
    
def listTasks():
    with open("data.txt","r") as f:
        fileContent=f.readlines()
        return fileContent
