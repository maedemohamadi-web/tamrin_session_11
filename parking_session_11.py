cars=[]

while True:
    print("1)Add Car:")
    print("2)Parking List:")
    print("3)Count:")
    print("0)Exit")

    option = int(input("Option: "))
    print("_____________________________________")

    match option:
        case 1:
            print("Enter Car Information")
            name=input("Enter Name of Car: ")
            color=input("Enter Car Color: ")
            plate=int(input("Enter Plate Number: "))

            car={
                "name":name,
                "color":color,
                "plate":plate
            }

            #plates=[]
            #for carr in cars:
               #plates.append(carr["plate"])
            #if plate not in plates:
               #cars.append(car)
               #print("Car added successfully")
           #else:
               #print("Plate already exists")
           #list_comprehension
            plates=list(map(lambda carss: carss["plate"],cars))
            if plate not in plates:
                cars.append(car)
                print("Car Added Successfully")
            else:
                print("Car Plate Already Exists")

        case 2:
            print("Parking List")
            print(cars)

        case 3:
            print("Count:",len(cars))

        case 0:
            print("Exit")
            break

        case _:
            print("Invalid Option")

    print("_____________________________________")