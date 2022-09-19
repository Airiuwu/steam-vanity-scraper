from string import ascii_uppercase, digits, ascii_lowercase
from random import choice
from requests import get
from sys import maxsize
from time import sleep
from os import system
import config

def randomString(size=8, chars=ascii_uppercase + digits + ascii_lowercase + "_" + "-"):
	return ''.join(choice(chars) for _ in range(size))

def main():
    system('cls')
    print('How many characters would you like to search for?')
    amount = int(input())
    for i in range(maxsize**10):
        vanityURL = randomString(amount)
        resp = get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={config.steamAPIKey}&vanityurl={vanityURL}").json()
        if not resp['response']['steamid']:
            print(f'\033[92mAvalible Vanity URL found: {vanityURL}\033[0m')
            break
        else:
            print(f'\033[91mVanity URL Taken: {vanityURL}\033[0m')
        sleep(0.017674)

main()