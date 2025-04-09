import time
import os
import subprocess

# This is the device ID of your wireless USB receiver
receiver_id = "USB\\VID_046D&PID_C534"

def is_receiver_connected():
    try:
        output = subprocess.check_output('wmic path Win32_USBHub get DeviceID', shell=True).decode()
        return receiver_id in output
    except Exception as e:
        print("Error:", e)
        return False

print("Waiting for USB receiver to be connected...")

# Step 1: Wait for receiver to be connected
while not is_receiver_connected():
    time.sleep(1)

print("Receiver detected. Monitoring...")

# Step 2: Start monitoring
while True:
    if not is_receiver_connected():
        print("Receiver removed. Shutting down...")
        os.system("shutdown /s /t 1")
        break
    time.sleep(1)
# E:\killswitch
