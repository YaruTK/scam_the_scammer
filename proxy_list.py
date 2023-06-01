import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open("proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


print(requests.get("http://ipinfo.io/json").status_code)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            print(f"checking proxy {proxy}")
            res = requests.get("http://ipinfo.io/json",
                               proxies={"http": proxy,
                                        "https": proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)


for _ in range(2):
    threading.Thread(target=check_proxies).start()
