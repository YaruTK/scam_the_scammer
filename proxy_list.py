import queue
import threading
import requests

q = queue.Queue()
valid_proxies = []

with open("proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)


def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            #print(f"checking proxy {proxy}")
            #print(q.qsize())
            res = requests.get("https://challengereumode.com/l20x340rfymp.html#",
                               proxies={"http": proxy,
                                        "https": proxy})
        except:
            continue
        if res.status_code == 200:
            print(proxy)


for _ in range(10):
    threading.Thread(target=check_proxies).start()
