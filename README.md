# Scan Sentry

Scan Sentry is a powerful and flexible network port discovery tool designed to help you identify open ports on a target machine. It supports various scanning techniques, including ICMP ping, UDP ping, and several types of TCP scans, providing a comprehensive view of your network security.

## Features

- **ICMP Ping Scan**: Checks if a target is alive by sending ICMP echo requests.
- **UDP Ping Scan**: Probes target using UDP packets to discover open UDP ports.
- **TCP Scans**: Includes multiple TCP scan types such as SYN, Stealth, FIN, Null, XMAS, Maimon, ACK, TTL, and Window scans.

## Installation

To use Scan Sentry, you need Python installed on your system. Additionally, you will need `nmap` and `hping3` for performing the scans. You can install these dependencies using the following commands:

```sh
sudo apt-get install nmap
sudo apt-get install hping3
```

## Usage

Run Scan Sentry from the command line with the target IP address or hostname and the ports to scan (for TCP scans).

### Basic Syntax

```sh
python scansentry.py <target> -p <ports>
```

### Example

```sh
python scansentry.py 192.168.1.1 -p 1-100,443,8080
```

### Command Line Options

- `target`: The target IP address or hostname.
- `-p` or `--ports`: Ports to scan (e.g., `1-100`, `443`, `8080`).

## Menu Options

After running the script, you will be presented with a menu to select the desired scan type:

1. **ICMP Ping Scan**: Performs an ICMP ping scan.
2. **UDP Ping Scan**: Performs a UDP ping scan.
3. **TCP Scan**: Performs various TCP scans (SYN, Stealth, FIN, Null, XMAS, Maimon, ACK, TTL, Window) on the specified ports.
4. **Exit**: Exits the program.

## Example Usage

```sh
python scansentry.py 192.168.1.1 -p 1-100,443,8080
```

### After starting the program:

```sh
 ____                    ____             _              
/ ___|  ___ __ _ _ __   / ___|  ___ _ __ | |_ _ __ _   _ 
\___ \ / __/ _` | '_ \  \___ \ / _ \ '_ \| __| '__| | | |
 ___) | (_| (_| | | | |  ___) |  __/ | | | |_| |  | |_| |
|____/ \___\__,_|_| |_| |____/ \___|_| |_|\__|_|   \__, |
                                                   |___/ 

Select a port discovery technique:
1. ICMP Ping Scan
2. UDP Ping Scan
3. TCP Scan
4. Exit
```

Enter the desired choice to perform the scan.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and ensure you have permission to scan the target network.

## Authors

- **[PAARTHARNAZ](https://github.com/PAARTHARNAZ)**
  
---
Happy scanning with Scan Sentry!
