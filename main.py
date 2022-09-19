from string import ascii_uppercase, digits
from json import JSONDecodeError
from os import system, name
from random import choice
from requests import get
from sys import maxsize
from time import sleep
import bcolors
import config

used_vanity = []

def clearConsole():
	command = 'clear'
	if name in ('nt', 'dos'):
		command = 'cls'
	system(command)

def startupCheck():
	check = get(f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={config.steamAPIKey}&vanityurl=')
	if check.status_code == 403:
		print(f'{bcolors.WAITMSG}Steam API Key is invalid. Please check config.py{bcolors.ENDC}')
		exit()

def randomString(size=8, chars=ascii_uppercase + digits + '_' + '-'):
	return ''.join(choice(chars) for _ in range(size))

def start(amount):
	search(amount)

def search(amount):
	for _ in range(maxsize**10):
		vanityURL = randomString(amount)
		if vanityURL in used_vanity:
			vanityURL = randomString(amount)
		try:
			resp = get(f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={config.steamAPIKey}&vanityurl={vanityURL}').json()
		except JSONDecodeError:
			start(amount)
		if resp['response']['success'] == 1:
			print(f'{bcolors.ERRMSG}Vanity URL Taken: {vanityURL}{bcolors.ENDC}')
			used_vanity.append(vanityURL) 
		else:
			print(f'{bcolors.OKMSG}Avalible Vanity URL found: {vanityURL}{bcolors.ENDC}')
			break
		sleep(config.delay)

def main():
	clearConsole()
	startupCheck()
	print('How many characters would you like to search for?')
	amount = int(input())
	start(amount)

main()
