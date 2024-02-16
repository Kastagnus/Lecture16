import requests

result = requests.get("https://fakestoreapi.com/products")

list1 = result.json()
price_list = []
category_list = []
title_id_list = []
rating_list = []
for x in list1:
    price_list.append(x["price"])

for x in list1:
    category_list.append(x["category"])

for x in list1:
    title_id_list.append({"title": x["title"], "id": x["id"]})

for x in list1:
    rating_list.append(x["rating"]["rate"])



print(f"minimum - {min(price_list)}, maximum - {max(price_list)}, average - {sum(price_list) / len(price_list)}")

print(sorted(set(category_list)))

print(sorted(title_id_list, key=lambda x: x["title"]))

print(sorted(rating_list))
