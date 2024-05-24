import subprocess

class Firewall:
    def __command(self, command: str) -> str:
        return subprocess.run(command, capture_output=True, text=True).stdout
    
    def blockIp(self, ip: str) -> str:
        return self.__command(f"iptables -s {ip} -j DROP")
    
    def allowIp(self, ip: str) -> None:
        return self.__command(f"iptables -s {ip} -j ACCEPT")