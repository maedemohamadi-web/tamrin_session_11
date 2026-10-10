def show_menu():
    print("1)Add")
    print("2)Search")
    print("3)Count")
    print("0)Exit")
    option = int(input("Option: "))
    return option

def get_call_data():
    name= input("Name: ")
    last_name = input("Last Name: ")
    phone_number = int(input("Phone Number: "))
    title =input("Title: ")

    call = {
        "name": name,
        "last_name": last_name,
        "phone_number": phone_number,
        "title": title,
    }
    return call

def show_call_list(call_list):
    print("Call List:")
    print("{:^20} {:^20} {:^20} {:^20}" .format("name", "last_name", "phone_number", "title")),
    for call in call_list:
        print("{:^20} {:^20} {:^20} {:^20}".format(call["name"], call["last_name"], call["phone_number"], call["title"]))


def find_call_by_phone_number(call_list,phone_number):
   result=list(filter(lambda call: call["phone_number"] == phone_number, call_list))
   if result:
       return result[0]
   return None