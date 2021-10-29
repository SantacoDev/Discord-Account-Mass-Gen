import os, time, requests;from colorama import Fore, Style
os.system('cls & mode 83, 22')
f = open('proxies.txt','wb')
#proxytype = input(f"{Fore.CYAN}{Style.BRIGHT}>{Fore.RESET} ProxyType [http/https/socks4/socks5]{Fore.CYAN}{Style.BRIGHT}:{Fore.RESET} ")
proxytype = 'http'
#if proxytype not in ['http', 'https', 'socks4', 'socks5']:
	#print(f'{Fore.CYAN}{Style.BRIGHT}>{Fore.RESET} Invalid Choice.')
	#time.sleep(5)
	#os._exit(0)
r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxytype}&timeout=10000&country=all")
f.write(r1.content)
f.close()
print(f'{Fore.CYAN}{Style.BRIGHT}>{Fore.RESET} Successfully scraped proxies.\n{Fore.CYAN}{Style.BRIGHT}>{Fore.RESET} You may close this window.')
input()