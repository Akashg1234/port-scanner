import socket
from IPy import IP
socket.setdefaulttimeout(100)

class PortScanner():
    banner=[]
    open_ports=[]
    def __init__(self,target,port_number):
        self.target=target
        self.port_number=port_number
    
    def get_banner(self,sock_obj):
        return sock_obj.recv(1024)

    def check_ip(self):
        try:
            IP(self.target)
            
            return self.target
        except ValueError:
            #print(socket.gethostbyname(self.target))
            return socket.gethostbyname(self.target)

    def scan_port(self,port):
        try:
            converted_ip = self.check_ip()
            print("\n [0_Q] Scanning target ... "+str(self.target))
            sock=socket.socket()
            sock.connect((converted_ip,port))
            self.open_ports.append(port)
            try:
                banner = self.get_banner(sock_obj=sock)
                self.banner.append(banner)
                #print("[+] Port {} is open : {} ".format(port,banner.decode().strip('\n')))
            except ValueError:
                self.banner.append('--')
                #print("[+] Port {} is open ".format(port))
            sock.close()
        except ProcessLookupError:
            pass
            # print("[-] Port {} is closed".format(port))
    def scan(self):
        for port in range(self.port_number):
            self.scan_port(port)

