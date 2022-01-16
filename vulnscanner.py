import portscanner as ps

targets_ip = input("[+] Enter target/s (separate by ',') :: ")
port_number = int(input("[+] Enter number of Ports you want to scan :: "))
vuln_scan = input("[+] Enter File path to you want to store information :: ")

target = ps.PortScanner(targets_ip,port_number)
target.scan()

with open(vuln_scan.txt,'r') as file:
    count=0
    for banner in target.banner:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print("[!!] VULNARABLE BANNER :: {} ON PORT :: {}".format(banner,target.open_ports[count]))
        count+=1
