# Network_scanner


# Overview

This is a Python-based network scanner that identifies active devices in a network by performing an ARP (Address Resolution Protocol) scan. It retrieves the IP and MAC addresses of devices within a specified target IP range.

# Features

Scans a specified IP range to find active devices.

Retrieves and displays IP and MAC addresses of connected devices.

Command-line interface for ease of use.

# Requirements

Ensure you have the following installed:

Python (3.x recommended)

Scapy library

You can install Scapy using:

pip install scapy

# How to Use

Clone this repository or download the script.

Open a terminal and navigate to the script's directory.

Run the script with the following syntax:

python network_scanner.py -t <target>

Example:

python network_scanner.py -t 192.168.1.1/24

Here, 192.168.1.1/24 specifies the IP range to scan.

# Script Details

Functions

get_arguments():

Parses command-line arguments to accept a target IP or IP range.

scan(ip):

Sends ARP requests to the specified IP range.

Combines the ARP request with an Ethernet frame to broadcast it.

Collects responses and extracts IP and MAC addresses.

print_res(result_list):

Displays the scanned results in a tabular format.

# Example Output

IP			MAC Address
---------------------------------------------------
192.168.1.1		00:11:22:33:44:55
192.168.1.2		66:77:88:99:AA:BB

# Limitations

The script requires administrative/root privileges to run.

Designed for local network scanning; will not work across the internet.

May miss devices with firewalls blocking ARP requests.


# Disclaimer

This tool is intended for educational and ethical purposes only. Unauthorized network scanning may violate laws or regulations. Use responsibly.

