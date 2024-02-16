import os
import csv

# ქმნის საქაღალდეს, თუ არსებობს აგრძელებს მუშაობას
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder Successfully created ! Continue working...")
        return folder_name
    except FileExistsError:
        print("folder already exists! continue...")
        return folder_name

# ქმნის CSV ფორმატის ფაილს, და თუ არსებობს აგრძელებს მუშაობას
def create_file(file_path, file_name):
    full_path = f"{file_path}/{file_name}.csv"
    try:
        file = open(full_path, 'x', encoding="utf-8")
        file.close()
    except FileExistsError as ex:
        print(f"File already exists on path {full_path}")
        print("You can work on that file")
    return file_path

# ვინახავთ სტუდენტის ინფორმაციას რასაც გადავწერთ CSV ფაილში
data = [

]

# კითხულობს ფაილს და აბრუნებს ფაილის შიგთავსს გადაცემულ მისამათზე
def file_reader(path):
    with open(f'{path}', mode='r', encoding='utf-8', newline='') as file:
        reader = list(csv.DictReader(file))
    return reader

# ამოწმებს იუზერის შეყვანილ ასაკს, თუ სტუდენტის ასაკი 6 და 80 წელს შორისაა ვეკითხებით დარწმუნებულია თუ არა მონაცემის სისწორეში
def confirm_age(age):
    while age > 80 or age < 6:
        print(f"Age you entered is {age}, are you sure you want to continue? Yes or No")
        confirmation = input().lower()
        if confirmation == 'yes':
            return age
        elif confirmation == 'no':
            age = ask_for_integer("Please, enter age of the student: ")
        else:
            print("Enter yes or no !")
    return age

# ამოწმებს მომხმარებელმა ველში შეიყვანა თუ არა ციფრი
def ask_for_integer(input_text):
    while True:
        try:
            number = int(input(input_text))
            return number
        except ValueError:
            print("Please, enter an integer")


csv.register_dialect("my_dialect", delimiter="=")

# თუ ფაილი არსებობს და ფაილში ჩანაწერიცაა დაამატებს მხოლოდ ახალ დატას. თუ ფაილში არაფერი გვაქვს მოცემული ჯერ დაამატებს გაწერილ ჰედერებს და შემდგომ სტუდენტის ინფორმაციას
def write_file(file_path):
    fields = ["id", "name", "age", "subject_name", "marks"]
    file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

# ვიღებთ მომხმარებლსგან სტუდენტის შესახებ ინფორმაციას. გზად ვამოწმებთ მოცემული ID -ზე არსებობს თუ არა სტუდენტი
def ask_info():
    continue_process = False
    student_data = file_reader(full_path)
    while not continue_process:
        student_id = ask_for_integer("Please, enter your student ID: ")
        for i in student_data:
            if i["id"] == str(student_id):
                print("Student with this ID already exists. Please, Provide valid ID")
                break
        else:
            continue_process = True

        while continue_process:
            name = input("please, enter student name: ")
            age = confirm_age(ask_for_integer("Please, enter age of the student: "))
            subject_name = input("please, enter name of the subject: ")
            marks = ask_for_integer("Please, enter the marks of the student: ")
            new_student = {"id": student_id, "name": name, "age": age, "subject_name": subject_name, "marks": marks}
            data.append(new_student)
            return new_student

# ფაილის მისამართის, სტუდენტის აიდის და საგნის სახელით ვეძებთ სტუდენტს და ფუნქციაში გადაცემული ქულით შეიცვლება ფაილში მიმდინარე ქულა კონკრეტულ საგანში
def update_file(path, student_id, subject, mark):
    updated_student = [

    ]
    id_found = False
    subject_found = False
    with open(path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for i in list(reader):
            if i["id"] == str(student_id):
                id_found = True
                if i["subject_name"] == subject:
                    i['marks'] = mark
                    print("Successfuly updated!")
                    subject_found = True
            updated_student.append(i)

    if not id_found:
        print("student does not exist")
        return False
    if not subject_found:
        print("Incorrect subject")
        return False
    with open(full_path, "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_student)
        return True

folder_name = create_folder("task15")
file_path = create_file(folder_name, "students")
full_path = f"{file_path}/students.csv"

# მონაცემის აღების და ფაილში ჩაწერის გამშვები
def run_entry():
    ask_info()
    write_file(full_path)
    while True:
        confirmation = input("Do you want to add other student? Yes or No: ").lower()
        if confirmation == "yes":
            ask_info()
        elif confirmation == "no":
            print("Successfully added students to your CSV File")
            break
        else:
            print("Please, Enter Yes or No")

# მონაცემების წამკითხველის გამშვები
def run_read():
    student_data = file_reader(full_path)
    while True:
        confirmation = input("for all students write 'all', for single student write student ID: ")
        w1 = 10
        w2 = 20
        if confirmation.lower() == "all":
            count = 0
            for student in student_data:
                if count == 0:
                    x = list(student.keys())
                    print(f"{x[0]:<{w1}}{x[1]:<{w1}}{x[2]:<{w1}}{x[3]:<{w2}}{x[4]}")
                    print('=' * 60)
                    count += 1
                print(
                    f"{student["id"]:<{w1}}{student['name']:<{w1}}{student['age']:<{w1}}{student['subject_name']:<{w2}}{student['marks']}")
                print('-' * 60)
            break
        elif confirmation.isdigit():
            for student in student_data:
                if student["id"] == confirmation:
                    x = list(student.keys())
                    print(f"{x[0]:<{w1}}{x[1]:<{w1}}{x[2]:<{w1}}{x[3]:<{w2}}{x[4]}")
                    print('=' * 60)
                    print(
                        f"{student["id"]:<{w1}}{student['name']:<{w1}}{student['age']:<{w1}}{student['subject_name']:<{w2}}{student['marks']}")
                    print('-' * 60)
            break
        else:
            print("Invalid entry, Please enter valid ID or 'all' to continue")

# მონაცემის განახლების გამშვები
def run_update():
    print("enter Student ID, Subject and Mark. it will update corresponding student information")
    while True:
        student_id = ask_for_integer("enter student ID: ")
        subject = input("enter subject name: ")
        mark = ask_for_integer("enter student mark: ")

        if update_file(full_path, student_id, subject, mark):
            break
        else:
            print("Please enter valid information")


run_entry()
run_read()
run_update()
