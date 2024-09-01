import requests 
import json 
import platform 
import os 


if "linux" in str(platform.platform()).lower():
    os.system("clear") 
else: 
    os.system("cls")

def checker(ip,port): 
    reponse = requests.get(f"https://api.mcstatus.io/v2/status/java/{ip}:{port}")   
    raw_data = reponse.text
    data = json.loads(raw_data)  
    if data["online"] == False: 
        pass
    else: 
        players_on =  data["players"]["online"]
        players_max = data["players"]["max"]
        version =  data["version"]["name_clean"] 
        motd =  data["motd"]["clean"]
        print(f"({ip}:{port})({players_on}/{players_max})({version})({motd})")

def main(): 
    print("""
Allah akbar v1.0 
 @SkiddingLover on telegram         
""") 
    result_file = input("[+] Put your file here: ") 
    with open(result_file,"r") as f:  
        for line in f: 
            clean_line = line.strip("\n").split(",")  
            ip = clean_line[0] 
            port = int(clean_line[1])  
            checker(ip,port)


main()