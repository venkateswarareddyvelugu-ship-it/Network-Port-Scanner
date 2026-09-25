import socket
from datetime import datetime

target = input("Enter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname or IP address.")
    exit()

print("\n========================================")
print("       NETWORK PORT SCANNER")
print("========================================")
print("Target :", target)
print("IP     :", target_ip)
print("Time   :", datetime.now())
print("----------------------------------------")

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Proxy"
}

print("\nPort\tStatus\tService")
print("----------------------------------------")

for port, service in common_ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        print(f"{port}\tOPEN\t{service}")

        try:
            sock.sendall(b"\r\n")
            banner = sock.recv(1024).decode(errors="ignore").strip()

            if banner:
                print("      Banner:", banner[:80])
        except:
            pass
    else:
        print(f"{port}\tCLOSED\t{service}")

    sock.close()

print("----------------------------------------")
print("Scan completed.")