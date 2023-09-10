import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432
ARP_TABLE = {}

print("Initial ARP Table:", ARP_TABLE)

while True:
    ip = input("Enter IP to ARP for: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        s.sendall(ip.encode('utf-8'))
        mac = s.recv(1024).decode('utf-8')
        mac = None if mac == 'Not Found' else mac

    if mac:
        ARP_TABLE[ip] = mac
        print(f"Received ARP reply: {ip} is at {mac}")
    else:
        print(f"No ARP Reply for {ip}")
    print("Current ARP Table:", ARP_TABLE)