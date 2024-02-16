import json
import os

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

# საქაღალდის შექმნა
def create_folder(folder_name):
  try:
    os.mkdir(folder_name)
    print("Folder Successfully created ! Continue working...")
  except FileExistsError:
    print("folder already exists! continue...")
# ქმნის ჯეისონ ფორმატის ფაილს მითითებულ ფოლდერში. თუ მსგავსი უკვე არსებობს მაშინ გვეუბნება რომ უკვე არსებობს
def create_file(file_path, file_name):
    full_path = f"{file_path}/{file_name}.json"
    try:
        file = open(full_path, 'x', encoding="utf-8")
        file.close()
    except FileExistsError as ex:
        print(f"File already exists on path {full_path}")
        print("You can work on that file")
    return full_path


# წინასწარ შექმნილ ფაილში ჩაწერს ჯეისონ ფორმატით გადაცემულ მონაცემებს
def write_file(file_path, json_data):
    with open(file_path, "w", encoding="utf-8") as fout:
        fout.write(json.dumps(json_data))

# ფუნქცია დააბრუნებს ჯეისონ ფორმატის ფაილში ჩაწერილ ინფორმაციას
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as fin:
        return json.loads(fin.read())

# ფუნქციას უნდა გადავცეთ ჯეისონ ფორმატის ფაილის მისამართი და ჩვენთვის სასურველი მონაცემები. ფუნქცია განაახლებს/დაამატებს გადაცემულ ინფორმაციას
def update_file(file_path, json_data):
    data = read_file(file_path)
    data.append(json_data)
    write_file(file_path, data)
    return data

new_data = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

# ფუნქციას უნდა გადავცეთ ჯეისონ ფორმატის ფაილის მისამართი და ლექსიკონების სია. ფუნქცია ახალ ლექსიკონებს ჩაამატებს ჯეისონ ფორმატის ფაილში და დააბრუნებს განახლებულ ინფორმაციას
def add_new_data(file_path, new_data):
    for dict in new_data:
        update_file(file_path, dict)
    return read_file(file_path)

# ფუნქციების შესრულება მიმდევრობით

create_folder("task14")
file_path = create_file("task14", "json_data")

write_file(file_path, chess_players)

content = read_file(file_path)
print(content)
print(update_file(file_path, {"id": 1000, "name": "newname", "country": "China", "rating": 100}))


new_content = add_new_data(file_path, new_data)
print(new_content)