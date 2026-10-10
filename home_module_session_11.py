def show_menu():
    print("1)Add")
    print("2)Search")
    print("3)Count")
    print("0)Exit")
    option = int(input("Option: "))
    return option

def get_home_data():
    address= input("Address: ")
    owner = input("Owner: ")
    number_of_rooms = int(input("Number of rooms: "))
    parking =(input("Parking(yes/no)?: "))

    home = {
        "address": address,
        "owner": owner,
        "number_of_rooms": number_of_rooms,
        "parking": parking
    }
    return home

def show_home_list(home_list):
    print("Home List:")
    print("{:^20} {:^20} {:^20} {:^20}" .format("address","owner","number of rooms","parking"))
    for item in home_list:
        print("{:^20} {:^20} {:^20} {:^20}".format(item["address"], item["owner"], item["number_of_rooms"], item["parking"]))

def find_home_by_address(home_list,address):
    address_result=list(filter(lambda home: home["address"] == address, home_list))
    if address_result:
        return address_result[0]
    return None