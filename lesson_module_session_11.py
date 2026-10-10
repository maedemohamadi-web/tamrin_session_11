def show_menu():
    print("1)Add Lesson")
    print("2)Print Lesson List")
    print("3)Sum Lesson")
    print("0)Exit")
    choice = int(input("Choice: "))
    return choice

def get_lesson_data():
    title = input("Enter Title: ")
    teacher = input("Enter Teacher: ")
    code = int(input("Enter Code: "))
    unit = int(input("Enter Unit: "))

    lesson = {
        "title": title,
        "teacher": teacher,
        "code": code,
        "unit": unit
    }
    return lesson

def show_lesson_list(lesson_list):
    print("Lesson List:")
    print("{:^10} {:^10} {:^10} {:^10}" .format("title","teacher","code","unit"))
    for lesson in lesson_list:
        print("{:^10} {:^10} {:^10} {:^10}".format(lesson["title"], lesson["teacher"],lesson["code"],lesson["unit"]))

def show_sum_of_units(lesson_list):
    print("Sum of units:")
    sum_unit = 0
    result_sum=sum(map(lambda lesson: lesson["unit"], lesson_list))
    print(sum_unit)
