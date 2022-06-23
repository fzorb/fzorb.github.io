from discum import *
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

print(bcolors.OKCYAN + " ______           _       _   ")
print("|___  /          | |     | |     Made and maintained by fzorb")
print("   / /  ___  __ _| | ___ | |_    https://zealot.fzorb.xyz/")
print("  / /  / _ \/ _` | |/ _ \| __|   s/o to Kishyu, scraf, tried")
print("./ /__|  __/ (_| | | (_) | |_    reddy, elina and Aja")
print("\_____/\___|\__,_|_|\___/ \__| \n ")

token1 = input(bcolors.OKBLUE + "Token No 1: ")
token2 = input(bcolors.OKBLUE + "Token No 2: ")
token3 = input(bcolors.OKBLUE + "Token No 3: ")
message = input(bcolors.OKBLUE + "Message to spam: ")
channel = input("Channel to attack: ")

print(bcolors.OKGREEN + "Alright, everything is configured. Initializing the selfbot 😈")

a = input(bcolors.FAIL + bcolors.BOLD + "Waiting for user input...")

for i in range(1024):
    discum.Client(token=token1, log=False).sendMessage(channel, message)
    discum.Client(token=token2, log=False).sendMessage(channel, message)
    discum.Client(token=token3, log=False).sendMessage(channel, message)
