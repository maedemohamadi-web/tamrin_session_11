from home_module import *

home_list=[]

while True:
    option=show_menu()
    print("_"*30)

    match option:
        case 1:
            print("Enter home information")
            home=get_home_data()
            home_list.append(home)
            print("INFO:Home Added Successfully")
            print("_"*30)
            show_home_list(home_list)

        case 2:
            address=input("Enter address:")
            if find_home_by_address(home_list,address):
                print("found")
            else:
                print("not found")
        case 3:
            print("Count=",len(home_list))
        case 0:
            print("Exit")
            break
        case _:
            print("Invalid Option")
    print("_"*30)