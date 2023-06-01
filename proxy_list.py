import threading
import queue

import requests

q = queue.Queue()
valid_proxies = []

with open("proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


print(q.qsize())
r = requests.get("https://github.com", timeout=10)
print(r)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            #print(f"checking proxy {proxy}")
            #print(q.qsize())
            res = requests.get("https://ipinfo.io/",
                               proxies={"http": proxy,
                                        "https": proxy})
            print(f"proxy {proxy}" + f"status {res.status_code}")
        except:
            continue
        if res.status_code == 200:
            print(proxy)


check_proxies()
