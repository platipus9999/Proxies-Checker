import threading, queue, os, time

try:
    import requests
except:
    input("You need requests to continue, Press enter to install it ")
    os.system('pip install -r requirements.txt')

def Title(content: str):
    if os.name == 'nt':
        os.system(f'title {content}')
    else:
        pass
def Clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def yellow_to_red(text: str): 
    col = ""
    green = 250
    for line in text.splitlines():
        col += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return col

class colors:
    GREEN = '\033[32m'
    RED = '\033[31m'
    WHITE = '\033[37m'

class Setup:
    def scrap():
        if "proxies.txt" not in os.listdir():
            list_proxies = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", 
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
            "https://raw.githubusercontent.com/rx443/proxy-list/main/online/all.txt",
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "http://alexa.lr2b.com/proxylist.txt",
            "http://olaf4snow.com/public/proxy.txt",
            "http://inav.chat.ru/ftp/proxy.txt",
            "http://hack-hack.chat.ru/proxy/allproxy.txt",
            "http://hack-hack.chat.ru/proxy/anon.txt",
            "http://hack-hack.chat.ru/proxy/p1.txt",
            "http://hack-hack.chat.ru/proxy/p2.txt",
            "http://hack-hack.chat.ru/proxy/p3.txt",
            "http://hack-hack.chat.ru/proxy/p4.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
            "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all"
            ]

            Title(f"Nows@Platipus ~ Proxz $ Proxies Checker [ Loading Proxies... ]")
            Clear()

            open("proxies.txt", "w+")

            for site in list_proxies:
                r = requests.get(site).text
                with open("proxies.txt", "a+") as f:
                    f.write(r)

            
        else:pass

    que = queue.Queue()

    with open("proxies.txt", "r") as f:
        proxies = f.read().split("\n")
        for p in proxies:
            que.put(p)

def check_proxies():
    Clear()
    while not Setup.que.empty():
        proxy = Setup.que.get()
        try:
            req = requests.get("http://ipinfo.io/json", proxies= {"http": proxy, "https": proxy})
        except:
            continue
        if req.status_code == 200:
            print(f"{colors.GREEN}[+] {colors.WHITE}{proxy}")

            with open("valid_proxies.txt", "a+") as v:
                v.write(f"{proxy}\n")

def remove_duplicate():
    Clear()
    with open("valid_proxies.txt", "r") as a:
        pro = a.read().split("\n")

    set1  = list(set(pro))
    new_proxies = ""
    
    for _ in set1:
        if _ == "":
            pass
        else:
            new_proxies += _+"\n"

    with open("valid_proxies.txt", "w+") as a:
        a.write(new_proxies)

    print(yellow_to_red("""
 ██▓███   ██▀███   ▒█████  ▒██   ██▒▒███████▒
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░▒ ▒ ▒ ▄▀░
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░░ ▒ ▄▀▒░ 
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ▄▀▒   ░
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒▒███████▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▒▒ ▓░▒░▒
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░░░▒ ▒ ░ ▒
░░         ░░   ░ ░ ░ ░ ▒   ░    ░  ░ ░ ░ ░ ░
            ░         ░ ░   ░    ░    ░ ░    
                                    ░
Dublicate Proxies Were Removed Successfully !"""))
    time.sleep(3)

