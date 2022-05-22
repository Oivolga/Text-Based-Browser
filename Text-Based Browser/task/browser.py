import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore

args = sys.argv
dir_name = args[-1]
tabs_list = []
index = 0
file_name = ''

if not os.access(dir_name, os.W_OK):
    os.mkdir(f'{dir_name}')

while True:
    adress = input()
    if adress == 'exit':
        break
    elif adress == 'back':
        if len(tabs_list) > 1:
            print(tabs_list[index - 1])
    else:
        if not adress.startswith("https://"):
            file_name = adress.split('.')[0]
            adress = "https://" + adress
        try:
            r = requests.get(adress)
            soup = BeautifulSoup(r.content, 'html.parser')
            for link in soup.find_all('a'):
                link.string = Fore.BLUE + link.get_text() + Fore.RESET
            text = soup.get_text()
            print(text)
            tabs_list.append(text)
            index = tabs_list.index(text)
            file_path = os.path.join(dir_name, file_name)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except requests.exceptions.ConnectionError:
            print('Incorrect URL')
