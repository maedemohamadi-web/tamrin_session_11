from call_module import *

call_list=[]

while True:
    option=show_menu()
    print("_"*30)

    match option:
        case 1:
            print("Enter call information")
            call=get_call_data()
            call_list.append(call)
            print("INFO:Call Information Added Successfully")
            print("_"*30)
            show_call_list(call_list)

        case 2:
            phone_number=int(input("Enter phone number:"))
            result=find_call_by_phone_number(call_list,phone_number)
            if result is not None:
                print("found")
                print("Name:",result["name"])
            else:
                print("not found")
        case 3:
            print("Count=",len(call_list))
        case 0:
            print("Exit")
            break
        case _:
            print("Invalid Option")
    print("_"*30)