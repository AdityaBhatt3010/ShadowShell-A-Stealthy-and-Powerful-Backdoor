# 🔥 ShadowShell – A Stealthy and Powerful Backdoor

### **A covert, feature-rich reverse shell for ethical hacking and penetration testing.**

---

## 📌 About the Project
**ShadowShell** is a **Python-based backdoor** designed for cybersecurity professionals and penetration testers.  
It provides a **persistent, stealthy reverse shell**, enabling secure **remote command execution, file transfer, keylogging, screenshot capture, and system information gathering.**  

This tool is intended for **authorized security assessments and educational purposes only.**  

---

## ⚡ Features
✅ **Reverse Shell** – Execute remote commands on the target system.  
✅ **Persistence Mechanism** – Ensures the backdoor runs after reboot (Windows).  
✅ **File Transfer (Upload & Download)** – Move files between attacker and target.  
✅ **Screenshot Capture** – Remotely take screenshots of the target’s screen.  
✅ **Keylogger** – Capture keystrokes in the background.  
✅ **System Information Gathering** – Get OS details, username, IP, and more.  
✅ **Stealth Mode** – Runs undetected in the background.  
✅ **Improved Reliability** – Enhanced exception handling for stability.  

---

## 📂 Project Structure
```bash
📦 ShadowShell
├── backdoor.py        # Client-side (Target Machine) - Runs as a background process
├── server.py          # Server-side (Attacker Machine) - Controls the backdoor
├── requirements.txt   # Requirements File 
├── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 📌 **Step 1: Clone the Repository**
```bash
git clone https://github.com/YourGitHubUsername/ShadowShell.git
cd ShadowShell
```

### 📌 **Step 2: Install Dependencies**
Ensure Python3 is installed. Install required dependencies:
```bash
pip install -r requirements.txt
```

### 📌 **Step 3: Run the Server (Attacker Machine)**
Modify `server.py` with your **attacker IP** and execute:
```bash
python server.py
```

### 📌 **Step 4: Deploy the Backdoor (Target Machine)**
Modify `backdoor.py` with your **server IP**, then execute:
```bash
python backdoor.py
```
For **Windows Persistence**, compile it to an executable:
```bash
pyinstaller --onefile --noconsole backdoor.py
```

---

## 🎯 Usage Guide

### **Available Commands in the Attacker Console**
| Command         | Description |
|----------------|-------------|
| `quit`        | Terminate the connection |
| `clear`       | Clear the attacker’s terminal |
| `cd <dir>`    | Change directory on the target machine |
| `download <file>` | Download a file from the target |
| `upload <file>` | Upload a file to the target |
| `screenshot`  | Capture and download the target’s screen |
| `sysinfo`     | Retrieve OS, hostname, username, and IP details |

---

## ⚠️ Legal Disclaimer
**This tool is strictly for ethical hacking and authorized penetration testing.**  
**The aim of this tool is for authorized security assessments and educational purposes only.**  
**The author holds no responsibility for any unauthorized use of this tool.**  

Use **ShadowShell** responsibly and only with explicit permission from the target system owner.  

---

## 🤝 Contribution
Contributions, feature suggestions, and pull requests are welcome!  
Feel free to fork and enhance **ShadowShell** with new capabilities.  

---

### 💻 **Developed by:** Aditya Bhatt  
