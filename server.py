import socket

# Network dictionary
NETWORK = {
    '192.168.1.1': '00:0A:95:9D:68:16',
    '192.168.1.2': '00:0A:95:9D:68:17',
    '192.168.1.3': '00:0A:95:9D:68:18',
    '192.168.1.4': '00:0A:95:9D:68:19',
    '192.168.1.5': '00:0A:95:9D:68:1A',
    '192.168.1.6': '00:0A:95:9D:68:1B',
    '192.168.1.7': '00:0A:95:9D:68:1C',
    '192.168.1.8': '00:0A:95:9D:68:1D',
    '192.168.1.9': '00:0A:95:9D:68:1E',
    '192.168.1.10': '00:0A:95:9D:68:1F',
}

SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen()
    print("ARP server is listening...")

    # Keep the server running
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                ip = conn.recv(1024).decode('utf-8')
                if not ip: break
                mac = NETWORK.get(ip, None)
                response = mac if mac else 'Not Found'
                print(f"Received ARP request for IP: {ip}. Responded with: {response}")
                conn.sendall(response.encode('utf-8'))