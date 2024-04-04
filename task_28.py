import time, threading, concurrent.futures, requests

# 1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე
odd = []
even = []
def do_odd():
    for x in range(30,51):
        if x%2 == 0:
            even.append(x)
            time.sleep(1)
    return "Done Even"

def do_even():
    for x in range(30,51):
        if x%2 != 0:
            odd.append(x)
            time.sleep(1)
    return "Done Odds"


# =============
start = time.time()

t1 = threading.Thread(target=do_even)
t2 = threading.Thread(target=do_odd)

# პროცესის შექმნა
t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"\nFinishing in {end - start} seconds...")
print(odd)
print(even)

# =========================================================
# 2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

mp3_urls = ["https://shorturl.at/quI57", "https://shorturl.at/LPT26", "https://shorturl.at/aeBKM", "https://shorturl.at/VX468"]

def download_mp3(url):


    file_name = url.split("/")[-1]
    result = requests.get(url)
    with open(file_name, mode="wb") as file:
        file.write(result.content)
    print(f"Downloaded {file_name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_mp3, mp3_urls)