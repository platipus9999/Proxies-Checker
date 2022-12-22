from check_proxies import *

def main():
    Clear()
    Title(f"Nows@Platipus ~ Proxz $ Proxies Checker [/]")
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
[1]Check Proxies
[2]Remove Duplicate Proxies"""))
    choice = int(input(f"{colors.RED}>"))
    if choice == 1:
        t1 = threading.Thread(target=Setup.scrap)
        t1.start()
        t1.join()

        with open("proxies.txt", "r") as num:
                num_proxies = len(num.read().strip("\n"))

        Title(f"Nows@Platipus ~ Proxz $ Proxies Checker [ Proxies from the sources: ({num_proxies}) ]")
        
        t2 = threading.Thread(target=Setup)
        t2.start()
        t2.join()
        thread = int(input("Amout of Thread > "))
        for _ in range(thread):
            threading.Thread(target=check_proxies).start()
    if choice == 2:
        remove_duplicate()

if "__main__" == __name__:
    os.system("")
    main()
