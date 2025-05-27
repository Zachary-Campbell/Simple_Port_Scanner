import socket
from datetime import datetime

# ----------------------------------------
# Simple Port Scanner
# Author: Zachary Campbell
# Description: This script scans for open
# TCP ports on a target IP address.
# ----------------------------------------

# Define the function to perform the scan
def scan_ports(target_ip, start_port, end_port):
    print(f"\nStarting scan on {target_ip}")
    print(f"Scanning ports {start_port} to {end_port}...\n")

    open_ports = []  # List to store open ports

    # Record the start time
    start_time = datetime.now()

    # Loop through each port in the given range
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)  # Timeout to prevent hanging

        result = sock.connect_ex((target_ip, port))  # Try to connect to the port
        if result == 0:
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    # Record the end time
    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\nScan completed in {duration}")
    print(f"Open ports: {open_ports if open_ports else 'None found'}")

# Main execution
if __name__ == "__main__":
    print("=== Simple Port Scanner ===")

    # Get user input
    target = input("Enter the target IP address (e.g., 192.168.1.1): ")
    start = int(input("Enter the starting port (e.g., 1): "))
    end = int(input("Enter the ending port (e.g., 1024): "))

    scan_ports(target, start, end)
