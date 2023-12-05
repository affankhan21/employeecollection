from emp import Emp
#Class Programmer is inherited from Emp
class Admin(Emp):
    def __init__(self,id,name,bs,comm):
        #Call the constructor of base class
        #We refer to parent class using super keyword
        super().__init__(id,name,bs)        
        self.commission = comm
    def __str__(self):
        data = super().__str__()
        data += "\nCommission ="+str(self.commission)
        return data

    def calSal(self):
        return self.basic + self.commission
