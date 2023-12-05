from emp import Emp
#Class Programmer is inherited from Emp
class SalesMgr(Emp):
    def __init__(self,id,name,bs,incent):
        #Call the constructor of base class
        #We refer to parent class using super keyword
        super().__init__(id,name,bs)        
        self.incentive = incent 
    def __str__(self):
        data = super().__str__()
        data += "\nIncentive ="+str(self.incentive)
        return data
    
    def calSal(self):
        return self.basic + self.incentive