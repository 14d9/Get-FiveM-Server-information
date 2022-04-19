import requests, webbrowser, time

print("""
      _____    __    ____                       _      ___                    __  _         
     / ___/__ / /_  / __/__ _____  _____ ____  (_)__  / _/__  ______ _  ___ _/ /_(_)__  ___ 
    / (_ / -_) __/ _\ \/ -_) __/ |/ / -_) __/ / / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / _ \/ _ \ 
    \___/\__/\__/ /___/\__/_/  |___/\__/_/   /_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\___/_//_/                                                                                       
""")
print("""
      [1] Get FiveM Server information
      [0] Exit
""")

choice = int(input('Choose number :'))

# Exit
if choice == 0 :
    print('Goodbye see you later <3')
    time.sleep(2)
    exit()

# Get FiveM Server information
if choice == 1 :
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
        instagram = 'https://www.instagram.com/q97l/'

                
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
