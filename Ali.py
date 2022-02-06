import requests
import webbrowser
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

print("""
      _____    __    ____                       _      ___                    __  _         
     / ___/__ / /_  / __/__ _____  _____ ____  (_)__  / _/__  ______ _  ___ _/ /_(_)__  ___ 
    / (_ / -_) __/ _\ \/ -_) __/ |/ / -_) __/ / / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / _ \/ _ \ 
    \___/\__/\__/ /___/\__/_/  |___/\__/_/   /_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\___/_//_/                                                                                       
""")
print("""
      [1] Get FiveM Server information [With Webhook]
      [2] Get FiveM Server information [Without webhook]
      [0] Exit
""")

choice = int(input('Choose number :'))



# Exit
if choice == 0 :
    print('Goodbye see you later <3')
    time.sleep(2)
    exit()

# Get FiveM Server information [With Webhook]
if choice == 1 :
        server = input("[+] SERVER CFX : ")

        webhook_url = input( "[+] YOUR WEBHOOK : ")
        if webhook_url == '':
                print("[-] WRITE THE WEBHOOK")
                time.sleep(1)
                print("[!] After 3 seconds [Get IP information] will be closed automatically")
                time.sleep(3)
        url = ("https://servers-frontend.fivem.net/api/servers/single/"+server)
        headers = {
                'path': f'/api/servers/single/{server}',
                'accept': 'application/json',
                'accept-language': 'en',
                'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
        }
        req = requests.get(url,headers=headers)
        instagram = 'https://www.instagram.com/14d9/'

                
        print(" ")
        print(" ")
        print(" ")
        print("Server IP : ",req.json()["Data"]["connectEndPoints"])
        print("Server Name : ",req.json()["Data"]["hostname"])
        print("Players : ",req.json()["Data"]["clients"])
        print("UpVotes : ",req.json()["Data"]["upvotePower"])
        print("Max Players : ",req.json()["Data"]["sv_maxclients"])
        print("Owner Name : ",req.json()["Data"]["ownerName"])
        print("Owner Profile : ",req.json()["Data"]["ownerProfile"])

        webhook = DiscordWebhook(url=f"{webhook_url}", username="Instagram : @14d9", avatar_url="https://cdn.discordapp.com/attachments/838674685452484608/939825286021787708/0.png")

        embed = DiscordEmbed(title='Ali | Get FiveM Server information', description=f'**IP : {req.json()["Data"]["connectEndPoints"]}\nServer Name : {req.json()["Data"]["hostname"]}\nPlayers : {req.json()["Data"]["clients"]}\nUpVotes : {req.json()["Data"]["upvotePower"]}\nMax Players : {req.json()["Data"]["sv_maxclients"]}\nOwner Name : {req.json()["Data"]["ownerName"]}\nOwner Profile : {req.json()["Data"]["ownerProfile"]}\nBanner Connecting : {req.json()["Data"]["vars"]["banner_connecting"]}\nBanner Detail : {req.json()["Data"]["vars"]["banner_detail"]}\nsv_projectName : {req.json()["Data"]["vars"]["sv_projectName"]}\nsv_projectDesc : {req.json()["Data"]["vars"]["sv_projectDesc"]}\nonesync_enabled : {req.json()["Data"]["vars"]["onesync_enabled"]}\nLocale : {req.json()["Data"]["vars"]["locale"]}**', color='000000')
        embed.set_image(url='https://cdn.discordapp.com/attachments/838674685452484608/939825250714152970/600x200.png')

        embed.set_footer(text='Created By Ali || Instagram @14d9')

        webhook.add_embed(embed)
        response = webhook.execute()

        print("")
        print("")
        print("[+] Thank you for using my tool")
        time.sleep(1)
        webbrowser.open(instagram)
        print("")
        print("[!] After 5 seconds [Get FiveM Server information] will be closed automatically")
        time.sleep(5)

# Get FiveM Server information [Without webhook]
if choice == 2 :
        server = input("[+] SERVER CFX : ")
        if server == '':
                print("[-] WRITE THE SERVER CFX")
                time.sleep(1)
                print("[!] After 3 seconds [FiveM Server information] will be closed automatically")
                time.sleep(3)
        url = ("https://servers-frontend.fivem.net/api/servers/single/"+server)
        headers = {
                'path': f'/api/servers/single/{server}',
                'accept': 'application/json',
                'accept-language': 'en',
                'user-agent': 'ios:2.65.0:488:14:iPhone13,3',
        }
        req = requests.get(url,headers=headers)
        instagram = 'https://www.instagram.com/14d9/'

                
        print(" ")
        print(" ")
        print(" ")
        print("Server IP : ",req.json()["Data"]["connectEndPoints"])
        print("Server Name : ",req.json()["Data"]["hostname"])
        print("Players : ",req.json()["Data"]["clients"])
        print("UpVotes : ",req.json()["Data"]["upvotePower"])
        print("Max Players : ",req.json()["Data"]["sv_maxclients"])
        print("Owner Name : ",req.json()["Data"]["ownerName"])
        print("Owner Profile : ",req.json()["Data"]["ownerProfile"])

        print("")
        print("")
        print("[+] Thank you for using my tool")
        time.sleep(1)
        webbrowser.open(instagram)
        print("")
        print("[!] After 5 seconds [Get FiveM Server information] will be closed automatically")
        time.sleep(5)