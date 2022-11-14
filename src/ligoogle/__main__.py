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


def run(command):
    os.system(command)

os.system('cls' if os.name=='nt' else 'clear')

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

while True:
    search = input(color.BOLD + color.GREEN + "search@google " + color.END + color.END + color.BLUE  + color.BOLD + "$ " + color.END + color.END)
    if str(search) == "command:app":
        from ligoogle import app_google
    else:
        cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
        cls()
        print("Hang on tight! Scraping your results...")
        from magic_google import MagicGoogle
        PROXIES = None
        mg = MagicGoogle(PROXIES)
        case = 0
        searchresultgoogle = []
        cls()
        for i in mg.search(query=search, num=10):
            case += 1
            print(color.BOLD + "RESULT " + str(case) + ": " + color.GREEN + i["title"] + color.END + color.END)
            print("URL: " + i["url"])
            searchresultgoogle.append(i["url"])
            print("\n\n")
        resultopen = input(color.BOLD + color.GREEN + "result@google " + color.UNDERLINE + "(number of result to open/q to go back to search)" + color.END + color.END + color.END + color.BLUE  + color.BOLD + "$ " + color.END + color.END)
        if resultopen == "q":
            cls()
        else:
            import webbrowser
            webbrowser.open(searchresultgoogle[int(resultopen) - 1], new = 2)
            cls()
