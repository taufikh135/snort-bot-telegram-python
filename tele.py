from time import sleep
import subprocess

class Telegram:
    def __init__(self, apiKey: str) -> None:
        self.__apiKey = "API_KEY"
        
    def sendMessage(self, message: str) -> None:
        pass
    
class Firewall:
    def __command(self, command: str) -> str:
        return subprocess.run(command, capture_output=True, text=True).stdout
    
    def blockIp(self, ip: str) -> str:
        return self.__command(f"iptables -I INPUT -s {ip} -j DROP")
    
    def allowIp(self, ip: str) -> None:
        return self.__command(f"iptables -D INPUT -s {ip} -j DROP")
    
class Snort:    
    def __init__(self, logFile: str, telegram: Telegram, firewall: Firewall) -> None:
        self.__logFile = logFile
        self.__prevLog = self.__getAllLog().count()
        self.__currLog = self.__prevLog
        
    def __getAllLog(self) -> list:
        with open(self.__logFile, "r") as file:
            return file.read().splitlines()
        
    def __getLogByIndex(self, index: int) -> str:
        return self.__getAllLog()[index]
    
    def analyze(self) -> None:
        while True:
            
            sleep(2)
            
firewall = Firewall()
print(firewall.ls())