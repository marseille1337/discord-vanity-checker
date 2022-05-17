import time, threading, colorama, requests
from colorama import Fore

vanity = open('vanitys.txt', 'r').read().split('\n')
available = open('avaible.txt', 'w')

def marseille1377():
    for marseille in vanity:
        r = requests.get(f'https://discord.com/api/v9/invites/{marseille}')
        if r.status_code == 200:
            print(Fore.RED + marseille + Fore.YELLOW +  ' > ' + Fore.MAGENTA + 'Taken!')
        if r.status_code == 404:
            print(Fore.RED + marseille + Fore.YELLOW +  ' > ' + Fore.MAGENTA + 'Not taken!')
            available.write(f'{marseille}\n')
  
thread = threading.Thread(target=marseille1377)
thread.start()