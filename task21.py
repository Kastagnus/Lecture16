import json

class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def to_dict(self):
        return {'city': self.city, 'street': self.street}

    @staticmethod
    def from_dict(data):
        return Address(data['city'], data['street'])


class Student:
    _id_counter = 1

    def __init__(self, name, mark, address):
        self.id = Student._id_counter
        Student._id_counter += 1
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.assign_grade(mark)

    @staticmethod
    def assign_grade(mark):
        if 91 <= mark <= 100:
            return 'A'
        elif 81 <= mark <= 90:
            return 'B'
        elif 71 <= mark <= 80:
            return 'C'
        elif mark <= 70:
            return 'D'
        else:
            return 'Invalid mark'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mark': self.mark,
            'address': self.address.to_dict(),
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data):
        address = Address.from_dict(data['address'])
        student = cls(data['name'], data['mark'], address)
        student.id = data['id']
        Student._id_counter = max(Student._id_counter, student.id + 1)
        return student


address1 = Address('New York', '5th Ave')
student1 = Student('Will Smith', 75, address1)

address2 = Address('New Jersey', '19 Lincoln Ave')
student2 = Student('Mark Zuckerberg', 95, address2)

address3 = Address('Chicago', '10 Michigan Ave')
student3 = Student('Donald Trump', 100, address3)

address4 = Address('Washington', '18th Street NW')
student4 = Student('Joe Biden', 45, address4)

students = [student1, student2, student3, student4]


def save_students(students, filename='students.json'):
    with open(filename, 'w') as f:
        json.dump([student.to_dict() for student in students], f, indent=4)


def load_students_from_json(filename='students.json'):
    with open(filename, 'r') as file:
        students_data = json.load(file)
    return students_data


def update_student_by_id(student_id, new_mark=None, new_address=None, filename='students.json'):
    with open(filename, 'r') as f:
        students_data = json.load(f)

    if student_id > len(students_data):
        print("id out of range")
    if new_mark is not None and not isinstance(new_mark, int):
        print("The 'mark' must be an integer.")
        return
    if new_address is not None and not isinstance(new_address, dict):
        print("The 'address' must be a dictionary.")
    if new_mark is None and new_address is None:
        print("Provide at least one, mark or address")

    for student_data in students_data:
        if student_data['id'] == student_id:
            if new_mark is not None:
                student_data['mark'] = new_mark
                student_data['grade'] = Student.assign_grade(new_mark)
                print("Mark has been updated!")
            if new_address is not None:
                student_data['address'].update(new_address)
                print("Address has been updated!")
            break

    with open(filename, 'w') as f:
        json.dump(students_data, f, indent=4)


def add_new_student(new_student, filename='students.json'):

    student_data = load_students_from_json()
    student_data.append(new_student.to_dict())

    with open(filename, 'w') as file:
        json.dump(student_data, file, indent=4)
    print("New student added successfully.")

save_students(students)

# თუ გაუშვებთ ქვედა კოდს განაახლებს რიგით მეოთხე სტუდენტის მონაცემებს
# new_mark = 100
# new_address = {"city": "Michigan", "street": "Apple Ave"}
#
# update_student_by_id(4, new_mark=new_mark, new_address=new_address)

#თუ გაუშვებთ ქვედა კოდს დაამატებს მეხუთე სტუდენტს სიაში
# address5 = Address('colorado', 'wisconsin ave')
# student5 = Student('Abraham Lincoln', 51, address5)
# add_new_student(student5)
