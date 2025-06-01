import socket
from datetime import datetime

# Shahakar Patel
# Port Scanner
# 6/1/2025

# Step 1: Ask user for input. 
target = input("Enter the IP address or hostname to scan: ")

# Step 2: Have a failsafe incase user decides to mash keyboard. 
try: 
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname or IP address.")
    exit()
print(f"\nStarting scan on: {target_ip}")

# Step 3: Captures the time the scanner begins and captures the end time 
#         to see how long it took to finsih scanning. 
start_time = datetime.now()

# Step 4: Scanning ports in a loop, we'll scan ports and try to connect to each one. 

for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    sock.close()

# AF_INET uses IPv4 and SOCK_STREAM uses TCP, not UDP
# We neeed to create a new socket every time, or the old one might stay open

# Step 5: Capturing the end time. 

end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")


