from string import ascii_uppercase, digits
from os import system, name
from random import choice
from requests import get
from sys import maxsize
from time import sleep
import config

used_vanity = []

def clearConsole():
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

def randomString(size=8, chars=ascii_uppercase + digits + "_" + "-"):
	return ''.join(choice(chars) for _ in range(size))

def main():
	clearConsole()
	print('How many characters would you like to search for?')
	amount = int(input())
	for _ in range(maxsize**10):
		vanityURL = randomString(amount)
		if vanityURL in used_vanity:
			vanityURL = randomString(amount)
		resp = get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={config.steamAPIKey}&vanityurl={vanityURL}").json()
		if resp['response']['success'] == 1:
			print(f'\033[91mVanity URL Taken: {vanityURL}\033[0m')
			used_vanity.append(vanityURL) 
		else:
			print(f'\033[92mAvalible Vanity URL found: {vanityURL}\033[0m')
			break
		sleep(config.delay)
		
main()
