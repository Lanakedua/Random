#!/usr/bin/env python3
# Created By X - MrG3P5
import pyfiglet
import requests
import os
from time import sleep
from datetime import datetime
from pytz import timezone
from colorama import Fore, init

# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE

init(autoreset=True)

def logTime():
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone("Asia/Jakarta"))
    return now_pacific.strftime("%H:%M:%S")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{red}[ {white}Created By Lana | Backup {red}]")
def start():
    input_auth = input(f"{red}[{white}?{red}] {white}Enter your auth token : ")
    round_input = input(f"{red}[{white}?{red}] {white}Enter round (1, 2, 3) : ")
    delay_input = input(f"{red}[{white}?{red}] {white}Enter Delay (ex: 1 = 1sec) : ")

    while True:
        try:
            sleep(int(delay_input))
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{round_input}", headers={
                "authorization": input_auth
            })
            if "BANNED" in str(req_game.text) or req_game.status_code == 403:
                print(f"{red}[{yellow}*{red}] {white}You Got Banned")
                break
            elif "SERVER_ERROR" in str(req_game.text):
                continue
            elif "User" in str(req_game.text):
                print(f"======================")
                print(f"Nickname: {green}{req_game.json()['User']['Username']}")
                print(f"Country: {green}{req_game.json()['User']['Country']}")
                print(f"Trophy: {green}{req_game.json()['User']['SkillRating']}")
                print(f"Crown: {green}{req_game.json()['User']['Crowns']}")
                print(f"CREATED LANA | Backup")
        except:
            continue

if __name__=="__main__":
    start()
