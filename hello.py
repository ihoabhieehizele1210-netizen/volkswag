services = ["21 : FTP", "22 : SSH", "23 : Telnet"]

for port in services:
    print(port)

for port in services:
    if "22" in port:
        print(port)