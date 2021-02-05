#The application was writen in Python 3.7.3 by Nikolai Ivanov

#the imports from datetime are used to create datetime objects from the dates in the file
from datetime import datetime as dt
from datetime import timedelta as td 

class Employee:  
    def __init__(self, workerID, logList, IDlist):
        self.workerID=workerID
        self.workedOnprojects=logList
        self.workedWith={}
        
        for i in IDlist:# creates a dictionary with the IDs of every employee
            if i != workerID:
                self.workedWith.update({i : td(seconds=1)})
                
    def mostWorkedWith(self):# prints the most worked with employee for this instance of class Employee
        if self.workedWith.get(max(self.workedWith, key=self.workedWith.get)).days == 0:
            print("{} hasn't worked with anyone".format(self.workerID))
        else: 
            print("Employee {}, has {} days of work with employee {}".format(self.workerID, self.workedWith.get(max(self.workedWith, key=self.workedWith.get)).days, max(self.workedWith, key=self.workedWith.get)))
        
    def get_colleague(self):# used for finding the maximum days 2 employees have
        return  max(self.workedWith, key=self.workedWith.get)
    
    def get_days(self):# used for finding the maximum days 2 employees have
        return  self.workedWith.get(max(self.workedWith, key=self.workedWith.get)).days
    
    def calculate(self, colleagues):#used to calculate the number of days worked with every employee
        for i in colleagues:
            if i.workerID == self.workerID:# or i.workerID == None:" 
                continue
            for j in self.workedOnprojects:
                for k in i.workedOnprojects:# iterates through the workLogs
                    if j.projID == k.projID:#and checks if both employees have worked on the same project
                        #checks if the both employees have worked on the same project at the same time
                        if (j.dateFrom < k.dateFrom and j.dateTo < k.dateTo) and (j.dateFrom < k.dateTo and j.dateTo < k.dateFrom) or (j.dateFrom > k.dateFrom and j.dateTo > k.dateTo) and (j.dateFrom > k.dateTo and j.dateTo > k.dateFrom):
                            continue
                        #sets the lower boundary of time worked
                        start=None
                        if j.dateFrom > k.dateFrom:
                            start=j.dateFrom
                        else: start=k.dateFrom
                        #sets the lower boundary of time worked
                        end=None
                        if j.dateTo < k.dateTo:
                            end=j.dateTo
                        else: end=k.dateTo
                        
                        #updates the dictionary that holds worked days for each employeed
                        self.workedWith.update({k.empID : self.workedWith.get(k.empID)+(end-start) })


class WorkLog: #used to structure and easily manipolate the data from the file
    def __init__(self, string):
        self.empID, self.projID, self.dateFrom, self.dateTo = i.split(', ')#parsing the raw string
        
        #creating the datetime objects
        self.dateFrom=self.dateFrom.split('-')
        self.dateFrom=dt(int(self.dateFrom[0]),int(self.dateFrom[1]),int(self.dateFrom[2]))
        
        self.dateTo=self.dateTo.split('-')
        if self.dateTo == ['NULL']:
            self.dateTo=dt.now()# if the there is a NULL value, we use the current date to indicate that the project is ongoing
        else:
            self.dateTo=dt(int(self.dateTo[0]),int(self.dateTo[1]),int(self.dateTo[2]))
            
            
            
while True:
    try:# extracting the raw data from the file
        fileName=input("Please enter the file's full name to contune or /// to exit the application\n")
        with open(fileName) as f:
            fileContent=f.readlines()
            break
    except:
        if fileName == "///" :
            break
        print("Something went wrong! Have you entered the file extension?")
        

employeeIDList=[]#holds every unique empoyee ID
workLogList=[]#holds WorkLog objects
employeeList=[]#holds Employee objects

for i in fileContent:#parsing the data from the file and organising it with a class
    i=i.replace(' \n', '')
    employeeIDList.append(i.split(",", 1)[0])
    log=WorkLog(i)#crateing a new WorkLog object with the parsed data
    workLogList.append(log)# and appending it to the WorkLog List
    
employeeIDList=list(dict.fromkeys(employeeIDList))# removing duplicates
for i in employeeIDList:
    relevantLogs=[]#this list holds the relevant worklogs for the current employee object
    for j in workLogList:
        if j.empID == i:
            relevantLogs.append(j)
    emp=Employee(i, relevantLogs, employeeIDList)#crateing a new Employee object
    employeeList.append(emp)
    
for i in employeeList:#calculates the number of days worked with every other employee
    i.calculate(employeeList)
    
try:
    choise=0
    while choise != '3' and fileName != "///":# a small menu for the user
        choise=input("Please enter the corresponding number : \n1. Output the pair of employees with most days worked. \n2. Output every employee's partner. \n3. Exit.")
        if choise == '1':#setting of the default values
            a=employeeList[0].workerID
            b=employeeList[0].get_colleague()
            c=employeeList[0].get_days()
            for i in employeeList:
                if i.get_days()>c:
                     a=i.workerID
                     b=i.get_colleague()
                     c=i.get_days()
            print("Employees with the most work days together are {} and {}, with {} days".format(a,b,c))
        elif choise == '2':#outputs the buddy of every employee
            for i in employeeList:
                i.mostWorkedWith()
        elif choise == '3':#exits the application
            print("Have a nice day")
        else: print("invalid input")
except:
    print("Something went wrong!")
    
