from emp import Emp
#Class Programmer is inherited from Emp
class Programmer (Emp):
    def __init__(self,id,name,bs,eh,cph):
        #Call the constructor of base class
        #We refer to parent class using super keyword
        super().__init__(id,name,bs)        
        self.extraHrs = eh
        self.costPerHrs = cph
    def __str__(self):
        data = super().__str__()
        data += "\nExtra Hrs ="+str(self.extraHrs)
        data += "\nCost Per Hrs ="+str(self.costPerHrs)
        return data
    
    def calSal(self):
        return self.basic + self.extraHrs * self.costPerHrs