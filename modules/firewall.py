import subprocess

class Firewall:
    __whitelistIP = []
    
    def __command(self, command: str) -> str:
        return subprocess.run(command, capture_output=True, text=True).stdout
    
    def blockIP(self, ip: str) -> str:
        if ip in self.__whitelistIP:
            return "IP already whitelisted"
        
        return self.__command(f"iptables -s {ip} -j DROP")
    
    def allowIP(self, ip: str) -> None:
        return self.__command(f"iptables -s {ip} -j ACCEPT")
    
    def addWhitelistIP(self, ip: str) -> None:
        self.__whitelistIP.append(ip)
        self.allowIP(ip)