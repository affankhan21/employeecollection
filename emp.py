from abc import ABC,abstractmethod
#ABC ->Abstract Base Class
class Emp(ABC):
    def __init__(self,id,nm,bs):
        self.eid = id
        self.ename = nm
        self.basic = bs

    def __str__(self):
        data = "Eid = "+str(self.eid)
        data += "\nEName ="+self.ename
        data += "\nBasic ="+str(self.basic)
        return data
    
    @abstractmethod
    def calSal(self):
        pass

