
# Port Scanner

A simple TCP port scanner built with Python to identify open ports on a given IP address or hostname.

## 💡 Features

- Scans ports 1 through 100 by default
- Uses TCP sockets with timeout
- Resolves hostnames to IP addresses
- Measures and displays scan duration
- Gracefully handles invalid inputs

## 🛠 Built With

- Python `socket` module
- `datetime` for scan timing

## 📸 Sample Output

Enter the IP address or hostname to scan: scanme.nmap.org

Starting scan on: 45.33.32.156
[OPEN] Port 22
[OPEN] Port 80

Scan completed in: 0:00:05.123456


## ⚠️ Legal Notice

This tool is for **educational and ethical use only**. Never scan a system or network you don't own or have explicit permission to test.

## 👨‍💻 Created by

Shahakar Patel  
Cybersecurity Enthusiast | Learning by building
