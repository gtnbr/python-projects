from objects import Student, Staff

def load_file(filepath):
    '''Loads the file with the appropriate classes from objects.py'''
    with open(filepath, "r") as f:
        info = [line.split(": ") for line in f]
        students = []
        staff = []
        for i in info:
            if "Student" in i[0]:
                students.append(Student(str(i[1])[:-1], int(i[0].split(" ")[1])))
            elif "Staff" in i[0]:
                staff.append(Staff(str(i[1])[:-1], int(i[0].split(" ")[1])))
        grade_info = []
        advisee_info = []
        for i in info:
            if "Grade" in i[0].split()[0]:
                grade_info.append(i[0].split())
            if "Advisee" in i[0].split()[0]:
                advisee_info.append(i[0].split())
        for g in grade_info:
            for s in students:
                if int(g[1]) == s.get_id():
                    s.set_grade(g[2], int(g[3]))
        for a in advisee_info:
            for st in staff:
                for s in students:
                    if int(a[1]) == st.get_id():
                        if int(a[2]) == s.get_id():
                            st.add_advisee(s)
        x = [s.average_grade() for s in students]
        global_average = sum(x)/len(x)
        return {"Students": students, "Staff": staff, "GA": global_average}

def is_excellent_student(filepath, student):
    '''Returns True if the student is excellent.'''
    return student.average_grade() > load_file(filepath)["GA"]

def is_excellent_staff(filepath, staff):
    '''Returns True if the staff member is excellent'''
    excellent_students = 0
    for advisee in staff.get_advisees():
        if is_excellent_student(filepath, advisee):
            excellent_students += 1
    return (staff.advisees_average_grades() > load_file(filepath)["GA"]) and (excellent_students*2 > len(staff.get_advisees()))

def count_excellent_staff(filepath):
    '''Counts all excellent staff members.'''
    db = load_file(filepath)
    count = 0
    for staff_member in db["Staff"]:
        if is_excellent_staff(filepath, staff_member):
            count += 1
    return count

def is_elite_student(filepath, student):
    '''Returns true if the student is elite.'''
    if not is_excellent_student(filepath, student):
        return False
    for staff_member in load_file(filepath)["Staff"]:
        if is_excellent_staff(filepath, staff_member):
            return True
    return False

def count_elite_students(filepath):
    '''Counts all elite student members.'''
    db = load_file(filepath)
    count = 0
    for student in db["Students"]:
        if is_elite_student(filepath, student):
            count += 1
    return count

def elite_students_average_grade(filepath):
    '''Returns the average value of all elite students.'''
    db = load_file(filepath)
    grades = []
    for student in db["Students"]:
        if is_elite_student(filepath, student):
            grades.append(student.average_grade())
    return int(sum(grades)/len(grades))

def best_module(filepath):
    '''Returns the module with the best average grades.'''
    with open(filepath, "r") as f:
        info = [line.split(": ") for line in f]
    grade_info = []
    for i in info:
        if "Grade" in i[0].split()[0]:
            grade_info.append(i[0].split()[2:])
    modules = set()
    for i in grade_info:
        modules.add(i[0])
    grade_info2 = {m: [0, 0, 0] for m in modules}
    for i in grade_info:
        grade_info2[i[0]][0] += int(i[1])
        grade_info2[i[0]][1] += 1
        grade_info2[i[0]][2] = grade_info2[i[0]][0]/grade_info2[i[0]][1]
    grade_averages = []
    for i in grade_info2.values():
        grade_averages.append(i[2])
    best_grade_average = sorted(grade_averages, reverse=True)[0]
    answer = set()
    for key in grade_info2:
        if grade_info2[key][2] == best_grade_average:
            answer.add(key)
    return answer
