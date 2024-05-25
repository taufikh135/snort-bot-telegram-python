import subprocess

class Firewall:    
    def __command(self, command: str) -> str:
        return subprocess.check_output(command, shell=True, text=True)
    
    def blockIP(self, ip: str) -> str:        
        return self.__command(f"sudo iptables -I INPUT -s {ip} -j DROP")
    
    def removeBlockIP(self, ip: str) -> str:
        return self.__command(f"sudo iptables -D INPUT -s {ip} -j DROP")
        
    def allowIP(self, ip: str) -> None:
        return self.__command(f"sudo iptables -I INPUT -s {ip} -j ACCEPT")