import subprocess
import argparse

# Color codes for formatting text
class color:
    HEADER = '\033[0;31m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# Function to perform ICMP Ping Scan
def icmp_ping_scan(target):
    print(color.GREEN + "Performing ICMP Ping Scan..." + color.END)
    subprocess.run(["ping", "-c", "4", target])

# Function to perform UDP Ping Scan
def udp_ping_scan(target):
    print(color.GREEN + "Performing UDP Ping Scan..." + color.END)
    subprocess.run(["hping3", "-2", "-c", "4", target])

# Function to perform SYN Scan
def syn_scan(target, ports):
    print(color.GREEN + "Performing SYN Scan..." + color.END)
    subprocess.run(["nmap", "-sS", "-p", ports, target])

# Function to perform Stealth Scan
def stealth_scan(target, ports):
    print(color.GREEN + "Performing Stealth Scan..." + color.END)
    subprocess.run(["nmap", "-sS", "-p", ports, "--scan-delay", "1", target])

# Function to perform FIN Scan
def fin_scan(target, ports):
    print(color.GREEN + "Performing FIN Scan..." + color.END)
    subprocess.run(["nmap", "-sF", "-p", ports, target])

# Function to perform Null Scan
def null_scan(target, ports):
    print(color.GREEN + "Performing Null Scan..." + color.END)
    subprocess.run(["nmap", "-sN", "-p", ports, target])

# Function to perform XMAS Scan
def xmas_scan(target, ports):
    print(color.GREEN + "Performing XMAS Scan..." + color.END)
    subprocess.run(["nmap", "-sX", "-p", ports, target])

# Function to perform Maimon Scan
def maimon_scan(target, ports):
    print(color.GREEN + "Performing Maimon Scan..." + color.END)
    subprocess.run(["nmap", "-sM", "-p", ports, target])

# Function to perform ACK Scan
def ack_scan(target, ports):
    print(color.GREEN + "Performing ACK Scan..." + color.END)
    subprocess.run(["nmap", "-sA", "-p", ports, target])

# Function to perform TTL Scan
def ttl_scan(target, ports):
    print(color.GREEN + "Performing TTL Scan..." + color.END)
    subprocess.run(["nmap", "--ttl", "1", "-p", ports, target])

# Function to perform Window Scan
def window_scan(target, ports):
    print(color.GREEN + "Performing Window Scan..." + color.END)
    subprocess.run(["nmap", "-sW", "-p", ports, target])

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description=color.BLUE + "Network Port Discovery Tool" + color.END)
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 1-100,443,8080)")
    args = parser.parse_args()

    # Main loop for user interaction
    while True:
        # Display ASCII art title
        print(color.HEADER + """
 ____            _     ____                                  
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   

        """ + color.END)

        # Display menu options
        print(color.BLUE + "Select a port discovery technique:")
        print("1. ICMP Ping Scan")
        print("2. UDP Ping Scan")
        print("3. TCP Scan")
        print("4. Exit" + color.END)

        # User input for choice
        choice = input(color.YELLOW + "Enter your choice: " + color.END)

        # Perform selected action based on user choice
        if choice == "1":
            icmp_ping_scan(args.target)
        elif choice == "2":
            udp_ping_scan(args.target)
        elif choice == "3":
            if args.ports is None:
                print(color.RED + "Please specify ports using the -p/--ports option" + color.END)
            else:
                syn_scan(args.target, args.ports)
                stealth_scan(args.target, args.ports)
                fin_scan(args.target, args.ports)
                null_scan(args.target, args.ports)
                xmas_scan(args.target, args.ports)
                maimon_scan(args.target, args.ports)
                ack_scan(args.target, args.ports)
                ttl_scan(args.target, args.ports)
                window_scan(args.target, args.ports)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print(color.RED + "Invalid choice" + color.END)
