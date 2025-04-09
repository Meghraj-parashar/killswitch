# KillSwitch

KillSwitch is a Python-based script that monitors the connection of a specific USB device (e.g., a wireless USB receiver). If the device is disconnected, the system will automatically shut down.

## Files

- **[killswitch.py](e:/killswitch/killswitch.py)**: The main Python script that monitors the USB device and triggers a shutdown when the device is removed.
- **[killswitch.bat](e:/killswitch/killswitch.bat)**: A batch file to run the Python script in the background.

## How It Works

1. The script continuously checks for the presence of a specific USB device using its Device ID.
2. If the device is removed, the script initiates a system shutdown.

## Prerequisites

- Python 3.x installed on your system.
- The `wmic` command must be available (default on Windows systems).

## Usage

1. Update the `receiver_id` variable in [killswitch.py](e:/killswitch/killswitch.py) with the Device ID of your USB device. You can find the Device ID using the `wmic path Win32_USBHub get DeviceID` command.
2. Run the batch file [killswitch.bat](e:/killswitch/killswitch.bat) to start the monitoring process.

