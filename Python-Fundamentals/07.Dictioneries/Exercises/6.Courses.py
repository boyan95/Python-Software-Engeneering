command = input()
courses = {}
as_list = []
while not command == "end":
    course_name, student_name = command.split(" : ")
    if not course_name in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    command = input()
new_dict = {}
for key, value in courses.items():
    new_dict[key] = len(value)
my_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))

for key, value in courses.items():
    courses[key] = sorted(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")
    mey_dict_2 = dict(sorted(new_dict.items(), key=lambda x: x[1]))
    for course_name, student_name in courses.items():
        if value == 1 and course_name == key:
            print(f"-- {' '.join(student_name)}")
        elif value > 1 and course_name == key:
            a = '\n-- '.join(student_name)
            print(f"-- {a}")
