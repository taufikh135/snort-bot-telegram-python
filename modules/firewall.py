import subprocess

class Firewall:        
    def __command(self, command: str) -> str:
        return subprocess.check_output(command, shell=True, text=True)
    
    def __checkBlocked(self, ip: str) -> bool:
        result = self.__command(f"sudo iptables -S INPUT | grep {ip}/")
        return len(result) > 0
    
    def blockIP(self, ip: str) -> None:  
        if not self.__checkBlocked(ip):
            return
              
        self.__command(f"sudo iptables -I INPUT -s {ip} -j DROP")
        self.__blockedIP.append(ip)
    
    def removeBlockIP(self, ip: str) -> None:
        self.__command(f"sudo iptables -D INPUT -s {ip} -j DROP")
        
    def whitelistIP(self, ip: str) -> None:
        return self.__command(f"sudo iptables -I INPUT -s {ip} -j ACCEPT")