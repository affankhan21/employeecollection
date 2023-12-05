from addNewEmp import getEmp
from emp import Emp
class Company:
    def __init__(self,cname,c_code):
        self.cname = cname
        self.c_code = c_code
        self.allEmp = [] #Empty list for emp
    def addEmp(self):
        e=getEmp()
        self.allEmp.append(e)
    def searchEmp(self,id):
        for e in self.allEmp:
            if id==e.eid:
                print("EMPLOYEE RECORD FOUND")
                print(e)
                break
        else:
            print("EMPLOYEE RECORD  NOT FOUND")            
    def editEmp(self,id):
        '''for j in self.allEmp:
             if id==j.eid:
                print("EMPLOYEE RECORD FOUND")
                print(j)
                print("edit started")
                j=getEmp()
                self.allEmp.append(j)
                print("edit completed!")
                

        else:
            print("EMPLOYEE RECORD  NOT FOUND") '''  


    def deleteEmployee(self,id):
        for i in self.allEmp:
            if id==i.eid:
                print("EMPLOYEE RECORD FOUND")
                self.allEmp.remove(i)
                print("deleted")
                break
        else:
            print("EMPLOYEE RECORD  NOT FOUND") 
    def showAllEmp(self):
        for e in self.allEmp:
            print(e)
            print("-------------------")