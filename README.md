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

## How to Use

## **Step 1: Clone or Download the Project**

```bash
git clone https://github.com/your-username/killswitch.git
cd killswitch
```

