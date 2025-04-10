# KillSwitch

## Description
**KillSwitch** is a Python-based security tool that automatically shuts down your Windows laptop if a specific USB receiver (like the one used for a wireless keyboard/mouse) is removed. This can act as a personal kill switch to prevent unauthorized access if someone physically tampers with your system.

It's useful for:
- Security-conscious users
- Public setups
- Personal privacy in shared environments

---

## Features
- **Auto-shutdown** on USB receiver removal
- **Runs silently in background**
- **Prevents multiple instances** from running simultaneously
- Can be added to **startup** for automatic launch

---

## How it Works
1. Waits for a specific USB receiver to be connected
2. Once connected, monitors the connection continuously
3. If the receiver is removed, the system **immediately shuts down

# How to Use

## **Step 1: Clone or Download the Project**

```bash
git clone https://github.com/your-username/killswitch.git
cd killswitch
```
## **Step 2: Customize the USB Detection**
1. Open ```killswitch.py``` and update the ```is_receiver_connected()``` function with your receiver's name or Device ID.

2. Use this command to view USB devices in your terminal:
```bash
wmic path Win32_USBHub get DeviceID, Description
```
## **Test the Scipt**
Run the script using:
```bash
python killswitch.py
```
## **Convert to Executable**
Install PyInstaller:
```bash
pip install pyinstaller
```
Then build the .exe:
```bash
pyinstaller --noconsole --onefile killswitch.py

```
## **Step 5: Add to Startup (Optional)**
1. To run KillSwitch at boot:

2. Press ```Win + R```

3. Type ```shell:startup``` and hit Enter

4. Copy ```killswitch.exe``` into that folder

# Author
```Meghraj Parashar```

## Note
This app is powerful and shuts down your system if the USB receiver is removed. Test carefully and use responsibly.
