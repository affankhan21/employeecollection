from company import Company

c1 = Company("Aug_18",1201)
choice = 0
while choice != 5:
    print("\t1.Add Emp")
    print("\t2.Display all emps")
    print("\t3.Search Emp")
    print("\t4.Delete Emp")
    print("\t5.Edit Emp")
    print("\t6.Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        c1.addEmp()
    elif choice == 2:
        c1.showAllEmp()
    elif choice == 3:
        id = int(input("Enter the id you want to search : "))
        c1.searchEmp(id)
    elif choice == 4:
        id = int(input("Enter the id you want to delete : "))
        c1.deleteEmployee(id)
    elif choice==5:
        id = int(input("Enter the id you want to edit : "))
        c1.editEmp(id)

    else:
        print("bye ")       