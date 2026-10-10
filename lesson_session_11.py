from lesson_module import *

lesson_list=[]

while True:
    choice = show_menu()
    print("_"*30)

    match choice:
        case 1:
            print("Enter Lesson Information")
            lesson=get_lesson_data()
            sum_unit=sum(map(lambda course: course["unit"], lesson_list))
            if lesson["unit"] in [1, 2, 3, 5] and (sum_unit + lesson["unit"]) <= 17:
                lesson_list.append(lesson)
                print("INFO:Lesson Added Successfully")
            else:
                print("Invalid")

        case 2:
          show_lesson_list(lesson_list)

        case 3:
          show_sum_of_units(lesson_list)

        case 0:
            print("Exit")
            break

        case _:
            print("Invalid Option")

    print("_"*30)