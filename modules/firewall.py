import subprocess

class Firewall:    
    __blockedIP = []
    
    def __command(self, command: str) -> str:
        return subprocess.check_output(command, shell=True, text=True)
    
    def blockIP(self, ip: str) -> None:  
        if ip in self.__blockedIP: 
            return
              
        self.__command(f"sudo iptables -I INPUT -s {ip} -j DROP")
        self.__blockedIP.append(ip)
    
    def removeBlockIP(self, ip: str) -> None:
        self.__command(f"sudo iptables -D INPUT -s {ip} -j DROP")
        
    def allowIP(self, ip: str) -> None:
        return self.__command(f"sudo iptables -I INPUT -s {ip} -j ACCEPT")