import random
import string
import bs4 as bs
from urllib.request import Request, urlopen


def random_email(a, b):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(a, b))) + "@gmail.com"


def random_password(a, b):
    return ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(a, b)))


req = Request(
    url='https://challengereumode.com/#',
    headers={'User-Agent': 'Mozilla/5.0'}
)
source = urlopen(req, timeout=10).read()
soup = bs.BeautifulSoup(source, 'lxml')
print(source)

#print(random_email(6, 12) + " " + random_password(12, 18))
