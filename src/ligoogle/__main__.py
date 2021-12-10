class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import os
import http.client
import urllib.parse
import urllib
import json

key = "72ddb23f61mshd7034341804bcedp12906djsned505dec18e5"
def run(command):
    os.system(command)
print("""
‖ Unofficial .g8'''''bgd                               `7MM                    ‖ 
‖           .dP´     `M                                 MM                     ‖ 
‖           dm´       `   ,pW"Wq.   ,pW"Wq.   .P"Ybmmm  MM  .gP"Ya             ‖ 
‖           MM           6W´   `Wb 6W´   `WB :MI  I8    MM ,M´   Yb            ‖ 
‖           MM.    `7MMF´8M     MB 8M     M8  WmmmP"    MM 8M''''''            ‖ 
‖           `Mb      MM  YA.   ,A9 YA.   ,A9 8M         MM YM.    ,            ‖ 
‖             `"bmmmdPY   `Ybmd9´   `Ybmd9´   YMMMMMb .JMML.`Mbmmd´            ‖ 
‖                                            6´     dP                         ‖ 
‖                         The Linux Google    Ybmmmd´                          ‖
""")
print(color.PURPLE + "Loading google..." + color.END)
run("sleep 1")
print(color.BLUE + "Loading host..." + color.END)
run("sleep 1")
while True:
    search = input(color.GREEN + "search@google " + color.END + color.BLUE  + color.BOLD + "$ " + color.END + color.END)
    if str(search) == "api-change":
        ask = input("Enter API key: ")
        key = ask
    elif str(search) == "app":
        from ligoogle import app_google
    else:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("Hang on tight! Scraping your results...")
        print("")
        print("")
        print("")
        conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")
        headers = {
            'x-user-agent': "desktop",
            'x-proxy-location': "US",
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "72ddb23f61mshd7034341804bcedp12906djsned505dec18e5"
        }
        conn.request("GET", "/api/v1/search/q=elon+musk&num=100", headers=headers)
        res = conn.getresponse()
        data = res.read()
        result = data.decode("utf-8")
        your_json = result
        parsed = json.loads(your_json)
        print(json.dumps(parsed, indent=4, sort_keys=True))