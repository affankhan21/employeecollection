from admin import Admin
from salesmgr import SalesMgr
from programmer import Programmer

def getEmp():
    choice=0
    print("\nWhich type of employee you want :")
    print("\t\t1.Admin ")
    print("\t\t2.Sales Manager  ")
    print("\t\t3.Programmer ")
    print("\t\t4.Exit ")
    choice=int(input("ENTER YOUR CHOICE :"))   
    if (choice==1):
        eid=int(input("ENTER THE ADMIN EMPLOYEE EID  :"))
        ename=input("ENTER EMPLOYEE NAME             :")
        salary=float(input("ENTER EMPLOYEE SALARY    :" ))
        comm=float(input("ENTER THE COMIISION        :"))
        al=Admin(eid,ename,salary,comm)
        return al
    elif(choice==2):
        eid=int(input("ENTER THE SALES MANAGER EMPLOYEE EID       :"))
        ename=input("ENTER EMPLOYEE NAME                          :")
        salary=float(input("ENTER EMPLOYEE SALARY                 :"))
        incent=float(input("ENTER THE INCENTIVES                  :"))
        s1=SalesMgr(eid,ename,salary,incent)
        return s1
    elif(choice==3):
        eid=int(input("ENTER THE PROGRAMMER EMPLOYEE EID  :"))
        ename=input("ENTER EMPLOYEE NAME             :")
        salary=float(input("ENTER EMPLOYEE SALARY    :" ))
        extrahrs=int(input("ENTER EMPLOYEE  EXTRA HOURS :"))
        costperhr=int(input("ENTER THE COST PER HOURS  :"))
        p1=Programmer(eid,ename,salary,extrahrs,costperhr)
        return p1
    else: 
        return    

