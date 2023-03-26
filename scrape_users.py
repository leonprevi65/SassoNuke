import os
import json
import requests_futures.sessions

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')

#guild_id = input("Guild ID: ")

headers = {
        'Authorization': f'Bot {token}'
    }

session = requests_futures.sessions.FuturesSession()
def scrape(guild_id):
    try:
        os.remove("scraped/members.txt")
        os.remove("scraped/channels.txt")
        os.remove("scraped/roles.txt")
    except:
        pass
    # Fetch members
    members_url = f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000"
    members_response = session.get(members_url, headers=headers).result()
    members_data = members_response.json()
    
    members_file = open("scraped/members.txt", "a+")
    for member in members_data:
        member_id = member['user']['id']
        members_file.write(f"{member_id} \n")
    members_file.close()

    # Fetch channels
    channels_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    channels_response = session.get(channels_url, headers=headers).result()
    channels_data = channels_response.json()
    
    channels_file = open("scraped/channels.txt", "a+")
    for channel in channels_data:
        channels_file.write(f"{channel['id']}\n")
    channels_file.close()

    # Fetch roles
    roles_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    roles_response = session.get(roles_url, headers=headers).result()
    roles_data = roles_response.json()
    
    roles_file = open("scraped/roles.txt", "a+")
    for role in roles_data:
        roles_file.write(f"{role['id']}\n")
    roles_file.close()

    print("IDs scraped successfully!")
