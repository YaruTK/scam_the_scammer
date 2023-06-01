import random
import string
import time

from selenium import webdriver
from selenium.webdriver .chrome.service import Service
from webdriver_manager .chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


scammers_site = "https://challengereumode.com/#"

connect_button = '/html/body/main/div[3]/div[1]/div/div/div[1]/div[2]/div/a'
login_button = '/html/body/main/div[3]/div[3]/div/div/div/div[2]/a'
iframe = '/html/body/div/div/iframe'
sign_in_button = '/html/body/div/div/div[4]/div[2]/div/div[1]/div/div/div/div[2]/div/div/div[4]/button'

with open("valid_proxies.txt", 'r') as f:
    proxy_list = f.read().split('\n')


def rand_proxy():
    proxy = random.choice(proxy_list)
    return proxy


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')


def launchBrowser(a, b, c):
    chrome_options.add_argument(f'--proxy-server={a}')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get(scammers_site)
    browser.find_element(By.LINK_TEXT, "SIGN UP").click()
    time.sleep(0.3)
    browser.find_element(By.XPATH, connect_button).click()
    time.sleep(0.3)
    browser.find_element(By.XPATH, login_button).click()
    time.sleep(0.3)
    browser.switch_to.frame(browser.find_element(By.XPATH, iframe))
    browser.find_element(By.XPATH, '//input[@type="text"]').send_keys(b)
    time.sleep(1)
    browser.find_element(By.XPATH, '//input[@type="password"]').send_keys(c)
    time.sleep(1)
    browser.find_element(By.XPATH, sign_in_button).click()
    time.sleep(3)
    browser.quit()


def random_email(a, b):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(a, b))) + "@gmail.com"


def random_password(a, b):
    return ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(a, b)))


count = 0

while True:
    p = rand_proxy()
    e = random_email(8, 15)
    w = random_password(10, 20)
    try:
        launchBrowser(p, e, w)
        count += 1
    except:
        pass
    finally:
        print(f'Sent {count} fake instances, used {p} as proxy')

