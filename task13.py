my_dict = {
    "students": [
        {"id": 20, "name": "giorgi", "age": 25},
        {"id": 25, "name": "giorgi", "age": 23},
        {"id": 100, "name": "nika", "age": 22},
        {"id": 56, "name": "nika", "age": 25},
        {"id": 1232, "name": "dato", "age": 22},
        {"id": 846723, "name": "archili", "age": 32}
    ],
    "subjects": [
        {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "100": "A", "56": "B", "1232": "C", "846723": "A"}},
        {"id": 2, "name": "Physics",
         "grades": {"20": "A", "25": "B", "100": "A", "56": "B", "1232": "C", "846723": "B"}},
        {"id": 3, "name": "English",
         "grades": {"20": "A", "25": "A", "100": "A", "56": "A", "1232": "B", "846723": "A"}},
        {"id": 4, "name": "Chemistry",
         "grades": {"20": "B", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
        {"id": 5, "name": "History",
         "grades": {"20": "C", "25": "B", "100": "A", "56": "B", "1232": "A", "846723": "A"}},
    ]
}


# გამოგვაქვს აიდი-ების სია და მომხმარებლის ინფუთს ვიღებთ
def start_over():
    print("List of IDs: ", end=" ")
    for x in my_dict["students"]:
        print(f"{x["id"]}", end=" ")
    user_input = input("\nEnter the ID of the student you would like to check: ")
    return user_input


# მომხმარებლის ინფუთის შესაბამისი ინფორმაციას ვეძებთ ბიბლიოთეკაში და ვბეჭდავთ
def retrive_information(user_input):
    print("Student Information:")
    for x in my_dict["students"]:
        if x["id"] == int(user_input):
            for key, value in x.items():
                print(f"{key} : {value}", end=" ")
    print("\n")
    for i in my_dict["subjects"]:
        print("Subject: " + i["name"] + " " + "Grade " + i["grades"][user_input])


# პროგრამის გამშვები, მოწმდება შეყვანილი მონაცემის სისწორე და იძახებს შესაბამის ფუნქციას
def run():
    while True:
        list_of_ids = [x["id"] for x in my_dict["students"]]
        user_input = start_over()

        try:
            int(user_input)
            if int(user_input) in list_of_ids:
                retrive_information(user_input)
                break
            else:
                print("Incorrect ID!, Please choose from below list")
                continue
        except:
            print("Invalid input entered!, Please choose from numbers below")
            continue


run()
