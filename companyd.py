from addNewEmp import getEmp
from emp import Emp
class Companyd:
    def __init__(self,cname,c_code):
        self.cname = cname
        self.c_code = c_code
        self.allEmp = {}#Empty dict for emp
    def addEmp(self):
        e=getEmp()
        self.allEmp[e1.eid]=e1
    def searchEmp(self,id):
        result=self.allEmp.get(id,"not found")
        print(result)            
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